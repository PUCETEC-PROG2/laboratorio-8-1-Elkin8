# Generated by Django 4.2 on 2024-07-11 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_alter_pokemon_height_alter_pokemon_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('A', 'Agua'), ('P', 'Planta'), ('E', 'Eléctrico'), ('T', 'Tierra'), ('L', 'Lagartija'), ('F', 'Fuego')], max_length=30),
        ),
    ]
