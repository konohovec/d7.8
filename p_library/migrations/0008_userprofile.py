# Generated by Django 2.2.6 on 2020-07-19 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('p_library', '0007_auto_20200711_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('avatar', models.ImageField(upload_to='avatars/', verbose_name='Аватар')),
                ('birth_year', models.SmallIntegerField(verbose_name='Год рождения')),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=120, verbose_name='Локация')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]