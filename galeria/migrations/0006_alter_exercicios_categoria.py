# Generated by Django 4.2.1 on 2023-06-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_exercicios_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicios',
            name='categoria',
            field=models.CharField(choices=[('PEITO', 'Peito'), ('COSTAS', 'Costas'), ('BICEPS', 'Biceps'), ('TRICEPS', 'Triceps'), ('PERNAS', 'Pernas'), ('OMBROS', 'Ombros')], default='', max_length=100),
        ),
    ]
