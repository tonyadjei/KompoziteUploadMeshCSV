from rest_framework import serializers
from .models import Mesh


class MeshSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=256)
    name = serializers.CharField(max_length=256)
    trame = serializers.CharField(max_length=256)
    mass_surf = serializers.FloatField()
    is_compat_interior_wall = serializers.BooleanField()
    mesh_height = serializers.FloatField()
    mesh_width = serializers.FloatField()
    mass_comb = serializers.FloatField()
    roll_pallet = serializers.IntegerField()
    color_names = serializers.CharField(max_length=512)

    def create(self, validated_data):
        return Mesh.objects.create(**validated_data)