from django.shortcuts import render, redirect
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.

def login(request):
    return render(request, 'navigations/login.html')

@login_required
def postcontroller(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES   )

        if form.is_valid():
            form.save()

            return redirect('postcontroller')

    else:
        form = PostForm()

    return render(request, 'navigations/postcontroller.html', {'form':form})

def posts(request):
    """List existing posts."""
    posts = Post.objects.all().order_by('-created')
    return render(request, 'navigations/posts.html', {'posts': posts})