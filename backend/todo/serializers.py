from rest_framework import serializers
from todo.models import *
from django.forms import ValidationError


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class CreateBoardSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=300)
    creatable = serializers.BooleanField()
    done = serializers.BooleanField()

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        # fields = '__all__'
        fields = ('id', 'board_list', 'title', 'content', 'user', 'created', 'status', 'labels')

class CreateCardSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=300)
    content = serializers.CharField()
    status = serializers.CharField()
    labels = serializers.CharField()

    def validate_title(self, value):
        if len(value) < 2:
            raise ValidationError("Deve ter pelo menos três caracteres")
        return value
