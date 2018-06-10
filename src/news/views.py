from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from src.utils import paginators
from . models import News
from . forms import AddNewsForm, EditNewsForm


def index(request):
    all_news = News.objects.all().order_by('-date_add')
    return render(request, 'news/index.html', {'news': paginators(request, all_news, 20)})


def news(request, news_pk):
    new = get_object_or_404(News, pk=news_pk)
    road = [
        {'link': '/', 'title': u'Главная'},
        {'link': '/news/', 'title': u'Новости'}
    ]
    return render(request, 'news/news.html', {'news': new, 'road': road})


@login_required()
def add_news(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST)
        if form.is_valid():
            neww = form.save()
            neww.author = request.user
            neww.save()
            messages.success(request, 'Новость успешно добавлена.')
            return redirect('news:news', neww.pk)
        messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = AddNewsForm()
    return render(request, 'news/add_news.html', {'form':form})


@login_required
def edit_news(request, news_pk):
    news = get_object_or_404(News, pk=news_pk)
    if request.user != news.author:
        raise Http404
    if request.method == 'POST':
        form = EditNewsForm(request.POST, instance=news)
        if form.is_valid():
            art = form.save()
            messages.success(request, 'Новость успешно изменена.')
            return redirect('news:news', news.pk)
        messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = EditNewsForm(instance=news)
    return render(request, 'news/edit_news.html', {'form':form})
