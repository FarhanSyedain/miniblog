from django.shortcuts import render,get_object_or_404

from Configrations.models import *
from Configrations.serializers import PostSerilizer
from Configrations.utilts import CustomPagination 
from Configrations.forms import PostCreationForm

from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


#For the catogory page 
class CateogoryAPIView(ListAPIView):
    serializer_class = PostSerilizer
    permission_classes = [IsAuthenticated,]
    pagination_class = CustomPagination


    def get_queryset(self):
        if self.kwargs['category'].capitalize() == 'All':
            return Post.objects.all().order_by('-posted')
        return  Post.objects.filter(catogory=self.kwargs['category'].capitalize()).order_by('-posted')
        

class SearchPageAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerilizer
    permission_classes = [IsAuthenticated,]
    pagination_class = CustomPagination
    filter_backends = [OrderingFilter,SearchFilter]
    ordering_fields = ['posted','visitors']
    search_fields = ['author__username','key_words','sub_title']

    
def search_page(request):
    search_and_filter = request.META['QUERY_STRING']
    search_query = request.GET.get('search')

    return render(request,'category.html',{'search_and_filter':search_and_filter,'page':'search','search_query':search_query})


def category(request,category):
    
    get_object_or_404(Post,catogory=category.capitalize())
    
    return render(request,'category.html',{'search_and_filter':None,'page':'category','search_query':None,'cateogry':category})
    

def blog_detail(request):
    return render(request,'single-standard.html')


def upload_post(request):
    
    form = PostCreationForm()
    
    return render(request,'upload.html',{'form':form})