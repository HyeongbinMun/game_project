# Generated by Django 3.1.3 on 2020-11-23 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0008_comment_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='modify_data',
        ),
    ]
