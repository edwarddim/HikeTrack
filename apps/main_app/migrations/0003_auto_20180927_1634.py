# Generated by Django 2.1.1 on 2018-09-27 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20180926_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.FileField(upload_to='uploads'),
        ),
    ]
