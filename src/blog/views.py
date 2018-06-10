import datetime
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from src.utils import paginators
from . models import Article
from . forms import AddArticleForm, EditArticleForm


def index(request):
    articles = Article.objects.all().order_by('-date_add')
    return render(request, 'blog/index.html',
                  {'articles': paginators(request, articles, count=20)})


def article(request, article_pk):
    art = get_object_or_404(Article, pk=article_pk)
    road = [
        {'link': '/', 'title': 'Главная'},
        {'link': '/articles/', 'title': 'Статьи'}
    ]
    return render(request, 'blog/article.html', {'article': art, 'road': road})


@login_required()
def add_article(request):
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            art = form.save()
            art.date_add = datetime.datetime.now()
            art.author = request.user
            art.save()
            messages.success(request, 'Статья успешно добавлена.')
            return redirect('blog:article', art.pk)
        messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = AddArticleForm()
    return render(request, 'blog/add_article.html', {'form':form})


@login_required()
def edit_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user != article.author:
        raise Http404
    if request.method == 'POST':
        form = EditArticleForm(request.POST, instance=article)
        if form.is_valid():
            art = form.save()
            messages.success(request, 'Статья успешно изменена.')
            return redirect('blog:article', art.pk)
        messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = EditArticleForm(instance=article)
    return render(request, 'blog/edit_article.html', {'form':form})
