# Generated by Django 3.0.6 on 2020-08-21 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configrations', '0008_auto_20200820_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='show_thumbnail',
            field=models.BooleanField(default=False),
        ),
    ]
