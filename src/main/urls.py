from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from . import views
from . sitemap import AccountsSitemap, PageSitemap, NewsSitemap, ArticleSitemap, StaticSitemap

sitemaps = {'accounts': AccountsSitemap, 'pages': PageSitemap, 'news': NewsSitemap,
            'articles': ArticleSitemap, 'stat': StaticSitemap}

app_name = 'main'
urlpatterns = (
    path('', views.index, name='index'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedbackerror/', views.feedbackerror, name='feedbackerror'),
    path('search/', views.search, name='search'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
)
