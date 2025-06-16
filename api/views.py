from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PublicData, PrivateData
from .serializers import PublicDataSerializer, PrivateDataSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .tasks import send_welcome_email

User = get_user_model()

class PublicDataList(generics.ListCreateAPIView):
    queryset = PublicData.objects.all()
    serializer_class = PublicDataSerializer
    permission_classes = [permissions.AllowAny]

class PrivateDataList(generics.ListCreateAPIView):
    serializer_class = PrivateDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PrivateData.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Send welcome email via Celery
            send_welcome_email.delay(user.email, user.username)
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        
        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'username': user.username,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })