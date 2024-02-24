# Generated by Django 4.2.4 on 2024-01-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_file_upload", "0002_remove_blog_author"),
    ]

    operations = [
        migrations.RemoveField(model_name="blog", name="file",),
        migrations.RemoveField(model_name="blog", name="title",),
        migrations.AddField(
            model_name="blog",
            name="file_upload",
            field=models.FileField(
                default=None, max_length=250, null=True, upload_to="uploads/"
            ),
        ),
    ]