import json

from django.test   import TestCase, Client
from unittest.mock import patch, MagicMock

client = Client()

class KakaoSignIn(TestCase):
    @patch('user.views.requests')
    def test_kakao_sign_in_success(self, mock):
        class FakeKakaoResponse:
            def json(self):
                return {
                    'id'           : '11234',
                    'kakao_account': {
                        'id'        : '12345',
                        'email'     : 'test@gmail.com',
                        'age_range' : '20~30',
                        'gender'    : 'Female'
                    }
                }

        access_token = {"access_token": 123456789}
        mock.get = MagicMock(return_value = FakeKakaoResponse())
        response     = client.post('/user/kakao', json.dumps(access_token), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"access_token": response.json().get("access_token")})

    def test_kakao_sign_in_key_error(self):

        response = self.client.post('/user/kakao', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error":"KEY_ERROR"})