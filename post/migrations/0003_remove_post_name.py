# Generated by Django 4.2.17 on 2025-01-01 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
    ]