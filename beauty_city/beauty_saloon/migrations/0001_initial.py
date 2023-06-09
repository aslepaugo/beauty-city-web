# Generated by Django 3.2.19 on 2023-05-24 10:34

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='master_photos')),
                ('employment_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('contact_info', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='salon_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('photo', models.ImageField(blank=True, upload_to='service_photos')),
                ('duration', models.DurationField(default='00:30:00')),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beauty_saloon.client')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beauty_saloon.master')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beauty_saloon.master')),
            ],
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beauty_saloon.salon')),
            ],
        ),
        migrations.AddField(
            model_name='master',
            name='salon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beauty_saloon.salon'),
        ),
        migrations.AddField(
            model_name='master',
            name='services',
            field=models.ManyToManyField(to='beauty_saloon.Service'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('is_paid', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beauty_saloon.client')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beauty_saloon.master')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beauty_saloon.service')),
            ],
        ),
    ]
