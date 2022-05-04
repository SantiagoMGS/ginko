from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response 

@api_view(['GET', 'POST'])
def get_action(request):
    if request.method == 'GET':
        ApiObj = actionModel.objects.all()
        ApiSerializer = actionSerializer(ApiObj,many=True)
        return Response(ApiSerializer.data)

    elif request.method == 'POST':
        ApiSerializer = actionSerializer(data = request.data)
        if ApiSerializer.is_valid():
            ApiSerializer.save()
            return Response(ApiSerializer.data)
        return Response(ApiSerializer.errors)

@api_view(['GET','PUT','DELETE'])
def get_action_detail(request, pk=None):

    if request.method == "GET":
            Api = actionModel.objects.filter(action_id = pk).first()
            ApiSerializer = actionSerializer(Api)
            return Response(ApiSerializer.data)

    elif request.method == 'PUT':
        Api = actionModel.objects.filter(action_id = pk).first()
        ApiSerializer = actionSerializer(Api, data = request.data)
        if ApiSerializer.is_valid():
            ApiSerializer.save()
            return Response(ApiSerializer.data)
        return Response(ApiSerializer.errors)

    elif request.method == 'DELETE':
        Api = actionModel.objects.filter(action_id = pk).first()
        Api.delete()
        return Response("deleted object")