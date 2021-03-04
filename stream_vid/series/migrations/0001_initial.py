# Generated by Django 2.2.7 on 2021-02-20 08:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=300)),
                ('creator', models.CharField(blank=True, max_length=250, null=True)),
                ('genre', multiselectfield.db.fields.MultiSelectField(choices=[('action', 'Action'), ('adventure', 'Adventure'), ('animated', 'Animated'), ('comedy', 'Comedy'), ('crime', 'Crime'), ('documentary', 'Documentary'), ('drama', 'Drama'), ('fantasy', 'Fantasy'), ('horror', 'Horror'), ('kids', 'Kids')], max_length=100)),
                ('series_logo', models.ImageField(upload_to='images/')),
                ('trailer_url', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=280)),
                ('video_file_url', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.Series')),
            ],
        ),
    ]