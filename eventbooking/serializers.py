from rest_framework import serializers
from .models import EventBooking

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBooking
        fields = '__all__'
