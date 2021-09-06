from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField
from django.urls import reverse
from django.template.defaultfilters import slugify

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
 
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = SummernoteTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images',null=True, blank=True)
    category = models.ForeignKey('blog.category', on_delete=models.SET_NULL, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='blog_Post')

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created_on'] # this is used to order blog posts using time

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        
        return reverse('home')



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)


class category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    
