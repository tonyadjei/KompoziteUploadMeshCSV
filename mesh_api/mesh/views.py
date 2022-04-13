from django.db import IntegrityError
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from . import forms
from . import models
from .serializers import MeshSerializer
from .parseCSV import parse_csv_file


def save_csv_file(mesh_file):
    with open('mesh.csv', mode='wb+') as meshFile:
        for chunk in mesh_file.chunks():
            meshFile.write(chunk)


class MeshView(APIView):
    def get(self, request):
        mesh_form = forms.CreateMeshFile()
        return render(request, 'mesh/upload_mesh.html', {'form': mesh_form})    
    def post(self, request):
        mesh_file = request.data['mesh_file']
        if mesh_file.name.split('.')[1] == 'csv':
            save_csv_file(request.data['mesh_file'])
            mesh_items, errors = parse_csv_file('mesh.csv')
            for mesh in mesh_items:
                mesh_serializer = MeshSerializer(data=mesh)
                if mesh_serializer.is_valid():
                    try:
                        mesh_serializer.save()
                    except IntegrityError:
                        errors.append(f'There is already an existing mesh with id : <{mesh["id"]}>')
            if len(errors):
                mesh_form = forms.CreateMeshFile()
                return render(request, 'mesh/upload_mesh.html', {'errors': errors, 'form': mesh_form})     
            else:
                meshes = models.Mesh.objects.all()
                meshes_serializer = MeshSerializer(meshes, many=True)
                if len(meshes):
                    return Response({'count': len(meshes_serializer.data), 'data': meshes_serializer.data, 'message': 'All meshes have been successfully saved to the database.'})
        else:
            mesh_form = forms.CreateMeshFile()
            return render(request, 'mesh/upload_mesh.html', {'message': 'Please upload a csv file.', 'form': mesh_form})