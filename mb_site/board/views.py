def post_detail(request, pk):
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Post
from .forms import PostForm


def home(request):
    recent = Post.objects.order_by('-created')[:5]
    return render(request, 'board/home.html', {'posts': recent})


def about(request):
    return render(request, 'board/about.html')


def posts(request):
    # Anyone can view posts; only authenticated users can create
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created.')
            return redirect('posts')
    else:
        form = PostForm()
    all_posts = Post.objects.order_by('-created')
    return render(request, 'board/posts.html', {'form': form, 'posts': all_posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'board/post_detail.html', {'post': post})


def _is_staff(user):
    return user.is_active and user.is_staff


@user_passes_test(_is_staff)
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated.')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'board/post_edit.html', {'form': form, 'post': post})


@user_passes_test(_is_staff)
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted.')
        return redirect('posts')
    return render(request, 'board/post_confirm_delete.html', {'post': post})
