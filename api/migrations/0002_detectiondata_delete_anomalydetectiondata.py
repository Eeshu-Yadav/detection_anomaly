# Generated by Django 5.0.6 on 2024-05-23 20:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DetectionData",
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
                ("protocol", models.CharField(max_length=10)),
                ("service", models.CharField(max_length=10)),
                ("flag", models.CharField(max_length=10)),
                ("src_bytes", models.FloatField()),
                ("dst_bytes", models.FloatField()),
                ("count", models.FloatField()),
                ("same_srv_rate", models.FloatField()),
                ("diff_srv_rate", models.FloatField()),
                ("dst_host_serve_count", models.FloatField()),
                ("dst_host_same_serve_count", models.FloatField()),
                ("result", models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name="AnomalyDetectionData",
        ),
    ]
