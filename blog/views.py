from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.forms import PostForm

# Create your views here.

def posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            post = Post(title=title, body=body)
            post.save()
    form = PostForm()
    posts = Post.objects.all().order_by('-created')
    context = {'posts': posts, 'form': form}
    return render (request,'blog/posts.html', context)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    form = PostForm()
    context = {'form': form}
    return render (request,'blog/post_add.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post':post}
    return render(request, 'blog/post_detail.html',context)