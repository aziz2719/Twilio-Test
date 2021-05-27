from rest_framework import serializers
from rest_auth.models import TokenModel
from django.shortcuts import render
from .models import User, CheckCode
from .sendSms import save
import random

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField()

    def Generate(self):
        self.Gencode = random.randint(1000, 9999)
    
    def returnCode(self):
        code = self.Gencode
        return code

    def create(self, validated_data):
        request = "GET /user/check/ HTTP/1.1"
        self.Generate()
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        save(phone=validated_data["phone"], code=self.returnCode())
        user.save()

        TokenModel.objects.create(user=user)
        return user

class CheckCodeSerializer(serializers.Serializer):
    code = serializers.CharField()
    print(code)
    print(UserRegisterSerializer.returnCode)
    if code == UserRegisterSerializer.returnCode:
        print("true")
    else:
        print("false")

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    