from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from src.blog.models import Article
from src.news.models import News
from src.accounts.models import User
from src.pages.models import Page


class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Article.objects.all()


class NewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return News.objects.all()


class AccountsSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.5

    def items(self):
        return User.objects.all()


class PageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Page.objects.all()


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['main:index']

    def location(self, object):
        return reverse(object)
