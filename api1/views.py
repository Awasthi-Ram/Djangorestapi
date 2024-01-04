from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from rest_framework import viewsets
# Create your views here.
from api1.models import Movie,collections
from api1.serializers import MovieSerializer,collectionsSerializer

from rest_framework.response import Response
from rest_framework.decorators import action
def home(request):
    movie=['dunki','animals','jawan']
    return JsonResponse(movie,safe=False)

class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer


    #apimovies/{movieid}/collection
    @action(detail=True,methods=['get'])
    def collection(self,request,pk=None):
        try:
            movie1 =Movie.objects.get(pk=pk)
            coll = collections.objects.filter(movie=movie1)

            coll_serializer=collectionsSerializer(coll,many=True,context={'request':request})
            print("method get collection of ",pk,"collection movie")

            return Response(coll_serializer.data)
        except Exception as e:
            return Response({
                'message':"Collection not exites"
            }
            )
    

       
        

class collectionsViewSet(viewsets.ModelViewSet):
    queryset=collections.objects.all()
    serializer_class=collectionsSerializer