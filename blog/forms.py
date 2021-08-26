from .models import Comment, Post, category
from django import forms


choices =  category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
	choice_list.append(item)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class PostForm(forms.ModelForm):
    category = forms.ChoiceField(choices = choice_list)
    class Meta:
        model = Post
        fields = ('title', 'category','author', 'content', 'image','status')

class EditForm(forms.ModelForm):
    category = forms.ChoiceField(choices = choice_list)
    class Meta:
        model = Post
        fields = ('title', 'category', 'content', 'image','status')
