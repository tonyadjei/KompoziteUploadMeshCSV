from django.db import models

class Mesh(models.Model):
    trame_values = [
        ('1', 'T2 Ra1 M2 E2'),
        ('2', 'T2 Ra1 M4 E2'),
        ('3', 'T2 Ra1 M4 E3'),
    ]
    id = models.CharField(max_length=256, primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    trame = models.CharField(max_length=256)
    mass_surf = models.FloatField()
    is_compat_interior_wall = models.BooleanField(blank=False, null=False)
    mesh_height = models.FloatField()
    mesh_width = models.FloatField()
    mass_comb = models.FloatField()
    roll_pallet = models.IntegerField()
    color_names = models.CharField(max_length=512)


class UploadMesh(models.Model):
    mesh_file = models.FileField()