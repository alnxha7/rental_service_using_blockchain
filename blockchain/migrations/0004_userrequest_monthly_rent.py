# Generated by Django 5.1.3 on 2024-11-26 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0003_alter_rentalagreement_terms'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='monthly_rent',
            field=models.BooleanField(default=False),
        ),
    ]
