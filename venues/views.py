from django.shortcuts import render
from . import serializers
from . import models  
from rest_framework.views import APIView
from rest_framework.response import Response

class VenuesView(APIView):
    def post(self,request):
    	'''
    	datos = request.data
    	datos['user'] = request.user.id
		serializer = PersonSerializer(data=datos)
		if serializer.is_valid()
			serializer.save()
			return Response(serializer.data,status = status.HTTP_201_CREATED)
		return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
	   	'''

    def get(self, request):
	    model = models.Venue.objects.all()
	    serializer_class = serializers.VenueSerializer(model, many="True")
	    return Response(serializer_class.data)
    	