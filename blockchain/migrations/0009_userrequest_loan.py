# Generated by Django 5.1.3 on 2024-11-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0008_delete_loan'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='loan',
            field=models.BooleanField(default=False),
        ),
    ]
