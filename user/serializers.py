from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import IntegrityError

CustomUser = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'location',
                  'phone_number', 'date_of_birth', 'profile_picture',
                  'password']
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'location': {'required': True},
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if 'email' in attrs:
            # Ensure email is in the correct format
            email = attrs['email']
            if '@' not in email:
                raise serializers.ValidationError(
                    "Email must be a valid email address.")
        return attrs

    def create(self, validated_data):
        email = validated_data.pop('email')
        username = email.split('@')[0]
        password = validated_data.pop('password')

        try:
            user = CustomUser.objects.create_user(username=username,
                                                  email=email,
                                                  password=password,
                                                  **validated_data)
            return user
        except IntegrityError:
            raise serializers.ValidationError(
                "A user with this email already exists.")
