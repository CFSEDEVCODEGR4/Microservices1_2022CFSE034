from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

import json

from microapp.models import User
from microapp.serializers import UserSerializer

#============================================================================================
# Add User using custom endpoint
#============================================================================================
@api_view(['POST'])
def RegisterUserRestAPI(request):
	if request.method == 'POST':
		new_user_data = JSONParser().parse(request)
		
		u_id = new_user_data['user_id']
		user_name = new_user_data['user_name']
		user_mobile = new_user_data['user_mobile']
		user_email = new_user_data['user_email']
		user_password = new_user_data['user_password']

		if u_id is not None and user_name is not None and user_password is not None:	

			# Check if book_id already exists
			users = User.objects.all()
			users = users.filter(user_id = u_id)
			if (len(users) > 0):
				return JsonResponse({'message': 'User already exists.'}, status=status.HTTP_204_NO_CONTENT)

			
			serializer = UserSerializer(data=new_user_data)	
			if serializer.is_valid():
				serializer.save()
				return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
			else:
				return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
				return JsonResponse({'message': 'Mandatory details missing.'}, status=status.HTTP_204_NO_CONTENT)  
	else:
		return JsonResponse({'message': 'Request method error'}, status=status.HTTP_204_NO_CONTENT) 
#============================================================================================
