# Generated by Django 4.2.2 on 2023-07-07 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='bed_type',
        ),
        migrations.RemoveField(
            model_name='room',
            name='num_beds',
        ),
    ]
