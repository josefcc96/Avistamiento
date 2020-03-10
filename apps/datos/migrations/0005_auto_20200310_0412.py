# Generated by Django 3.0.4 on 2020-03-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0004_auto_20200310_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avistamiento',
            name='autor',
            field=models.CharField(max_length=128, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='avistamiento',
            name='latitud',
            field=models.FloatField(verbose_name='Latitud'),
        ),
        migrations.AlterField(
            model_name='avistamiento',
            name='longitud',
            field=models.FloatField(verbose_name='Longitud'),
        ),
        migrations.AlterField(
            model_name='avistamiento',
            name='observación',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='familia',
            field=models.TextField(max_length=128, verbose_name='Familia'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='n_cientifico',
            field=models.TextField(max_length=128, verbose_name='Nombre Cientifico'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='n_comun',
            field=models.TextField(max_length=128, verbose_name='Nombre Comun'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='alias',
            field=models.CharField(max_length=128, verbose_name='Alias'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='departamento',
            field=models.CharField(max_length=128, verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='nombre',
            field=models.CharField(max_length=128, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='pais',
            field=models.CharField(max_length=128, verbose_name='Pais'),
        ),
    ]
