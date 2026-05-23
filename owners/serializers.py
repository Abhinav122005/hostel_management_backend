import os
from datetime import datetime, timedelta, timezone

import jwt
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import serializers

from .models import Owner


def generate_owner_token(owner_id):
    payload = {
        "id": owner_id,
        "role": "owner",
        "exp": datetime.now(timezone.utc) + timedelta(days=1),
    }
    return jwt.encode(payload, os.environ.get("JWT_SECRET", "secret123"), algorithm="HS256")


def default_payu_key():
    return os.environ.get("PAYU_MERCHANT_KEY") or os.environ.get("MERCHANT_KEY")


def default_payu_salt():
    return os.environ.get("PAYU_MERCHANT_SALT") or os.environ.get("MERCHANT_SALT")


class OwnerSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id", read_only=True)
    payuKey = serializers.CharField(source="payu_key", read_only=True)
    payuSalt = serializers.CharField(source="payu_salt", read_only=True)
    createdAt = serializers.DateTimeField(source="created_at", read_only=True)

    class Meta:
        model = Owner
        fields = ("_id", "name", "email", "mobile", "payuKey", "payuSalt", "createdAt")


class OwnerRegisterSerializer(serializers.ModelSerializer):
    payuKey = serializers.CharField(required=False, allow_blank=True, write_only=True)
    payuSalt = serializers.CharField(required=False, allow_blank=True, write_only=True)

    class Meta:
        model = Owner
        fields = ("name", "email", "mobile", "password", "payuKey", "payuSalt")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):
        if Owner.objects.filter(email=value).exists():
            raise serializers.ValidationError("Owner already exists")
        return value

    def create(self, validated_data):
        payu_key = validated_data.pop("payuKey", None) or default_payu_key()
        payu_salt = validated_data.pop("payuSalt", None) or default_payu_salt()
        validated_data["password"] = make_password(validated_data["password"])
        return Owner.objects.create(
            **validated_data,
            payu_key=payu_key,
            payu_salt=payu_salt,
        )


class OwnerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        owner = Owner.objects.filter(email=attrs["email"]).first()
        if not owner:
            raise serializers.ValidationError({"message": "Owner not found"})
        if not check_password(attrs["password"], owner.password):
            raise serializers.ValidationError({"message": "Invalid credentials"})
        attrs["owner"] = owner
        return attrs
