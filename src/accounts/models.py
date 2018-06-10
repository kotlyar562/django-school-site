from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from redactor.fields import RedactorField


RANKS = (
    (0, '-'),
    (1, 'Первая'),
    (2, 'Высшая'),
)


class User(AbstractUser):
    photo = models.ImageField(verbose_name=u'Фото', upload_to='uploads/TeacherPhoto/',
                              blank=True, null=True)
    post = models.CharField(verbose_name='Должность', max_length=200, blank=True)
    stag = models.CharField(verbose_name='Стаж', help_text='Например, 1 год, 10 лет, ...',
                            max_length=200, blank=True)
    rank = models.IntegerField('Категория', choices=RANKS, default=0)
    phone = models.CharField(verbose_name='Номер телефона', blank=True, max_length=20)
    statement = RedactorField('Дополнительная информация', blank=True)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
        ordering = ('last_name',)

    def __str__(self):
        return self.get_name()

    def get_absolute_url(self):
        return reverse('accounts:profile', args=[self.pk])

    def get_full_name(self):
        return self.last_name + ' ' + self.first_name

    def get_name(self):
        if self.first_name or self.last_name:
            return self.get_full_name()
        else:
            return self.username
