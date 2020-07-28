from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    context={
    'posts': Post.objects.all()
    }
    return render(request,'blog/blog-home.html',context)
def go(request):
    return render(request,'blog/go.html', {'title':'GoGo!'})
