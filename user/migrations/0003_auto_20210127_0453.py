# Generated by Django 3.1.4 on 2021-01-27 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210127_0346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_new',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_season',
        ),
    ]