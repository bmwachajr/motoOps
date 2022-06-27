# Generated by Django 4.0.5 on 2022-06-27 12:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_drivers_contact_drivers_emoto_license_and_more'),
        ('batteries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='batteries',
            name='serial',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='batteries',
            name='state_of_charge',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='batteries',
            name='state_of_health',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='batteries',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('CHARGED', 'CHARGED'), ('CHARGING', 'CHARGING')], default='ACTIVE', max_length=50),
        ),
        migrations.CreateModel(
            name='BatteryTelematics',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('current_charge', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('longitude', models.CharField(max_length=100, null=True)),
                ('latitude', models.CharField(max_length=100, null=True)),
                ('battery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='batteries.batteries')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='drivers.drivers')),
            ],
            options={
                'db_table': 'battery_telematics',
            },
        ),
    ]
