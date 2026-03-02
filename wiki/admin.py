from django.contrib import admin
from .models import Category, Post, Tag, Comments, Rating
admin.site.register(Post)
admin.site.register(Category)

admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Rating)

# Register your models here.
