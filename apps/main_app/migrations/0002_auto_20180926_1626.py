# Generated by Django 2.1.1 on 2018-09-26 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripdescription',
            name='tripdescript',
        ),
        migrations.AddField(
            model_name='trip',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TripDescription',
        ),
    ]
