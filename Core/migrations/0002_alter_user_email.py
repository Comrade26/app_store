# Generated by Django 4.1.7 on 2023-04-18 15:29

import Core.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254,
                unique=True,
                validators=[Core.models.chula_email_validator],
            ),
        ),
    ]
