# Generated by Django 4.1.7 on 2023-08-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_nota_foto_nota_nota_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='valor_material',
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
    ]
