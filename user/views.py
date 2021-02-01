import json
import requests
import jwt

from django.http      import JsonResponse
from django.views     import View
from .models          import User

from my_settings      import SECRET

class KakaoSignInView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            access_token = data['access_token']
            headers      = {'Authorization': f'Bearer {access_token}'}
            url          = 'https://kapi.kakao.com/v2/user/me'
            kakao_data   = requests.get(url, headers=headers).json()

            gender = kakao_data['kakao_account']['gender']
            age    = kakao_data['kakao_account']['age_range']

            user, _ = User.objects.get_or_create(
                email  = kakao_data['kakao_account']['email'],
            )
            
            user.gender = gender
            user.age    = age
            user.save()
             
            access_token = jwt.encode({"user_id" : user.id}, SECRET, algorithm='HS256')

            return JsonResponse({'access_token': access_token}, status=201)

        except KeyError:
            return JsonResponse({'error': 'KEY_ERROR'}, status=400)