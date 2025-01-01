from django.urls import reverse_lazy
from .filters import PostFilter
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

class PostList(ListView):
    model = Post
    ordering = '-created_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 1

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostListSearch(ListView):
    model = Post
    ordering = '-created_time'
    template_name = 'posts_search.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
    
class CreatePost(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/posts/news/create/':
            post.post_type = 'N'
        if self.request.path == '/posts/articles/create/':
            post.post_type = 'A'
        post.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.path == '/posts/news/create/':
            context['post_type'] = 'news'
        if self.request.path == '/posts/articles/create/':
            context['post_type'] = 'article'
        return context

class UpdatePost(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
