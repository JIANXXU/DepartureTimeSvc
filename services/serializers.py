from django.forms import widgets
from rest_framework import serializers
from services.models import DepartureTime


class DepartureTimeSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    agencyName = serializers.CharField(required=False,
                                  max_length=100)
    routeName = serializers.CharField(required=False,
                                  max_length=100)
    stopName = serializers.CharField(required=False,
                                  max_length=100)    
    stopCode = serializers.IntegerField(required=False)
    nextDepartureTime = serializers.IntegerField(required = False)
    latitude = serializers.FloatField(required = True)
    longitude = serializers.FloatField(required = True)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new DepartureTime instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.agencyName = attrs.get('agencyName', instance.agencyName)
            instance.routeName = attrs.get('routeName', instance.routeName)
            instance.stopName = attrs.get('stopName', instance.stopName)
            instance.stopCode = attrs.get('stopCode', instance.stopCode)
            instance.nextDepartureTime = attrs.get('nextDepartureTime', instance.nextDepartureTime)
            instance.latitude = attrs.get('latitude', instance.latitude)
            instance.longitude = attrs.get('longitude', instance.longitude)
            return instance

        # Create new instance
        return DepartureTime(**attrs)