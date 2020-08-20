from django.forms import ModelForm
from .models import Post

class PostCreationForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','sub_title','thumbnail','body' ,'key_words','tags','catogory','slug','active']