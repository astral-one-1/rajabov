from django.shortcuts import render, HttpResponse
from .models import Category, Post, Tag, Comments


# Create your views here.
def home_page(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    comments = Comments.objects.all()
    data = {
        "posts":posts,
        "categories":categories,
        "comments":comments
    }
    return render(request, 'index.html', context=data)

def more(request, pk):
    post = Post.objects.get(id=pk)
    categories = Category.objects.all()
    post.views+=1
    post.save()

    if request.method == "POST":
        name = request.POST.get("name")
        comment = request.POST.get('comment')
        if all([name, comment]):
            Comments.objects.create(
                author = name,
                post = post,
                comment = comment
            )

    return render(request, 'home2.html',{'post':post, "categories":categories})
    
def tagss(request, articles):
    category = Category.objects.all()
    post = Post.objects.all()
    r = Post.objects.get(id = articles)
    return render(request, 'tags.html', {"r":r})