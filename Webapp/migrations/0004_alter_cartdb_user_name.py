# Generated by Django 5.0.4 on 2024-05-31 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0003_cartdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdb',
            name='User_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
