#REST_FRAMEWORK
from rest_framework import serializers

from users.models import Users



class UsersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class UsersRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    userpassword = serializers.CharField(max_length=100)
    password_confirmation = serializers.CharField(max_length=100)

    def validate(self, data):
        if data["userpassword"] != data["password_confirmation"]:
            raise serializers.ValidationError("Password do not match")
        return data

    def create(self, validated_data):
        validated_data.pop("password_confirmation")
        user = Users.objects.create(
            username=validated_data["username"], email=validated_data["email"])
        user.set_password(validated_data["userpassword"])
        user.save()
        return user


class UsersLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    userpassword = serializers.CharField(max_length=100)

    def validate(self, data):
        user = Users.objects.filter(email=data["email"]).first()
        if user and user.verify_password(data["userpassword"]):
            return data
        raise serializers.ValidationError("Invalid credentials")

    def create(self, validated_data):
        return validated_data


