# Generated by Django 3.2.3 on 2021-05-27 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='number',
        ),
    ]
