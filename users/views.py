from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserLoginSerializer, UserRegisterSerializer, UserSerializer


@api_view(["POST"])
def register_user(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(UserRegisterSerializer(user).data, status=status.HTTP_201_CREATED)

    if "email" in serializer.errors:
        return Response({"message": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_user_by_id(request, user_id):
    user = User.objects.filter(id=user_id).first()
    if not user:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response(
        {
            "user": UserSerializer(user).data,
            "joinedHostel": user.joined_hostel_dict(),
            "transactions": [],
            "count": 0,
        },
        status=status.HTTP_200_OK,
    )
