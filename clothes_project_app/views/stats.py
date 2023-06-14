from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from clothes_project_app.models import *


# Create your views here.
@api_view(['GET'])
def stats(request):


    ret_val = {

    }
    return Response(ret_val)