# Generated by Django 2.0.6 on 2018-06-10 21:22

from django.db import migrations, models
import django.utils.timezone
import redactor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('klass', models.CharField(blank=True, help_text='Не обязательно, например, 10-11 классы или 6-А класс.', max_length=100, verbose_name='Классы')),
                ('date_begin', models.DateField(default=django.utils.timezone.now, verbose_name='Дата начала')),
                ('date_end', models.DateField(blank=True, help_text='Не обязательно, для событий длительностью больше 1 дня', null=True, verbose_name='Дата окончания')),
                ('content', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Текст')),
                ('etype', models.IntegerField(choices=[(0, 'Праздник (Единый урок, концерт и т.п.)'), (1, 'Особое учебное событие (олимпиада, ВПР и т.п.)'), (3, 'Выходной день (плановые и внеплановые выходные дни, в т.ч. каникулы)'), (5, 'Другое')], default=5, verbose_name='Тип события')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]