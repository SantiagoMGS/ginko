from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status


@api_view(['GET', 'POST'])
def get_action(request):

    # List all
    if request.method == 'GET':
        # Query set
        ApiObj = actionModel.objects.all()
        ApiSerializer = actionSerializer(ApiObj,many=True)
        return Response(ApiSerializer.data, status = status.HTTP_200_OK)
    # Create
    elif request.method == 'POST':
        ApiSerializer = actionSerializer(data = request.data)
        # Validation
        if ApiSerializer.is_valid():
            ApiSerializer.save()
            return Response(ApiSerializer.data, status = status.HTTP_201_CREATED)
        return Response(ApiSerializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def get_action_detail(request, pk=None):
    # Query set
    Api = actionModel.objects.filter(action_id = pk).first()
    # Validation
    if Api:
        # Retrieve
        if request.method == "GET":
                ApiSerializer = actionSerializer(Api)
                return Response(ApiSerializer.data, status = status.HTTP_200_OK)
        # Update
        elif request.method == 'PUT':
            ApiSerializer = actionSerializer(Api, data = request.data)
            if ApiSerializer.is_valid():
                ApiSerializer.save()
                return Response(ApiSerializer.data, status = status.HTTP_200_OK)
            return Response(ApiSerializer.errors, status = status.HTTP_400_BAD_REQUEST)
        # Delete
        elif request.method == 'DELETE':
            Api.delete()
            return Response({'message':'Deleted object'}, status = status.HTTP_200_OK)
    
    return Response({'message':'Object not found'}, status = status.HTTP_400_BAD_REQUEST)