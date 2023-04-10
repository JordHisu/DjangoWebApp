# Generated by Django 4.1.7 on 2023-04-06 22:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0005_game_gamescore_delete_numbergame'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='type',
        ),
        migrations.AddField(
            model_name='game',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default='DEFAULT GAME NAME', max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='game',
            name='rules',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]