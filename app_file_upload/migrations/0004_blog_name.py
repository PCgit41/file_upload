# Generated by Django 4.2.9 on 2024-02-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_file_upload", "0003_remove_blog_file_remove_blog_title_blog_file_upload"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="name",
            field=models.CharField(
                default=None, max_length=250, null=True, verbose_name="NAME"
            ),
        ),
    ]
