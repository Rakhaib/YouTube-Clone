# Generated by Django 4.2.7 on 2023-12-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Youtube', '0008_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.CharField(max_length=250),
        ),
    ]
