# Generated by Django 2.2.12 on 2020-06-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0002_remove_genre_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='photo',
            field=models.ImageField(blank=True, default=False, null=True, upload_to='photos/genre'),
        ),
    ]
