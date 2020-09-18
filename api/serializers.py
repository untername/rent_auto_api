from rest_framework import serializers
from .models import Auto, Renter, UpdatedUser
from typing import Type, Tuple, Dict


class UserSerializer(serializers.ModelSerializer):

    """ Сериализатор пользователя """

    def create(self, validated_data) -> UpdatedUser:
        user = UpdatedUser(
            email=validated_data['email'],
            username=validated_data['username'])

        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model: Type[UpdatedUser] = UpdatedUser
        fields: str = "__all__"
        extra_kwargs: Dict = {'password': {'write_only': True}}


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
