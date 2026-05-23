import os
from datetime import datetime, timedelta, timezone

import jwt
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import serializers

from .models import User


def generate_user_token(user_id):
    payload = {
        "id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(days=30),
    }
    return jwt.encode(payload, os.environ.get("JWT_SECRET", settings.SECRET_KEY), algorithm="HS256")


class UserSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id", read_only=True)
    joinedHostel = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "_id",
            "name",
            "email",
            "mobile",
            "joinedHostel",
            "created_at",
            "updated_at",
        )

    def get_joinedHostel(self, obj):
        return obj.joined_hostel_dict()


class UserRegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "name", "email", "mobile", "password", "token")
        extra_kwargs = {
            "password": {"write_only": True},
            "mobile": {"write_only": True},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User already exists")
        return value

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return User.objects.create(**validated_data)

    def get_token(self, obj):
        return generate_user_token(obj.id)

    def to_representation(self, instance):
        return {
            "_id": instance.id,
            "name": instance.name,
            "email": instance.email,
            "token": generate_user_token(instance.id),
        }


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = User.objects.filter(email=attrs["email"]).first()
        if not user or not check_password(attrs["password"], user.password):
            raise serializers.ValidationError("Invalid credentials")
        attrs["user"] = user
        return attrs

    def to_representation(self, instance):
        user = instance["user"]
        return {
            "_id": user.id,
            "name": user.name,
            "mobile": user.mobile,
            "email": user.email,
            "token": generate_user_token(user.id),
        }
