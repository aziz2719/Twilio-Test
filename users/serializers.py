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
        self.Gencode = str(random.randint(1000, 9999))
        codes = []
        codes.append(self.Gencode)
        return codes

    def create(self, validated_data):
        self.Generate()
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        save(phone=validated_data["phone"], code=self.Generate())
        user.save()
        TokenModel.objects.create(user=user)
        return user

class CheckCodeSerializer(serializers.Serializer):
    code = serializers.CharField()
 
    def create(self, validated_data):
        if self.code == UserRegisterSerializer.Generate(self):
            self.code = CheckCode.objects.create(**validated_data)
        else:
            print(False)
        return self.code

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()