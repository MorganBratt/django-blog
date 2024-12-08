from django.urls import path, include
from blogging.views import PostListView, PostDetailView, PostViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

# DRF router for API endpoints
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    # Traditional HTML views
    path('', PostListView.as_view(), name="blog_index"),  # Render list of posts
    path('posts/<int:pk>/', PostDetailView.as_view(), name="blog_detail"),  # Render post detail
    
    # DRF API routes
    path('api/', include(router.urls)),
]
