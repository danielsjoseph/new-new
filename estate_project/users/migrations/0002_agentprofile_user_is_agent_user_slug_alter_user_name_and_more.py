# Generated by Django 4.2.3 on 2023-09-29 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('display_picture', models.ImageField(default='images/default.jfif', upload_to='images/')),
                ('contact', models.IntegerField(default=123456789)),
                ('wa_number', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('contact', models.IntegerField(default=0)),
                ('wa_number', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Apartments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('location', models.TextField(max_length=255)),
                ('is_available', models.CharField(choices=[('Available', 'Available'), ('Rented', 'Rented'), ('Sold', 'Sold')], max_length=255)),
                ('looking_for', models.CharField(choices=[('Rent', 'Rent'), ('Sale', 'Sale')], max_length=255)),
                ('property_type', models.CharField(choices=[('Duplex', 'Duplex'), ('Bungalow', 'Bungalow'), ('Apartment', 'Apartment'), ('Land', 'Land')], max_length=255)),
                ('display_picture', models.ImageField(upload_to='images/')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.agentprofile')),
            ],
        ),
        migrations.AddField(
            model_name='agentprofile',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
