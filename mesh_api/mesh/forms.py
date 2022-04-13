from django import forms
from . import models



class CreateMeshFile(forms.ModelForm):
    class Meta:
        model = models.UploadMesh
        fields = ['mesh_file']

class MeshForm(forms.ModelForm):
    class Meta:
        model = models.Mesh
        fields = ['id', 'name', 'trame', 'mass_surf', 
        'is_compat_interior_wall', 'mesh_height', 
        'mesh_width', 'mass_comb', 'roll_pallet', 'color_names']