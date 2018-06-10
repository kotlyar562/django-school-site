from django.db import models
from redactor.fields import RedactorField
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(verbose_name='Название страницы', max_length=250)
    slug = models.SlugField(verbose_name='Ссылка на страницу', unique=True)
    content = RedactorField(verbose_name='Содержимое страницы')
    group = models.CharField(verbose_name='Группа', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Статическая страница'
        verbose_name_plural = 'Статические страницы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pages:page', args=[self.pk])
