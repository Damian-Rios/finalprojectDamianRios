# Generated by Django 5.1.3 on 2024-12-03 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sets', '0002_remove_userset_logo_url_remove_userset_release_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userset',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
