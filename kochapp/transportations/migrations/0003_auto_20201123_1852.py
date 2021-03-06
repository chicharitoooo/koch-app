# Generated by Django 3.1.3 on 2020-11-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportations', '0002_auto_20201113_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transportation',
            name='carrying_capacity',
        ),
        migrations.RemoveField(
            model_name='transportation',
            name='departure_date',
        ),
        migrations.AddField(
            model_name='transportation',
            name='from_shipment_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='transportation',
            name='to_shipment_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='transportation',
            name='weight',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transportation',
            name='volume',
            field=models.FloatField(),
        ),
    ]
