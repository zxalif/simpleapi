from rest_framework import serializers

from .models import (
    Category,
    Game,
    Thread,
    ThreadImage
)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id',)


class GameSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('id',)


class BasicGameSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('name',)
