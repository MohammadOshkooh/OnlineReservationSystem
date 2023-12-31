# Generated by Django 4.2.2 on 2023-07-07 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_alter_room_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('number_seats', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TrainSeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('is_reserved', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='is_reserved',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='TrainReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved_seats', models.PositiveIntegerField()),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.train')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='train',
            name='seats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trainseat'),
        ),
    ]
