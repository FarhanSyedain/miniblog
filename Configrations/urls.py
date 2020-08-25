from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from Home import views as Home
from OtherPages import views as Others
from Blog.settings import DEBUG


urlpatterns = [
    path('staff/admin/panel', admin.site.urls, name='admin_page'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    path('',Home.home,name='home_page'),
    path('view_blog/<slug:blog>',Others.blog_detail,name='blog_detail'),
    path('search/',Others.search_page,name='search'),
    path('category/<str:category>',Others.category,name='category_page'),
    path('upload_post/',Others.upload_post,name='upload_post'),
    path('tag/<str:tag>/',Others.tag,name='tageed_posts'),
    path('contact',Others.contact,name='contact_page'),
    path('edit_blog/<slug:slug>/',Others.edit_blog,name='edit_blog'),
    path('about/',Others.about_page,name='about_page'),
    
    path('api/home/',Home.HomePageAPIView.as_view(),name='home_api'),
    path('api/category/<str:category>',Others.CateogoryAPIView.as_view(),name='api_category'),
    path('api/tag/<str:tag>/',Others.TagPageApi.as_view(),name='tag_api'),
    path('search/api',Others.SearchPageAPIView.as_view(),name='search_api'),
 
]


if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
