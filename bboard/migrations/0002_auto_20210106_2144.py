# Generated by Django 3.1.5 on 2021-01-06 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bb',
            old_name='context',
            new_name='content',
        ),
    ]
