from dataclasses import field
from rest_framework.serializers import ModelSerializer, EmailField, CharField, SerializerMethodField
from rest_framework.validators import UniqueValidator

from base.models import Event, Seat
from django.contrib.auth.models import User



class EventSerializer(ModelSerializer):
    class Meta:
        model =  Event
        fields = '__all__'


class EventSeatSerializer(ModelSerializer):
    event = SerializerMethodField()
    seat = SerializerMethodField()
    def get_seat(self,obj):
        eventObj = EventSeatSerializer(instance=obj.event_id)
        return eventObj.data
    class Meta:
        model = Event



class SeatSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class UserSerializer(ModelSerializer):
    email = EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = CharField(max_length=32,  validators=[UniqueValidator(queryset=User.objects.all())])
    password = CharField(min_length=8,write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],validated_data['password'])


        return user
    class Meta:
        model = User
        fields = ('id', 'username','email', 'password')

