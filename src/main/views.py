from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render

from src.news.models import News
from src.blog.models import Article
from src.pages.models import Page
from . forms import FeedbackForm, FeedbackErrorForm


def index(request):
    last_news = News.objects.all().order_by('-date_add')[:4]
    last_articles = Article.objects.all().order_by('-date_add')[:12]
    home_text = Page.objects.get(slug=u'home')
    return render(request, 'main/index.html', locals())


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.send(request)
            messages.success(request, 'Спасибо, Ваше письмо отправлено')
            return HttpResponseRedirect('/')
    else:
        form = FeedbackForm()
    return render(request, 'main/feedback.html', {'form': form})


def feedbackerror(request):
    if request.method == 'POST':
        form = FeedbackErrorForm(request.POST)
        if form.is_valid():
            form.send(request)
            messages.success(request, 'Сообщение отправлено')
            return HttpResponseRedirect('/')
    else:
        form = FeedbackErrorForm(initial={'referer': request.META.get('HTTP_REFERER', '')})
    return render(request, 'main/feedbackerror.html', {'form': form})


def search(request):
    return render(request, 'main/search.html')
