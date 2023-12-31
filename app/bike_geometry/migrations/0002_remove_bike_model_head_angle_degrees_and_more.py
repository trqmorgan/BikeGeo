# Generated by Django 4.2.3 on 2023-07-18 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bike_geometry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike_model',
            name='head_angle_degrees',
        ),
        migrations.RemoveField(
            model_name='bike_model',
            name='model_size',
        ),
        migrations.RemoveField(
            model_name='bike_model',
            name='reach_mm',
        ),
        migrations.RemoveField(
            model_name='bike_model',
            name='seat_angle_degrees',
        ),
        migrations.RemoveField(
            model_name='bike_model',
            name='stack_mm',
        ),
        migrations.RemoveField(
            model_name='bike_model',
            name='top_tube_effective_mm',
        ),
        migrations.CreateModel(
            name='Bike_Geometry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_size', models.CharField(max_length=20)),
                ('reach_mm', models.IntegerField(default=None)),
                ('stack_mm', models.IntegerField(default=None)),
                ('top_tube_effective_mm', models.IntegerField(default=None)),
                ('seat_tube_center_top', models.IntegerField(default=None)),
                ('head_angle_degrees', models.IntegerField(default=None)),
                ('seat_angle_degrees', models.IntegerField(default=None)),
                ('head_tube_length_mm', models.IntegerField(default=None)),
                ('chainstay_length_mm', models.IntegerField(default=None)),
                ('wheelbase_mm', models.IntegerField(default=None)),
                ('front_center_mm', models.IntegerField(default=None)),
                ('standover_mm', models.IntegerField(default=None)),
                ('bb_drop_mm', models.IntegerField(default=None)),
                ('bb_height_mm', models.IntegerField(default=None)),
                ('bb_standard', models.CharField(max_length=20)),
                ('fork_offset_mm', models.IntegerField(default=None)),
                ('trail_mm', models.IntegerField(default=None)),
                ('seatpost_diameter_mm', models.IntegerField(default=None)),
                ('seat_clamp_size', models.IntegerField(default=None)),
                ('wheel_size', models.CharField(max_length=20)),
                ('front_travel_mm', models.IntegerField(default=None)),
                ('rear_travel_mm', models.IntegerField(default=None)),
                ('socks_size', models.CharField(max_length=20)),
                ('model_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike_geometry.bike_model')),
            ],
        ),
    ]
