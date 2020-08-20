# Generated by Django 3.0.6 on 2020-08-16 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configrations', '0003_auto_20200815_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='text',
            new_name='tag',
        ),
        migrations.AddField(
            model_name='post',
            name='catogory',
            field=models.ManyToManyField(to='Configrations.Category'),
        ),
    ]