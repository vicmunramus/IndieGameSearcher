# Generated by Django 3.1.2 on 2021-01-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesearcher', '0008_auto_20210102_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(default='No description'),
        ),
    ]