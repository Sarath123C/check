# Generated by Django 4.2.1 on 2023-05-23 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_remove_person_female_person_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Materials_Required',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materials_required', models.CharField(choices=[('dnb', 'Debit Note Book'), ('pen', 'Pen'), ('ep', 'Exam Pappers')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='Materials',
        ),
        migrations.DeleteModel(
            name='Materials',
        ),
        migrations.AddField(
            model_name='person',
            name='materials_required',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='persons.materials_required'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='persons.gender'),
        ),
    ]
