from django.urls import path
from . import  views 
from django.conf.urls.static import static
from django.conf import settings

app_name = "wiki"
urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('more/<pk>', views.more, name = 'more'),
    path('tags/<articles>',views.tagss, name = "articles"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)