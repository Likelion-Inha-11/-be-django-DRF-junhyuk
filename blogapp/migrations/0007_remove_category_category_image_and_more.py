# Generated by Django 4.2.2 on 2023-06-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0006_post_foreign_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="category_image",
        ),
        migrations.RemoveField(
            model_name="category",
            name="selected",
        ),
        migrations.AlterField(
            model_name="category",
            name="category_name",
            field=models.TextField(max_length=200, null=True, verbose_name="카테고리"),
        ),
    ]