from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

from django.contrib.auth.models import User
# from .serializers import *

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class EventView(generics.CreateAPIView):
    queryset = Events.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = EventSerializer
    # def get(self, reqjest):
    #     serializer = self.serializer_class(self.queryset, many=True)
    #     return Response(serializer.data, safe=False)
    def post(self, validated_data):
        event = Events.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            date=validated_data['date'],
            time=validated_data['time'],
            location=validated_data['location'],
            capacity=validated_data['capacity'],
            category=validated_data['category']
        )
        event.save()
        return event

class VenueViewSet(generics.CreateAPIView):
    queryset = Venue.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = VenueSerializer

class RegistrationViewSet(generics.CreateAPIView):
    queryset = Registration.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer