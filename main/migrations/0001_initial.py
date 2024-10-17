# Generated by Django 5.0 on 2024-10-17 18:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=200)),
                ('filepath', models.FilePathField(null=True, path='D:\\workshop\\python\\ongoing\\howa_resminama\\media')),
                ('date', models.DateField()),
                ('description', models.TextField(null=True)),
                ('signs_number', models.PositiveIntegerField(default=0)),
                ('signed', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default='Prosesde', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notifications', models.TextField(blank=True)),
                ('approved', models.BooleanField(default=False)),
                ('files_to_contrib', models.ManyToManyField(blank=True, related_name='reviewer', to='main.document')),
                ('personal_files', models.ManyToManyField(blank=True, related_name='owner', to='main.document')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
