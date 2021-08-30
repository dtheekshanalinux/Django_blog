from .models import Comment, Post, category
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=category.objects.all().order_by('name'))
    class Meta:
        model = Post
        fields = ('title', 'category','author', 'content', 'image','status')

class EditForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=category.objects.all().order_by('name'))
    class Meta:
        model = Post
        fields = ('title', 'category', 'content', 'image','status')
