# Generated by Django 3.2 on 2021-05-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_papers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='college',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
