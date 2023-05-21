from django.shortcuts import render

from rest_framework import generics
from microapp.serializers import  UserSerializer
from microapp.serializers import  User
               

# ===================================================
# Users
# ===================================================
class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = User.objects.all()
        # Allow filter/search using mobile as query parameter
        in_user_id = self.request.query_params.get('user_id', None)
        if (in_user_id is not None):
            queryset = queryset.filter(user_id = in_user_id)
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()



