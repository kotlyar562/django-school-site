from django.utils import timezone
from django.db import models
from django.urls import reverse
from redactor.fields import RedactorField

from src.accounts.models import User


class Article(models.Model):
    title = models.CharField(verbose_name='Название', max_length=250)
    date_add = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    content = RedactorField(verbose_name='Текст')
    author = models.ForeignKey(User, verbose_name='Автор',
                               on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-date_add',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article', args=[self.pk])
