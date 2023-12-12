# Generated by Django 4.2.1 on 2023-11-14 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tsj', '0006_remove_resident_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='tsjrequest',
            name='address',
        ),
        migrations.RemoveField(
            model_name='tsjrequest',
            name='resident',
        ),
        migrations.RemoveField(
            model_name='tsjrequest',
            name='status',
        ),
        migrations.RemoveField(
            model_name='tsjrequest',
            name='work_type',
        ),
        migrations.RemoveField(
            model_name='tsjrequest',
            name='worker',
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
        migrations.AlterModelOptions(
            name='apartment',
            options={'verbose_name': 'Квартира', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
        migrations.AlterModelOptions(
            name='workposition',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AlterModelOptions(
            name='worktype',
            options={'verbose_name': 'Тип работы', 'verbose_name_plural': 'Типы работ'},
        ),
        migrations.AlterField(
            model_name='worker',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='phone_number',
            field=models.CharField(max_length=255, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='work_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tsj.workposition', verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='worktype',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='worktype',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='worktype',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='worktype',
            name='work_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tsj.workposition', verbose_name='Должность'),
        ),
        migrations.DeleteModel(
            name='ResidentRequest',
        ),
        migrations.DeleteModel(
            name='TsjRequest',
        ),
        migrations.AddField(
            model_name='request',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tsj.address'),
        ),
        migrations.AddField(
            model_name='request',
            name='request_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tsj.requesttype'),
        ),
        migrations.AddField(
            model_name='request',
            name='resident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tsj.resident'),
        ),
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='tsj.status'),
        ),
        migrations.AddField(
            model_name='request',
            name='work_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tsj.worktype'),
        ),
        migrations.AddField(
            model_name='request',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tsj.worker'),
        ),
        migrations.AddField(
            model_name='worktype',
            name='request_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tsj.requesttype', verbose_name='Тип заявки'),
        ),
    ]
