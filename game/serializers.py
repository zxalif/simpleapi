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


class ThreadImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ThreadImage
        fields = ['image', ]


class BasicGameSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('name',)


class ThreadImageRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        return '%s' % (value.image.url)


class ThreadSerializer(serializers.ModelSerializer):

    thread_image = ThreadImageRelatedField(read_only=True, many=True)

    class Meta:
        model = Thread
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    thread = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('id',)

    def get_thread(self, obj):
        data = Thread.objects.filter(game__id=obj.id)
        return ThreadSerializer(data, many=True).data
