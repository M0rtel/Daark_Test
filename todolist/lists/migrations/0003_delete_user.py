# Generated by Django 4.2.1 on 2023-05-19 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
