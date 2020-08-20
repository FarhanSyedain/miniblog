from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Staff(models.Model):
    username = models.CharField(max_length=50,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile_picture = models.ImageField(blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.IntegerField(blank=True,null=True)
    name =  models.CharField(max_length=50,null=True,blank=True)
    

    def __str__(self):
        return self.get_name
    
    
    @property
    def get_name(self):
        if self.name is not None:
            if len(self.name) > 0:
                return str(self.name)
        return self.username
    
    
class Tag(models.Model):
    tag = models.CharField(max_length=30)


    def __str__(self):
        return self.tag
    

class Post(models.Model):
    author = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True)
    slug = models.SlugField(blank=True,null=True)
    body = RichTextUploadingField()#Replae with rich text field
    thumbnail = models.ImageField(upload_to='posts')
    key_words = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag,blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    trending = models.BooleanField(default=False) # The first three posts on home screen
    title = models.CharField(max_length=50)
    visitors = models.IntegerField(default=0)
    top_post = models.BooleanField(default=False) #Appear Near bottom
    catogory = models.CharField(max_length=40,null=True)
    sub_title = models.CharField(max_length=100,null=True)
    active = models.BooleanField(default=False) #If true, then dont show the post
    
    def save(self):
    
        self.key_words = self.title + " " + self.sub_title + ' '  + self.key_words 
    
        slug = slugify(str(self.title)) if self.slug is None else slugify(self.slug) #Replace With sluggify later
        
        if self.posted is None: #That means we are creating this model and not updating it ; Since posted will be added only after calling super().save()
            slug_exists = Post.objects.filter(slug=slug).exists() #Returns either True or False

            count = 0
            while slug_exists:
                slug = slug[:-len(str(count))] #If we have added a number and slug still exists, remove the previous number and add the new one
                #If number is not removed , it will add the new number -- which is incremented by 1 every itr-- at the add rather that adding that to previous number
                slug = slugify(slug + '-' + str(count))
                count += 1
                slug_exists = Post.objects.filter(slug=slug).exists() 
        
        self.slug = slug    
        
        super().save()
        
        
    def __str__(self):
        return str(self.title + ' by ' + self.author.get_name)
        

#All The models that we want to register in admin page.so we can edit them their
to_be_added_in_admin_page = [Post,Staff,Tag]