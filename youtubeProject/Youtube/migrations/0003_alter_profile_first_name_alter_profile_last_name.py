# Generated by Django 4.2.7 on 2023-12-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Youtube', '0002_video_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
