from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from blog.forms import PostForm

# Create your views here.

def posts(request):
    posts = Post.objects.all().order_by('-created')
    print(posts)
    context = {'posts': posts}
    return render (request,'blog/posts.html', context)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = 'request.user'
            post.save()
            return redirect('post_detail', pk=post.pk)
    form = PostForm()
    publish = True
    context = {'form': form, 'publish': publish}
    return render(request,'blog/post_add.html', context)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = 'request.user'
            post.save()
            return redirect('post_detail', pk=post.pk)
    form = PostForm(instance=post)
    publish = True
    context = {'form': form, 'publish': publish}
    return render(request,'blog/post_add.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post':post}
    return render(request, 'blog/post_detail.html', context)