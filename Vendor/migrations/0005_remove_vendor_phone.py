# Generated by Django 4.2 on 2023-04-18 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0004_remove_vendor_email_remove_vendor_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='phone',
        ),
    ]