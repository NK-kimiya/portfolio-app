# Generated by Django 5.1.4 on 2024-12-22 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GitProject",
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
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField()),
                ("subheading1", models.CharField(blank=True, max_length=200)),
                ("url1", models.URLField(blank=True)),
                ("subheading2", models.CharField(blank=True, max_length=200)),
                ("url2", models.URLField(blank=True)),
                ("subheading3", models.CharField(blank=True, max_length=200)),
                ("url3", models.URLField(blank=True)),
            ],
        ),
    ]