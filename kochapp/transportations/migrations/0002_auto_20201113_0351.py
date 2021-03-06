# Generated by Django 3.1.3 on 2020-11-13 03:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transportations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('vehicle_comment', models.TextField(blank=True, null=True)),
                ('carrying_capacity', models.FloatField()),
                ('volume', models.IntegerField()),
                ('price', models.IntegerField()),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vehicle_from_region', to='transportations.city')),
                ('from_region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vehicle_from_region', to='transportations.region')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vehicle_to_city', to='transportations.city')),
                ('to_region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vehicle_to_region', to='transportations.region')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_published'],
            },
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
