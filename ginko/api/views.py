from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response 

@api_view(['GET'])
def get_action(request):
    actionObj = actionModel.objects.all()
    actionSerializerObj = actionSerializer(actionObj,many=True)
    Resultmodel = actionSerializerObj.data
    return Response(Resultmodel)
