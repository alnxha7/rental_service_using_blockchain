# Generated by Django 5.1.3 on 2024-11-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0005_monthlypayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlypayment',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]