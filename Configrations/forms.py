from django.forms import ModelForm
from .models import Post

class PostCreationForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','sub_title','thumbnail','body','key_words','tags','catogory','slug','active']
    
    def save(self,author, commit=True):
        self.instance.catogory = self.instance.catogory.lower().capitalize()
        self.instance.author = author
        return super().save(commit=commit)
