from django.shortcuts import render, get_object_or_404
from .models import Post, category
from .forms import CommentForm, PostForm, EditForm
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )


def aboutus(request):
    return render(request,'about-us.html')

def contactus(request):
    return render(request,'contact-us.html')


class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-', ' '))
	return render(request, 'categories.html', {'cats':cats.replace('-', ' ').title(), 'category_posts':category_posts})