# Generated by Django 4.2.2 on 2023-07-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_train_trainseat_room_is_reserved_trainreservation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='origin',
            field=models.CharField(default='sf', max_length=100),
            preserve_default=False,
        ),
    ]