# Generated by Django 4.1.7 on 2023-04-25 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Buyer", "0005_alter_customer_telephone"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Customer",
        ),
    ]
