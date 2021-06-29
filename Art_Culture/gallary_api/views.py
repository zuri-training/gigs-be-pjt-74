from django.shortcuts import render
from django.http import HttpResponse
from .models import Art
from .serializers import ArtSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class ArtAPIView(APIView):
    
    def get(self, request):
        arts = Art.objects.all()
        serializer = ArtSerializer(arts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArtSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Art detail view
class ArtDetails(APIView):
    def get_obeject(self, id):
        try:
            return Art.objects.get(id=id)

        except Art.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        art = self.get_obeject(id)
        serializer = ArtSerializer(art)
        return Response(serializer.data)

    def put(self, request, id):
        art = self.get_obeject(id)
        serializer = ArtSerializer(art, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        art = self.get_obeject(id)
        art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Create your views here.
