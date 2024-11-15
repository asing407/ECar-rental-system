# Generated by Django 5.1.1 on 2024-11-09 20:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carrent", "0002_vehicle_range"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicle",
            name="position_x",
        ),
        migrations.RemoveField(
            model_name="vehicle",
            name="position_y",
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="carrent.location"
            ),
        ),
    ]
