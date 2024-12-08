from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogging.models import Post, Category
from rest_framework.viewsets import ModelViewSet
from blogging.serializers import PostSerializer, CategorySerializer


# html views
class PostListView(ListView):
    model = Post
    template_name = 'blogging/list.html'

    def get_queryset(self):
        # Return only published posts, ordered by the most recent publish date
        return Post.objects.exclude(published_date__exact=None).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    def get_queryset(self):
        # Ensure only published posts can be viewed in detail
        return Post.objects.exclude(published_date__exact=None)

# API views
class PostViewSet(ModelViewSet):
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    serializer_class = PostSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer