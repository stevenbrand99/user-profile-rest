from django.urls import path, include
from profile_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile', views.UserProfileViewSet, basename='profile')
router.register(r'feed', views.UserProfileFeedViewSet, basename='feed')


urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]