# Generated by Django 2.2.7 on 2019-11-26 01:26

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
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('openyear', models.CharField(max_length=10)),
                ('showtime', models.CharField(max_length=10)),
                ('watchgrade', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=20)),
                ('audience', models.IntegerField()),
                ('discription', models.TextField()),
                ('poster_url', models.CharField(max_length=150)),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
                ('liked_user', models.ManyToManyField(related_name='liked_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('score', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('img', models.CharField(max_length=500)),
                ('movies', models.ManyToManyField(related_name='directors', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('img', models.CharField(max_length=500)),
                ('movies', models.ManyToManyField(related_name='actors', to='movies.Movie')),
            ],
        ),
    ]
