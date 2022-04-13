from django.urls import path
from . import views

app_name = 'mesh'

urlpatterns = [
    path('', views.MeshView.as_view(), name='upload')
]