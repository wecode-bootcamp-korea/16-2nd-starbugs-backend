import jwt
import functools, time


from django.http      import JsonResponse
from my_settings      import SECRET
from user.models      import User

from django.db        import connection, reset_queries

def check_user(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token        = request.headers.get('Authorization')
            payload      = jwt.decode(token, SECRET, algorithms='HS256')
            request.user = User.objects.get(id=payload['user_id'])

        except User.DoesNotExist:
            return JsonResponse({"message" : "User doest not exist"}, status=401)

        except jwt.DecodeError:
            return JsonResponse({"message" : "Not Authorized"}, status=401)

        return func(self, request, *args, **kwargs)

    return wrapper

def check_user_slider(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token        = request.headers.get('Authorization')
            payload      = jwt.decode(token, SECRET, algorithms='HS256')
            request.user = User.objects.get(id=payload['user_id'])
        except:    
            request.user = None
        return func(self, request, *args, **kwargs)
    return wrapper

def query_debugger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        reset_queries()
        number_of_start_queries = len(connection.queries)
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        end    = time.perf_counter()
        number_of_end_queries = len(connection.queries)
        print(f"-------------------------------------------------------------------")
        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {number_of_end_queries-number_of_start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        print(f"-------------------------------------------------------------------")
        return result
    return wrapper