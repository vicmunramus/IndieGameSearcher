# Generated by Django 3.1.2 on 2021-01-02 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamesearcher', '0007_remove_game_currencytype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='buyURL',
            new_name='downloadURL',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='image',
            new_name='imageURL',
        ),
    ]
