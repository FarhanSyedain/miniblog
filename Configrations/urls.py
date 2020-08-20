from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from Home import views as Home
from OtherPages import views as Others
from Blog.settings import DEBUG


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.home,name='home_page'),
    path('blog',Others.blog_detail,name='blog_detail'),
    path('api/category/<str:category>',Others.CateogoryAPIView.as_view(),name='category'),
    path('api/home/',Home.HomePageAPIView.as_view()),
    path('search/api',Others.SearchPageAPIView.as_view()),
    path('search/',Others.search_page,name='search'),
    path('category/<str:category>',Others.category,name='category'),
    path('upload_post/',Others.upload_post,name='upload_post'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]



if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
