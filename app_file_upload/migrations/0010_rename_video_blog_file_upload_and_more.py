# Generated by Django 4.2.4 on 2024-02-05 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_file_upload", "0009_alter_blog_video"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blog", old_name="video", new_name="file_upload",
        ),
        migrations.RenameField(model_name="blog", old_name="caption", new_name="name",),
        migrations.RemoveField(model_name="blog", name="image",),
    ]
