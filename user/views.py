import requests
import jwt

from django.http      import JsonResponse
from django.views     import View
from .models          import User

from my_settings      import SECRET

class KakaoSignInView(View):
    def get(self, request):
        try:
            access_token = request.headers.get('Authorization', None)
            headers      = {'Authorization': f'Bearer {access_token}'}
            url          = 'https://kapi.kakao.com/v2/user/me'
            kakao_data   = requests.get(url, headers=headers).json()
            
            user, _ = User.objects.get_or_create(
                email            = kakao_data['kakao_account']['email'],
                gender           = kakao_data['kakao_account']['gender'],
                age              = kakao_data['kakao_account']['age'],
                drink_propensity = None,
            )
             
            access_token = jwt.encode({"user_id" : user.id}, SECRET, algorithm='HS256')

            return JsonResponse({'access_token': access_token}, status=201)

        except KeyError:
            return JsonResponse({'error': 'KEY_ERROR'}, status=400)
