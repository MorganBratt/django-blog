from django.urls import path, include
from polling.views import PollListView, PollDetailView,PollViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'polls', PollViewSet)


urlpatterns = [
    path("", PollListView.as_view(), name="poll_index"),
    path("polls/<int:pk>/", PollDetailView.as_view(), name="poll_detail"),


    # DRF API routes
    path('api/', include(router.urls)),
]

