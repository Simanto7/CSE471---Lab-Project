# Generated by Django 2.1 on 2021-02-12 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210212_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('0', 'Pending'), ('1', 'Out for delivery'), ('2', 'Delivered')], max_length=200, null=True),
        ),
    ]
