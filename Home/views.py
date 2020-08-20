from django.shortcuts import render,get_object_or_404

from Configrations.models import *
from Configrations.serializers import PostSerilizer
from Configrations.utilts import CustomPagination

from rest_framework import pagination
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


def home(request):
    trending_posts = Post.objects.filter(trending=True,active=False)[:3]
    popular_posts = Post.objects.filter(top_post=True,active=False)[:6]
    content = {'trending':trending_posts,'popular_posts':popular_posts,'page':'home'}
    
    return render(request,'index.html',content)


class HomePageAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerilizer
    permission_classes = [IsAuthenticated,]
    pagination_class = CustomPagination

    