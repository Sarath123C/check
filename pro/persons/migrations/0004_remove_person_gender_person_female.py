# Generated by Django 4.2.1 on 2023-05-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_remove_person_female_remove_person_male_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='gender',
        ),
        migrations.AddField(
            model_name='person',
            name='Female',
            field=models.BooleanField(default=False, verbose_name='Male'),
        ),
    ]
