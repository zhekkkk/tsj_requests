# Generated by Django 4.2.1 on 2023-11-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsj', '0011_requesttype_slug_alter_request_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requesttype',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]