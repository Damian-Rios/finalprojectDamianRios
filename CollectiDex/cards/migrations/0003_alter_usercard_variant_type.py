# Generated by Django 5.1.3 on 2024-12-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_usercard_variant_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercard',
            name='variant_type',
            field=models.CharField(choices=[('normal', 'Normal'), ('holofoil', 'Holofoil'), ('reverseHolofoil', 'Reverse Holofoil'), ('firstEditionHolofoil', 'First Edition Holofoil')], max_length=50),
        ),
    ]
