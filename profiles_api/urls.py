from django.urls import path, include

# 기본 경로를 이용하기 위해 사용
from rest_framework.routers import DefaultRouter

from profiles_api import views

# router를 이용하여 손 쉽게 url 설정 가능
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
