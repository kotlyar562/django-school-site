from django.db import models
from django.utils import timezone
from redactor.fields import RedactorField

CHOICE_TYPES = (
    (0, 'Праздник (Единый урок, концерт и т.п.)'),
    (1, 'Особое учебное событие (олимпиада, ВПР и т.п.)'),
    (2, 'Выходной день (плановые и внеплановые выходные дни, в т.ч. каникулы)'),
    (5, 'Другое'),
)

class Event(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    klass = models.CharField(verbose_name=u'Классы', max_length=100, blank=True,
                             help_text='Не обязательно, например, 10-11 классы или 6-А класс.')
    date_begin = models.DateField(verbose_name='Дата начала', default=timezone.now)
    date_end = models.DateField(verbose_name='Дата окончания', blank=True, null=True,
                                help_text='Не обязательно, для событий длительностью больше 1 дня')
    content = RedactorField(verbose_name='Текст', blank=True, null=True,
                            help_text='Подробности мероприятия, расписание и т.п.')
    etype = models.IntegerField(verbose_name='Тип события', choices=CHOICE_TYPES,
                                default=5)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ('date_begin',)

    def __str__(self):
        return self.title
