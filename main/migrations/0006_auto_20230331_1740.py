# Generated by Django 3.2.14 on 2023-03-31 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_galery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galery',
            old_name='photo_1',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='galery',
            name='photo_2',
        ),
        migrations.RemoveField(
            model_name='galery',
            name='photo_3',
        ),
        migrations.RemoveField(
            model_name='galery',
            name='photo_4',
        ),
        migrations.RemoveField(
            model_name='galery',
            name='photo_5',
        ),
    ]