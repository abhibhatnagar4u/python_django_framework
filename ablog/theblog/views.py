from django.shortcuts import render, reverse
from .models import Post
from .models import Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostForm
from .forms import EditForm
from django.core.cache import cache

# cache.clear()
# cache.delete_pattern(Post)

# Create your views here.
# def home(request):
# 	all_posts = Post.objects.all
# 	return	render(request, 'home.html', {'all_posts':all_posts})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-id']


class ArticleDetailsView(DetailView):
	model = Post
	template_name = 'article_details.html'	


class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'	
	# fields = '__all__'	
	#fields = ('title', 'body')


class UpdatePostView(UpdateView):
	
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'	
	

class AddCommentView(CreateView):
	model = Comment
	# form_class = CommentForm
	template_name = 'add_comment.html'	
	fields = ['name','body']
	# fields = '__all__'	
	