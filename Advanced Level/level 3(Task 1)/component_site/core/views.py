from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib import messages

def login_view(request):
 if request.method=='POST':
  user=authenticate(username=request.POST['username'],password=request.POST['password'])
  if user:
   login(request,user)
   next_url = request.POST.get('next') or request.GET.get('next') or 'home'
   return redirect(next_url)
  else:
   messages.error(request, 'Invalid username or password.')
 return render(request,'login.html')

def register(request):
 if request.method=='POST':
  username = request.POST['username']
  password = request.POST['password']
  if User.objects.filter(username=username).exists():
   messages.error(request, 'Username already exists.')
   return render(request,'register.html')
  User.objects.create_user(username=username, password=password)
  messages.success(request, 'Account created successfully. Please log in.')
  return redirect('login')
 return render(request,'register.html')

def logout_view(request):
 logout(request)
 return redirect('login')

@login_required
def home(request):
 posts = Post.objects.all().order_by('-created_at')
 return render(request,'home.html', {'posts': posts})

@login_required
def create_post(request):
 if request.method == 'POST':
  title = request.POST['title']
  content = request.POST['content']
  post = Post.objects.create(title=title, content=content, author=request.user)
  # Handle image uploads
  images = request.FILES.getlist('images')
  # assign up to 5 images to image1..image5
  for idx, img in enumerate(images[:5], start=1):
   setattr(post, f'image{idx}', img)
  post.save()
  messages.success(request, 'Post created successfully!')
  return redirect('home')
 return render(request, 'create_post.html')

@login_required
def post_detail(request, pk):
 post = get_object_or_404(Post, pk=pk)
 return render(request, 'post_detail.html', {'post': post})

@login_required
def edit_post(request, pk):
 post = get_object_or_404(Post, pk=pk)
 if post.author != request.user:
  messages.error(request, 'You can only edit your own posts.')
  return redirect('home')

 if request.method == 'POST':
  post.title = request.POST['title']
  post.content = request.POST['content']
  # Handle image uploads (replace or keep existing)
  images = request.FILES.getlist('images')
  for idx, img in enumerate(images[:5], start=1):
   setattr(post, f'image{idx}', img)
  post.save()
  messages.success(request, 'Post updated successfully!')
  return redirect('home')

 return render(request, 'edit_post.html', {'post': post})
