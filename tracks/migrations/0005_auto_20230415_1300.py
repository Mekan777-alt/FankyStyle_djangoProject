# Generated by Django 3.2.14 on 2023-04-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0004_auto_20230415_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description_1',
            field=models.CharField(default='name', max_length=256),
        ),
        migrations.AddField(
            model_name='video',
            name='description_2',
            field=models.CharField(default='name', max_length=256),
        ),
        migrations.AddField(
            model_name='video',
            name='description_3',
            field=models.CharField(default='name', max_length=256),
        ),
        migrations.AddField(
            model_name='video',
            name='name_1',
            field=models.CharField(default='name', max_length=256),
        ),
        migrations.AddField(
            model_name='video',
            name='name_2',
            field=models.CharField(default='name', max_length=256),
        ),
        migrations.AddField(
            model_name='video',
            name='name_3',
            field=models.CharField(default='name', max_length=256),
        ),
        migrations.AddField(
            model_name='video',
            name='video_1',
            field=models.FileField(blank=True, null=True, upload_to='video'),
        ),
        migrations.AddField(
            model_name='video',
            name='video_2',
            field=models.FileField(blank=True, null=True, upload_to='video'),
        ),
        migrations.AddField(
            model_name='video',
            name='video_3',
            field=models.FileField(blank=True, null=True, upload_to='video'),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(default='name', max_length=256),
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(default='name', max_length=256),
        ),
    ]