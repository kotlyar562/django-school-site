from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('src.main.urls', 'main')),
    path('admin/', admin.site.urls),
    path('redactor/', include('redactor.urls')),
    path('accounts/', include('src.accounts.urls', namespace='accounts')),
    path('articles/', include('src.blog.urls', namespace='blog')),
    path('news/', include('src.news.urls', namespace='news')),
    path('pages/', include('src.pages.urls', namespace='pages')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
