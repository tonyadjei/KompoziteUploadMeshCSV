from django.shortcuts import redirect
from rest_framework.decorators import api_view


@api_view(['GET'])
def upload_page(request):
    return redirect('mesh:upload')