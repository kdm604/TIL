# Generated by Django 2.2.6 on 2019-10-11 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='pster_url',
            new_name='poster_url',
        ),
    ]