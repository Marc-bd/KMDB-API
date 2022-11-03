from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20 )
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, max_length=127)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField()
    bio = serializers.CharField(allow_null=True, required=False)
    is_critic =  serializers.BooleanField(default=False)
    updated_at = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)



    def validate_email(self, value):
        email_already_exists = User.objects.filter(email=value).exists()

        if email_already_exists:
            raise serializers.ValidationError(detail="email already exists")
        
        return value

    def validate_username(self, value):
        username_already_exists = User.objects.filter(username=value).exists()

        if username_already_exists:
            raise serializers.ValidationError(detail="username already exists")

        return value

    def create(self, validated_data:dict) -> User:          
        for key, value in validated_data.items(): 
            if not key == "is_superuser" and not value == True:
                user = User.objects.create_user(**validated_data)
                return user        
            else:
                user = User.objects.create_superuser(**validated_data)
                return user


class LoginSerializer(serializers.Serializer): 
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)