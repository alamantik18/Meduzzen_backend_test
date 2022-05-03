from .models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    register_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()

        return instance