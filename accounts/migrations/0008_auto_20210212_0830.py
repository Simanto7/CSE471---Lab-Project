# Generated by Django 2.1 on 2021-02-12 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210212_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', '0'), ('Out for delivery', '1'), ('Delivered', '2')], max_length=200, null=True),
        ),
    ]
