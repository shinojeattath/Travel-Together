# Generated by Django 5.0.4 on 2024-04-05 04:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("travel_app", "0002_sub_places"),
    ]

    operations = [
        migrations.AddField(
            model_name="travelling_user",
            name="phone",
            field=models.CharField(max_length=30, null=True),
        ),
    ]