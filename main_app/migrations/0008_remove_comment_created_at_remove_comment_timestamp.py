# Generated by Django 4.1.7 on 2023-03-20 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_comment_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='timestamp',
        ),
    ]
