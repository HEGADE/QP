# Generated by Django 2.2.7 on 2020-05-30 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_papers', '0002_auto_20200530_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='isuue_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='provider',
            name='provide_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
