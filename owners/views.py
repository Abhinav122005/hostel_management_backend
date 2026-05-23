from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Owner
from .serializers import (
    OwnerLoginSerializer,
    OwnerRegisterSerializer,
    OwnerSerializer,
    generate_owner_token,
)


@api_view(["POST"])
def register_owner(request):
    serializer = OwnerRegisterSerializer(data=request.data)
    if serializer.is_valid():
        owner = serializer.save()
        return Response(
            {
                "message": "Owner registered successfully",
                "owner": OwnerSerializer(owner).data,
            },
            status=status.HTTP_201_CREATED,
        )

    if "email" in serializer.errors:
        return Response({"message": "Owner already exists"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_owner(request):
    serializer = OwnerLoginSerializer(data=request.data)
    if not serializer.is_valid():
        detail = serializer.errors.get("non_field_errors")
        if detail:
            message = serializer.errors["non_field_errors"][0]
            if isinstance(message, dict):
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

    owner = serializer.validated_data["owner"]
    return Response(
        {
            "message": "Login successful",
            "token": generate_owner_token(owner.id),
            "owner": OwnerSerializer(owner).data,
        },
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
def verify_payu(request, owner_id):
    owner = Owner.objects.filter(id=owner_id).first()
    if not owner:
        return Response({"message": "Owner not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response(
        {
            "merchantKey": owner.payu_key,
            "merchantSalt": owner.payu_salt,
        },
        status=status.HTTP_200_OK,
    )
