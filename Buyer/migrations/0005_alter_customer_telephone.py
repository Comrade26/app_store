# Generated by Django 4.2 on 2023-04-18 13:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0004_remove_customer_email_remove_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='telephone',
            field=models.CharField(default='0000000000', max_length=10, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_telephone', message='Telephone number must start with 0 and have 10 digits', regex='^0\\d{9}$')]),
        ),
    ]
