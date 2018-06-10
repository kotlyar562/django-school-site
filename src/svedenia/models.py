from django.db import models
from redactor.fields import RedactorField


class Group(models.Model):
    title = models.CharField('Название раздела', max_length=250)
    slug = models.SlugField(verbose_name='Ссылка', unique=True)
    number = models.IntegerField('Номер раздела', default=0,
                                 help_text='Порядок отображения в меню')

    class Meta:
        verbose_name = 'Раздел сведений об ОР'
        verbose_name_plural = 'Разделы сведений об ОР'
        ordering = ('number',)

    def __str__(self):
        return self.title


class Svedenie(models.Model):
    group = models.ForeignKey(Group, verbose_name=u'Раздел', on_delete=models.SET_NULL,
                              null=True)
    title = models.CharField('Название', max_length=250)
    text = RedactorField('Текст')
    number = models.IntegerField('Номер', default=0,
                                 help_text=u'Порядок отображения внутри раздела')

    class Meta:
        verbose_name = 'Информация об ОР'
        verbose_name_plural = 'Информация об ОР'
        ordering = ('number',)

    def __str__(self):
        return self.title
