from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Registration
from .serialize import EventSerializer, RegistrationSerializer
# Create your views here.
@api_view(['POST'])
def create_event(request):
    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def list_event(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def retrieve_event(request,pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventSerializer(event)
    return Response(serializer.data)

@api_view(['PUT','PATCH'])
def update_event(request,pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventSerializer(event, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_event(request,pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({"detail": "Event does not exist."}, status=status.HTTP_404_NOT_FOUND)
    
    event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_registration(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def list_registration(request):
    registrations = Registration.objects.all()
    serializer = RegistrationSerializer(registrations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def retrieve_registration(request,pk):
    try:
        registration = Registration.objects.get(pk=pk)
    except Registration.DoesNotExist:
        return Response({"detail": "Registration not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RegistrationSerializer(registration)
    return Response(serializer.data)

@api_view(['PUT','PATCH'])
def update_registration(request,pk):
    try:
        registration = Registration.objects.get(pk=pk)
    except Registration.DoesNotExist:
        return Response({"detail": "Registration not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RegistrationSerializer(registration, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_registration(request,pk):
    try:
        registration = Registration.objects.get(pk=pk)
    except Registration.DoesNotExist:
        return Response({"detail": "Registration does not exist."}, status=status.HTTP_404_NOT_FOUND)
    
    registration.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)