# Generated by Django 4.0.5 on 2022-06-28 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_drivers_contact_drivers_emoto_license_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivers',
            name='energy_consumption_rate',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
