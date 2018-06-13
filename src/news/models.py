from django.db import models
from django.utils import timezone
from django.urls import reverse

from redactor.fields import RedactorField

from src.accounts.models import User


class ImportantNewsManager(models.Manager):
    """Класс менеджер для вывода важных новостей"""
    def get_query_set(self):
        return super(ImportantNewsManager, self).get_query_set().filter(important=True)


class OtherNewsManager(models.Manager):
    def get_query_set(self):
        return super(OtherNewsManager, self).get_query_set().filter(important=False)


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    date_add = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    content = RedactorField(verbose_name='Текст')
    important = models.BooleanField(verbose_name='Важная новость', default=False)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL,
                               blank=True, null=True)

    objects = models.Manager()
    importants = ImportantNewsManager()
    others = OtherNewsManager()

    class Meta:
        ordering = ['-date_add']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:news', args=[self.pk])
