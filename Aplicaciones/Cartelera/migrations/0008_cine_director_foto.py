# Generated by Django 4.0.6 on 2024-07-09 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0007_genero_foto_pelicula_portada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('direccion', models.CharField(default='', max_length=150)),
                ('telefono', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='portadas'),
        ),
    ]
