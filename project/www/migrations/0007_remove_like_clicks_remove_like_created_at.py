# Generated by Django 4.1 on 2024-06-04 21:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0006_alter_comment_text_like"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="like",
            name="clicks",
        ),
        migrations.RemoveField(
            model_name="like",
            name="created_at",
        ),
    ]
