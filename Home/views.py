from django.shortcuts import render

from Configrations.models import *
from Configrations.serializers import PostSerilizer
from Configrations.utilts import CustomPagination

from rest_framework.generics import ListAPIView


def home(request):
    trending_posts = Post.objects.filter(trending=True,active=False)[:3]
    popular_posts = Post.objects.filter(top_post=True,active=False)[:6]
    content = {'trending': trending_posts, 'popular_posts': popular_posts, 'page': 'home'}
    
    return render(request, 'index.html', content)


class HomePageAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerilizer
    pagination_class = CustomPagination
