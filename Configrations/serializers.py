from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import *


class PostSerilizer(ModelSerializer):
    author = SerializerMethodField('get_username')
    tags = SerializerMethodField('get_tags')

    class Meta:
        model = Post
        fields = '__all__'


    def get_username(self, blog):
        return blog.author.username


    def get_tags(self, blog):
        to_be_returned = []
        for tag in blog.tags.all():
            to_be_returned.append(tag.tag)
        return to_be_returned


