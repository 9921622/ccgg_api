# Generated by Django 3.2.8 on 2021-10-28 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccgg_api', '0005_auto_20211027_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pawn',
            old_name='indentifier',
            new_name='identifier',
        ),
    ]
