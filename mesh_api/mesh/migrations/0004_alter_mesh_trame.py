# Generated by Django 4.0.4 on 2022-04-13 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesh', '0003_mesh_name_mesh_variant_alter_mesh_color_names_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesh',
            name='trame',
            field=models.CharField(max_length=256),
        ),
    ]