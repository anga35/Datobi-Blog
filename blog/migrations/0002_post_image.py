# Generated by Django 3.2.5 on 2022-05-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='post_thumbnail'),
        ),
    ]
