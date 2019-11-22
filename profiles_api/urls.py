from django.urls import path, include

# 기본 경로를 이용하기 위해 사용
from rest_framework.routers import DefaultRouter

from profiles_api import views

# router를 이용하여 손 쉽게 url 설정 가능
router = DefaultRouter()
# base_name은 url 쿼리문의 base 이름이 무엇인지 결정해준다.
# list, detail 등으로 어떤 값을 출력 할 지 결정한다.

# query set을 가지면 쿼리는 어떤 모델을 참조 할 지 자동으로 알게된다.
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
