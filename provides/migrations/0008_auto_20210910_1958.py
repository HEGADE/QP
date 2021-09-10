# Generated by Django 3.2 on 2021-09-10 14:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provides', '0007_alter_provide_paper_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provide',
            old_name='board',
            new_name='governing_body',
        ),
        migrations.RenameField(
            model_name='provide',
            old_name='claass',
            new_name='paper_title',
        ),
        migrations.RenameField(
            model_name='provide',
            old_name='provide_date',
            new_name='provided_date',
        ),
        migrations.RenameField(
            model_name='provide',
            old_name='papertitle',
            new_name='subject_name',
        ),
        migrations.RemoveField(
            model_name='provide',
            name='college',
        ),
        migrations.RemoveField(
            model_name='provide',
            name='sem',
        ),
        migrations.RemoveField(
            model_name='provide',
            name='sub',
        ),
        migrations.AddField(
            model_name='provide',
            name='course_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='provide',
            name='education_type',
            field=models.CharField(choices=[('sslc', 'SSLC'), ('puc', 'PUC'), ('degree', 'Degree'), ('engineering', 'Engineering'), ('diploma', 'Diploma'), ('iti', 'ITI')], default='sslc', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provide',
            name='period',
            field=models.CharField(choices=[('first', 'first'), ('second', 'second'), ('third', 'third'), ('fourth', 'fourth'), ('fifth', 'fifth'), ('sixth', 'sixth'), ('seventh', 'seventh'), ('eighth', 'eighth')], default='first', max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='provide',
            name='doc',
            field=models.FileField(upload_to='provider', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='provide',
            name='paper_type',
            field=models.CharField(choices=[('board', 'Board'), ('university', 'University')], max_length=100),
        ),
    ]
