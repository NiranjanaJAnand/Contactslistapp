# Generated by Django 5.0.6 on 2024-07-08 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact", old_name="is_favorited", new_name="is_favorite",
        ),
    ]
