# Generated by Django 5.0 on 2024-04-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SampleModel",
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
                ("text", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name": "Sample Model",
                "verbose_name_plural": "Sample Models",
                "db_table": "sample_model",
            },
        ),
    ]
