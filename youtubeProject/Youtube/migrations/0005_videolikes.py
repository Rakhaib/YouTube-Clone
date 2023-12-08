# Generated by Django 4.2.7 on 2023-12-05 05:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Youtube', '0004_remove_profile_first_name_remove_profile_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Youtube.video')),
            ],
            options={
                'unique_together': {('video', 'user')},
            },
        ),
    ]
