# Generated by Django 5.0.3 on 2024-04-03 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
