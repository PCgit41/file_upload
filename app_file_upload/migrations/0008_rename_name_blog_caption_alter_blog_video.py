# Generated by Django 4.2.4 on 2024-02-05 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_file_upload", "0007_rename_file_upload_blog_video"),
    ]

    operations = [
        migrations.RenameField(model_name="blog", old_name="name", new_name="caption",),
        migrations.AlterField(
            model_name="blog",
            name="video",
            field=models.FileField(
                default="", max_length=250, null=True, upload_to="input/%y"
            ),
        ),
    ]
