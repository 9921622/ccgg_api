# Generated by Django 3.2.8 on 2021-10-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccgg_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turtle',
            name='last_ping',
        ),
        migrations.RemoveField(
            model_name='turtle',
            name='x',
        ),
        migrations.RemoveField(
            model_name='turtle',
            name='y',
        ),
        migrations.RemoveField(
            model_name='turtle',
            name='z',
        ),
        migrations.AddField(
            model_name='turtle',
            name='command',
            field=models.CharField(default='', max_length=300),
        ),
    ]
