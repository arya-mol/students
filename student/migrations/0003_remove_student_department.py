# Generated by Django 3.2 on 2022-08-16 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20220816_0521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
    ]