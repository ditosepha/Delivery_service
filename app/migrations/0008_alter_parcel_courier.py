# Generated by Django 5.0.6 on 2024-05-12 13:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_deliveryproof_options_alter_parcel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='courier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courier_parcels', to=settings.AUTH_USER_MODEL),
        ),
    ]
