from rest_framework import serializers
from microapp.models import User

# ============================================================
# App User 
# ============================================================
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'user_id', 
                  'user_name',
                  'user_email',
                  'user_mobile',
                  'user_password'                   
                  ]
# ============================================================