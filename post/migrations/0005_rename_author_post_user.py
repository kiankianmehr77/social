# Generated by Django 4.2.17 on 2025-01-01 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_created_alter_post_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
    ]
