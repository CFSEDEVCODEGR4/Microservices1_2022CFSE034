from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

import json

from microapp.models import User
from microapp.serializers import UserSerializer

#============================================================================================
# User registration using custom endpoint
#============================================================================================
 

#============================================================================================
# Login 
#============================================================================================
@api_view(['GET'])
def LoginAPI(request):
	if request.method == 'GET':

		user_name = request.query_params.get('user_name', None)
		user_password = request.query_params.get('user_password', None)			

		if user_name is not None and user_password is not None :	
			users = User.objects.all()
			userName = users.filter(user_name=user_name) 	
			userpswd = users.filter(user_password=user_password) 	
			if(len(userName) != 0):
				serializer = UserSerializer(users, many=True)
				res = JsonResponse(serializer.data, safe=False)
				return JsonResponse({'message': 'Login successful'})       
			else:
				return JsonResponse({'message': 'Invalid credentials, try again.'}, status=status.HTTP_204_NO_CONTENT)       
		else:
			return JsonResponse({'message': 'Invalid input, please check.'}, status=status.HTTP_204_NO_CONTENT)  

