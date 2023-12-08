# Generated by Django 4.2.7 on 2023-12-07 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Youtube', '0012_comments_replies_cnt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channel', to='Youtube.profile'),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to='Youtube.profile'),
        ),
    ]