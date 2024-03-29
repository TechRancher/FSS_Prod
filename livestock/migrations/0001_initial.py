# Generated by Django 2.1.7 on 2019-03-21 22:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LivestockReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_Date', models.DateField(default=datetime.datetime.now)),
                ('sale_Type', models.CharField(default='Livestock', max_length=20)),
                ('type_Livestock', models.CharField(max_length=30)),
                ('head_Count', models.IntegerField(blank=True, null=True)),
                ('livestock_weight', models.CharField(choices=[('Weight', (('100-200', '100-200'), ('200-300', '200-300'), ('300-400', '300-400'), ('400-500', '400-500'), ('500-600', '500-600'), ('600-700', '600-700'), ('700-800', '700-800'), ('800-900', '800-900'), ('900-1000', '900-1000'), ('1000-1100', '1000-1100'), ('1100-1200', '1100-1200'), ('1200-1300', '1200-1300'), ('1300-1400', '1300-1400'), ('1400-1500', '1400-1500'), ('1500-1600', '1500-1600'), ('1600-1700', '1600-1700'), ('1700-1800', '1700-1800'), ('1800-1900', '1800-1900'), ('1900-2000', '1900-2000'), ('2000-2100', '2000-2100'), ('2100-2200', '2100-2200'), ('2200-2300', '2200-2300'), ('2300-2400', '2300-2400'), ('2400-2500', '2400-2500'), ('2500-5000', '2500-5000'))), ('Age', (('Young', 'Young'), ('Older', 'Older'))), ('Bottle Calves', (('Bottle Calves', 'Bottle Calves'),)), ('Pairs', (('Pairs', 'Pairs'),))], default='100-200', max_length=20)),
                ('high_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('remarks', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
