# Generated by Django 2.2.10 on 2021-04-03 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_storeproduct_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
