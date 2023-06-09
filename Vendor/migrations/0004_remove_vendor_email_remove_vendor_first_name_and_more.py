# Generated by Django 4.2 on 2023-04-18 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0003_alter_product_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/product/'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='qr_picture',
            field=models.ImageField(null=True, upload_to='images/qr_picture/'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='store_picture',
            field=models.ImageField(null=True, upload_to='images/store_picture/'),
        ),
    ]
