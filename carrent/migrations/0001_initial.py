# Generated by Django 5.1.1 on 2024-11-05 22:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                ("locationID", models.AutoField(primary_key=True, serialize=False)),
                ("address", models.CharField(max_length=255)),
                ("position_x", models.FloatField()),
                ("position_y", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="UserType",
            fields=[
                ("typeID", models.AutoField(primary_key=True, serialize=False)),
                ("typeName", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Rental",
            fields=[
                ("rentalID", models.AutoField(primary_key=True, serialize=False)),
                ("startTime", models.DateTimeField(auto_now_add=True)),
                ("endTime", models.DateTimeField(blank=True, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rentals",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                ("paymentID", models.AutoField(primary_key=True, serialize=False)),
                ("cardNumber", models.CharField(max_length=16)),
                ("expiryDate", models.CharField(max_length=5)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=6)),
                ("is_paid", models.BooleanField(default=False)),
                (
                    "rental",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="carrent.rental"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Operator",
            fields=[
                ("operatorID", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=128)),
                (
                    "userType",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="carrent.usertype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Manager",
            fields=[
                ("managerID", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=128)),
                (
                    "userType",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="carrent.usertype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("customerID", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=128)),
                ("accountBalance", models.FloatField()),
                (
                    "activeRental",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="active_customer",
                        to="carrent.rental",
                    ),
                ),
                (
                    "userType",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="carrent.usertype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                ("vehicleID", models.AutoField(primary_key=True, serialize=False)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("e_bike", "Electric Bike"),
                            ("scooter", "Electric Scooter"),
                        ],
                        max_length=50,
                    ),
                ),
                ("batteryStatus", models.FloatField()),
                ("isDefective", models.BooleanField(default=False)),
                (
                    "cost_per_minute",
                    models.DecimalField(decimal_places=2, default=0.2, max_digits=5),
                ),
                ("position_x", models.FloatField()),
                ("position_y", models.FloatField()),
                (
                    "location",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="carrent.location",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="rental",
            name="vehicle",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="carrent.vehicle"
            ),
        ),
        migrations.CreateModel(
            name="VehicleActivity",
            fields=[
                ("activityID", models.AutoField(primary_key=True, serialize=False)),
                ("activityType", models.CharField(max_length=100)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="carrent.vehicle",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                ("reportID", models.AutoField(primary_key=True, serialize=False)),
                ("startDate", models.DateField()),
                ("endDate", models.DateField()),
                ("activities", models.ManyToManyField(to="carrent.vehicleactivity")),
            ],
        ),
    ]