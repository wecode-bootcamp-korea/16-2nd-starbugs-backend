from django.test   import TestCase, Client
from requests.api import head
from unittest.mock import patch, MagicMock

client = Client()

class KakaoSignIn(TestCase):

    @patch('user.views.requests')
    def test_kakao_sign_in_success(self, mocked_request):
        class KakaoResponse:
            def json(self):
                return {
                    'id'           : '11234',
                    'kakao_account': {
                        'id'        : '12345',
                        'email'     : 'test@gmail.com',
                        'age'       : '20~30',
                        'gender'    : 'Female'
                    }
                }

        mocked_request.get = MagicMock(return_value = KakaoResponse())

        response = self.client.get('/user/kakao', content_type='application/json')
        self.assertEqual(response.status_code, 201)

    @patch('user.views.requests')
    def test_kakao_sign_in_key_error(self, mocked_request):
        class KakaoResponse:
            def json(self):
                return {
                    'id' : '11234',
                }

        mocked_request.get = MagicMock(return_value = KakaoResponse())

        response = self.client.get('/user/kakao', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error":"KEY_ERROR"})