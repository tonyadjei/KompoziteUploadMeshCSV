# Generated by Django 4.0.4 on 2022-04-13 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesh', '0004_alter_mesh_trame'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesh',
            name='variant',
        ),
        migrations.AlterField(
            model_name='mesh',
            name='id',
            field=models.CharField(max_length=256, primary_key=True, serialize=False),
        ),
    ]