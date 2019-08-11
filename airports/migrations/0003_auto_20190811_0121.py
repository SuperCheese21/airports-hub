# Generated by Django 2.2.4 on 2019-08-11 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0002_auto_20190810_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='airport',
            name='longitude',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='Runway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length_ft', models.IntegerField(default=0)),
                ('width_ft', models.IntegerField(default=0)),
                ('surface', models.CharField(max_length=16)),
                ('lighted', models.BooleanField(default=False)),
                ('closed', models.BooleanField(default=False)),
                ('le_ident', models.CharField(max_length=8)),
                ('le_latitude', models.FloatField()),
                ('le_longitude', models.FloatField()),
                ('le_elevation_ft', models.IntegerField(default=0)),
                ('le_heading_true', models.DecimalField(decimal_places=1, max_digits=4)),
                ('le_displaced_threshold_ft', models.IntegerField(default=0)),
                ('he_ident', models.CharField(max_length=8)),
                ('he_latitude', models.FloatField()),
                ('he_longitude', models.FloatField()),
                ('he_elevation_ft', models.IntegerField(default=0)),
                ('he_heading_true', models.DecimalField(decimal_places=1, max_digits=4)),
                ('he_displaced_threshold_ft', models.IntegerField(default=0)),
                ('icao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='airports.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=128)),
                ('frequency', models.DecimalField(decimal_places=3, max_digits=6)),
                ('icao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='airports.Airport')),
            ],
        ),
    ]
