# Generated by Django 3.1.4 on 2020-12-15 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_delete_votecounter'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]