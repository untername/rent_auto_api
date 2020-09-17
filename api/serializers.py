from rest_framework import serializers
from .models import Auto, Renter
from typing import Type, Tuple


class AutoSerializer(serializers.HyperlinkedModelSerializer):

    """ Сериализатор для моделей авто, включающий в представление всех арендаторов. """

    drivers = serializers.HyperlinkedRelatedField(queryset=Renter.objects.all(), many=True, view_name='renter-detail')

    class Meta:
        model: Type[Auto] = Auto
        fields: Tuple = ('url', 'id', 'drivers', 'auto_name', 'year', 'created_at')


class RenterSerializer(serializers.HyperlinkedModelSerializer):

    """ Сериализатор для моделей арендаторов. Создает список арендованных авто для каждого арендатора. """
    
    cars = AutoSerializer(many=True, read_only=True)

    class Meta:
        model: Type[Renter] = Renter
        fields: Tuple = ('url', 'id', 'name', 'email', 'language', 'cars')
