# Generated by Django 4.2.1 on 2023-11-16 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tsj', '0008_alter_worktype_request_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['pk'], 'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
        migrations.AlterModelOptions(
            name='apartment',
            options={'ordering': ['pk'], 'verbose_name': 'Квартира', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'ordering': ['pk'], 'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
        migrations.AlterModelOptions(
            name='workposition',
            options={'ordering': ['pk'], 'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AlterModelOptions(
            name='worktype',
            options={'ordering': ['pk'], 'verbose_name': 'Тип работы', 'verbose_name_plural': 'Типы работ'},
        ),
        migrations.AddField(
            model_name='request',
            name='apartment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tsj.apartment', verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='request',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tsj.address', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='request',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания'),
        ),
        migrations.AlterField(
            model_name='request',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tsj.requesttype', verbose_name='Тип заявки'),
        ),
        migrations.AlterField(
            model_name='request',
            name='resident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tsj.resident', verbose_name='Житель'),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tsj.status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='request',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления'),
        ),
        migrations.AlterField(
            model_name='request',
            name='work_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tsj.worktype', verbose_name='Тип услуги'),
        ),
        migrations.AlterField(
            model_name='request',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tsj.worker', verbose_name='Работник'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефона'),
        ),
    ]