# Generated by Django 2.2.6 on 2019-10-11 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('title_en', models.CharField(max_length=20)),
                ('audience', models.IntegerField()),
                ('open_date', models.DateTimeField()),
                ('genre', models.CharField(max_length=20)),
                ('watch_grade', models.CharField(max_length=20)),
                ('score', models.FloatField()),
                ('pster_url', models.TextField()),
                ('desription', models.TextField()),
            ],
        ),
    ]
