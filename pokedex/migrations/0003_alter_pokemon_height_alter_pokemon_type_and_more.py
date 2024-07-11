# Generated by Django 4.2 on 2024-07-11 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='height',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('P', 'Planta'), ('L', 'Lagartija'), ('T', 'Tierra'), ('E', 'Eléctrico'), ('F', 'Fuego'), ('A', 'Agua')], max_length=30),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4),
        ),
    ]
