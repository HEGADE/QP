# Generated by Django 3.0.6 on 2020-06-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_papers', '0003_auto_20200530_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='issues',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='provider',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
