from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Users
        fields =' __all__'