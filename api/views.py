from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import *
from .serializers import *
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getData(request):
    res = [
        'GET: api/',
        'GET: api/video/',
        'GET: api/flight/',
        'POST: api/upload/',
        'PUT: api/update/<str:pk>'
    ]
    return Response(res)

@api_view(['GET'])
def getVideo(request):
    if request.method == 'GET':
        video = Video.objects.all()
        serializer = videoSerializer(video, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def getPost(request):
      if request.method == 'POST':
        serializer = videoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
@api_view(['GET', 'PUT', 'DELETE'])
def updatePost(request, pk):
    video = Video.objects.get(pk=pk)
    serializer = videoSerializer(video)
    if request.method == "GET":
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "PUT":
        serializer = videoSerializer(video, data=request.data)
    if serializer.is_valid():
        serializer.save(isinstance=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "DELETE":
        video.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def querySet(request):
    video = Video.objects.all()
    search = request.query_params.get('q')
    if search != None and search != '':
        videos = video.filter(
            Q(videoName__icontains=search)
        ).distinct()
    serializer = videoSerializer(videos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)






    


