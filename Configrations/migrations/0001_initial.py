# Generated by Django 3.0.6 on 2020-08-16 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.IntegerField(blank=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('body', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('key_words', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('trending', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
                ('visitors', models.IntegerField(default=0)),
                ('top_post', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Configrations.Staff')),
                ('tags', models.ManyToManyField(to='Configrations.Tag')),
            ],
        ),
    ]
