# Generated by Django 4.1 on 2024-06-03 22:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0003_post_place"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="post",
        ),
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ManyToManyField(to="www.post"),
        ),
    ]
