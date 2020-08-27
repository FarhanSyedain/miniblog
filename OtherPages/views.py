from django.shortcuts import render,redirect,Http404,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from Configrations.models import *
from Configrations.serializers import PostSerilizer
from Configrations.utilts import CustomPagination 
from Configrations.forms import PostCreationForm

from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView


#For the catogory page 
class CateogoryAPIView(ListAPIView):
    serializer_class = PostSerilizer
    pagination_class = CustomPagination


    def get_queryset(self):
        return Post.objects.filter(catogory=self.kwargs['category'].capitalize()).order_by('-posted')
        

class SearchPageAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerilizer
    pagination_class = CustomPagination
    filter_backends = [OrderingFilter,SearchFilter]
    ordering_fields = ['posted','visitors']
    search_fields = ['author__username','key_words','sub_title']


class TagPageApi(ListAPIView):
    serializer_class = PostSerilizer
    pagination_class = CustomPagination
    
    
    def get_queryset(self):
        return Post.objects.filter(tags__tag=self.kwargs.get('tag').capitalize())
    
    
def search_page(request):
    search_and_filter = request.META['QUERY_STRING']#get the attributes ,after ? in the url, as a string rather than dict
    search_query = request.GET.get('search')
    popular_posts = Post.objects.filter(top_post=True,active=False)[:6]
    
    return render(request,'category.html',{'popular_posts':popular_posts,'search_and_filter':search_and_filter,'page':'search','search_query':search_query})


def category(request,category):
    popular_posts = Post.objects.filter(top_post=True,active=False)[:6]#Specify either 4 or 6 and set top_post of atleast 4 posts True
    if Post.objects.all().filter(catogory=category.capitalize()).exists():    
        return render(request,'category.html',{'popular_posts':popular_posts,'search_and_filter':None,'page':'category','search_query':None,'cateogry':category})
    
    raise Http404('404 Query does not exist')


def blog_detail(request,blog):
    if Staff.objects.filter(user=request.user).exists:
        post = get_object_or_404(Post,slug=blog)
        if (post.active and str(post.author) == str(request.user.staff)) or not post.active:
            pass
        else:
            raise Http404('No Posts Found')
    else:
        post = get_object_or_404(Post,slug=blog,active=False)
        
    popular_posts = Post.objects.filter(top_post=True,active=False)[:6]
    if request.user.is_authenticated and Staff.objects.filter(user=request.user).exists():
        owner = post.author == request.user.staff
    
    post.visitors = post.visitors + 1 #Post got one more view
    
    return render(request,'single-standard.html',{'popular_posts':popular_posts,'post':post,'owner':owner})


@login_required(login_url='../staff/admin/panel')
def upload_post(request):
    
    try:
        assert Staff.objects.filter(user=request.user).exists()
    except AssertionError:
        return redirect('home_page')
    
    form = PostCreationForm()
    
    if request.method == 'POST':
        form = PostCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(author=request.user.staff)
            return redirect('home_page')
        
    return render(request,'upload.html',{'form':form,'edit':False})


def tag(request,tag):
    popular_posts = Post.objects.filter(top_post=True,active=False)[:6]
    return render(request,'category.html',{'popular_posts':popular_posts,'search_and_filter':None,'page':'tag','search_query':None,'cateogry':category,'tag':tag})
    

def contact(request):
    
    if request.method == 'POST':
        body = request.POST.get('body')
        body = request.POST.get('name') + f'says "{body}"'
        heading = request.POST.get('heading')
        try:
            send_mail(
                heading,
                body,
                settings.EMAIL_HOST_USER,
                ['the email you want to send msg to'],
                fail_silently=False,
            )
            msg = messages.success(request,'We Have Recived The Email...Thanks For Your Feed Back')
        except:
            msg = messages.error(request,'An Error Occured while sending massage')
        
    popular_posts = Post.objects.filter(top_post=True,active=False)[:6]
    return render(request,'page-contact.html',{'popular_posts':popular_posts})


@login_required(login_url='../staff/admin/panel')
def edit_blog(request,slug):
    
    if request.user.is_authenticated and Staff.objects.filter(user=request.user).exists():
        post = get_object_or_404(Post,slug=slug)
        form = PostCreationForm(instance=post)
        
        if request.method == 'POST':
            if request.POST.get('delete') == 'True':
                post.delete()
                return redirect('home_page')

            form = PostCreationForm(request.POST,request.FILES,instance=post)
            if form.is_valid():
                form.save(author=request.user.staff)
                msg = messages.success(request,'Post Successfully Updated')
        
        return render(request,'upload.html',{'form':form,'edit':True})
    

def about_page(request):
    popular_posts = Post.objects.filter(top_post=True,active=False)[:6]
    return render(request,'page-about.html',{'popular_posts':popular_posts})