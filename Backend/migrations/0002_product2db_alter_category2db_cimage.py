# Generated by Django 5.0.4 on 2024-05-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product2db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(blank=True, max_length=100, null=True)),
                ('pprice', models.IntegerField(blank=True, null=True)),
                ('pdescription', models.CharField(blank=True, max_length=500, null=True)),
                ('pimage', models.ImageField(blank=True, null=True, upload_to='product_images')),
            ],
        ),
        migrations.AlterField(
            model_name='category2db',
            name='cimage',
            field=models.ImageField(blank=True, null=True, upload_to='category_images'),
        ),
    ]
