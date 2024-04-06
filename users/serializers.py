from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=127)
    birthdate = serializers.DateField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    bio = serializers.CharField(
        allow_blank=True, allow_null=True, default=None
    )
    is_critic = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validate_email(self, value: str) -> str:
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("This email already exists")

        return value

    def validate_username(self, value: str):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("This username already exists")

        return value

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
