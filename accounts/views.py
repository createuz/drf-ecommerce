from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

from .models import User
from .serializers import UserSerializer, LoginSerializer


class RegisterView(APIView):
    def get(self, request):
        products = User.objects.all()
        products_data = UserSerializer(products, many=True)
        return Response(products_data.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': '🟢 User registered successfully.'}, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                return Response({'message': '🟢 Login successful.'}, status=200)
            else:
                return Response({'message': '🔴 Invalid credentials.'}, status=401)
        else:
            return Response(serializer.errors, status=400)