# Generated by Django 4.1.7 on 2023-05-10 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("payment_id", models.IntegerField()),
                ("stamp", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("plane_number", models.CharField(max_length=100)),
                ("departure_airport", models.CharField(max_length=100)),
                ("destin_airport", models.CharField(max_length=100)),
                ("departure_datetime", models.DateTimeField()),
                ("arrival_datetime", models.DateTimeField()),
                ("seatbusi_occupied", models.IntegerField()),
                ("max_seatbusi", models.IntegerField()),
                ("seatbusi_price", models.FloatField()),
                ("seatcoom_occupied", models.IntegerField()),
                ("max_seatcoom", models.IntegerField()),
                ("seatcoom_price", models.FloatField()),
                ("seatfirst_occupied", models.IntegerField()),
                ("max_seatfirst", models.IntegerField()),
                ("seatfirst_price", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Refund",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_id", models.CharField(max_length=20)),
                ("refund_time", models.DateTimeField()),
                (
                    "booking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="aggregator.booking",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_id", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("seat_type", models.CharField(max_length=20)),
                ("status", models.CharField(max_length=20)),
                (
                    "booking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="aggregator.booking",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="booking",
            name="flight",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="aggregator.flight"
            ),
        ),
    ]
