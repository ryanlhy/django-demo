# Generated by Django 4.1.7 on 2023-04-19 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0008_alter_customer_address_alter_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
