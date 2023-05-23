# Generated by Django 4.2.1 on 2023-05-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0008_alter_gender_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='person',
            name='materials_required',
        ),
        migrations.AddField(
            model_name='person',
            name='female',
            field=models.BooleanField(default=False, verbose_name='Female'),
        ),
        migrations.AddField(
            model_name='person',
            name='male',
            field=models.BooleanField(default=False, verbose_name='Male'),
        ),
        migrations.AddField(
            model_name='person',
            name='note',
            field=models.BooleanField(default=False, verbose_name='Note Book'),
        ),
        migrations.AddField(
            model_name='person',
            name='paper',
            field=models.BooleanField(default=False, verbose_name='Exam Paper'),
        ),
        migrations.AddField(
            model_name='person',
            name='pen',
            field=models.BooleanField(default=False, verbose_name='Pen'),
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Materials_Required',
        ),
    ]