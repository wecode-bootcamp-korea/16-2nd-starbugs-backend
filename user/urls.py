from django.urls import path
from .views      import KakaoSignInView

urlpatterns = [
    path('/kakao', KakaoSignInView.as_view())
]