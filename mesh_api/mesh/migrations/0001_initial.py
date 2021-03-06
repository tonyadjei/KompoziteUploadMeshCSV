# Generated by Django 4.0.3 on 2022-04-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mesh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trame', models.TextField(choices=[('1', 'T2 Ral M2 E2'), ('2', 'T2 Ral M4 E2'), ('3', 'T2 Ral M4 E3')])),
                ('mass_surf', models.FloatField()),
                ('is_compat_interior_wall', models.BooleanField()),
                ('mesh_height', models.FloatField()),
                ('mesh_width', models.FloatField()),
                ('mass_comb', models.FloatField()),
                ('roll_pallet', models.IntegerField()),
                ('color_names', models.CharField(max_length=10000)),
            ],
        ),
    ]
