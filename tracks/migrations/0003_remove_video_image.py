# Generated by Django 3.2.14 on 2023-04-13 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_auto_20230407_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='image',
        ),
    ]