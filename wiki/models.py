from django.db import models
import json
class Category(models.Model):
    name = models.CharField(max_length = 250, verbose_name='category_name')
    slug = models.SlugField(max_length=250, unique=True)
    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name = models.CharField(max_length = 250, verbose_name='category_name')
    slug = models.SlugField(max_length=250, unique=True)
    def __str__(self):
        return str(self.name) 

class Post(models.Model):
    image = models.ImageField(upload_to = "rasmlar/", blank = True, null = True)
    title = models.CharField(verbose_name="Post title", max_length=600)
    body = models.TextField(verbose_name ='Post body')
    puplished_date = models.DateTimeField(auto_now = True, verbose_name='Publish date')
    author = models.CharField(verbose_name='Post author', default='Admin', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tag = models.ManyToManyField(Tag)
    views = models.PositiveIntegerField(default = 0)
    published = models.BooleanField(default = True)
    on_top = models.BooleanField(default = True)
    
    class Meta:
        ordering = ['-puplished_date']

    def __str__(self):
        return str(self.title)

class Kategoriya(models.Model):
    pass

class Comments(models.Model):
    author = models.CharField(verbose_name='Comment author',blank = False, default='Admin', max_length=100)
    comment = models.TextField(verbose_name='Comment')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    puplished_date = models.DateTimeField(auto_now = True, verbose_name='Publish date')
    def __str__(self):
        return str(self.author)

class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name="ratings")
    value = models.PositiveSmallIntegerField(default=0, verbose_name="Post rating")
    def __str__(self):
        return str(self.value)