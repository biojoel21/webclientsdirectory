# Generated by Django 5.1.2 on 2024-10-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdirectory', '0003_remove_newsfeed_imageurl_newsfeed_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='building',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
