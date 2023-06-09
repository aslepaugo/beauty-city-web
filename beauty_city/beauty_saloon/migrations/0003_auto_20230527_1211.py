# Generated by Django 3.2.19 on 2023-05-27 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beauty_saloon', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='payment_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='client_photos'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beauty_saloon.client'),
        ),
    ]
