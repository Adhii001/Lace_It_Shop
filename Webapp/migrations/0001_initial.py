# Generated by Django 5.0.4 on 2024-05-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactinfodb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=100, null=True)),
                ('csubject', models.CharField(blank=True, max_length=100, null=True)),
                ('cemail', models.CharField(blank=True, max_length=100, null=True)),
                ('cmessage', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
