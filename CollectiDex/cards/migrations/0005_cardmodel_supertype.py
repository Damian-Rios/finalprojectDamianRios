# Generated by Django 5.1.3 on 2024-12-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_cardmodel_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardmodel',
            name='supertype',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
