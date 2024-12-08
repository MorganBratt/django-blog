from django.urls import path, include
from django_blog.users_and_groups import views
from rest_framework.routers import DefaultRouter

# DRF router for API endpoints
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # Traditional HTML views
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
