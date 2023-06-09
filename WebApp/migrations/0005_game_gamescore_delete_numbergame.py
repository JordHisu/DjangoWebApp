# Generated by Django 4.1.7 on 2023-04-05 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('guess_number', 'Guess Number')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='WebApp.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='WebApp.player')),
            ],
        ),
        migrations.DeleteModel(
            name='NumberGame',
        ),
    ]
