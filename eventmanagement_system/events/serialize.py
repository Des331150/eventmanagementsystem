from rest_framework import serializers
from .models import Event, Registration

class EventSerializer(serializers.ModelSerializer):
    """
    Serializer representing an event with its details like title,description,location and timing.
    """
    class Meta:
        model = Event
        fields = ["title", "description", "location","start_date", "end_date",]

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer representing a user's registration to a specific event, including personal contact details.
    """
    class Meta:
        model = Registration
        fields = ["full_name", "email", "phone_number","registered_at"]