# Generated by Django 4.0.6 on 2024-06-04 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0005_pelicula'),
        
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.TimeField(null=True),
        ),
    ]
