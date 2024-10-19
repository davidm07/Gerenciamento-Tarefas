from typing import List
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from drf_yasg import openapi
from django.db.models import Q
from django.contrib.auth import authenticate



# Create your views here.
@swagger_auto_schema(
    methods=['GET'],
    tags=['tasks'],
    manual_parameters=[
        openapi.Parameter('page', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
    ]
)
@swagger_auto_schema(
    methods=['POST'],
    request_body=serializers.TaskSerializer,
    tags=['tasks']
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])

def tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 1
        result_page = paginator.paginate_queryset(tasks, request)
        serializer = serializers.TaskSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(
    methods=["GET", "DELETE"],
    tags=['tasks'],
)
@swagger_auto_schema(
    methods=["PUT"],
    tags=['tasks'],
    request_body=serializers.TaskSerializer,
)
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])

def task_by_id(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = serializers.TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(
    methods=['POST'],
    request_body=serializers.UserSerializer,
    tags=['token'],
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register(request):
    serializer = serializers.UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'username': serializer.data['username']}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    methods=['POST'],
    request_body=serializers.UserSerializer,
    tags=['cadastro'],
)
@api_view(['POST'])

@permission_classes([IsAuthenticated])
def cadastro(request):
    serializer = serializers.UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'username': serializer.data['username']}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
