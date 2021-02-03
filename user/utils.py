import jwt

from django.http      import JsonResponse

from my_settings      import SECRET
from user.models      import User

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
            print('0'*50)
            print(token)
            payload      = jwt.decode(token, SECRET, algorithms='HS256')
            request.user = User.objects.get(id=payload['user_id'])
        except:    
            request.user = None
        return func(self, request, *args, **kwargs)
    return wrapper