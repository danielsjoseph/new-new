from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields='__all__'
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            is_agent=validated_data['is_agent']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ApartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartments
        fields = '__all__'

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'