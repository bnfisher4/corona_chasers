# Generated by Django 3.0.2 on 2020-03-24 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200324_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='global',
            name='china_deaths',
        ),
        migrations.RemoveField(
            model_name='global',
            name='china_infected',
        ),
        migrations.RemoveField(
            model_name='global',
            name='china_recovered',
        ),
        migrations.RemoveField(
            model_name='global',
            name='nonchina_deaths',
        ),
        migrations.RemoveField(
            model_name='global',
            name='nonchina_infected',
        ),
        migrations.RemoveField(
            model_name='global',
            name='nonchina_recovered',
        ),
    ]
