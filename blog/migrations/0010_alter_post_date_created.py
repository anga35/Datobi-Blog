# Generated by Django 3.2.5 on 2022-05-05 13:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 13, 29, 49, 873515, tzinfo=utc)),
        ),
    ]