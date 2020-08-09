from djoser.serializers import UserSerializer
from rest_framework import serializers

from api.models import List, Task


class FilterListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    list = serializers.SlugRelatedField('name', read_only=True)
    parent = serializers.SlugRelatedField('name', read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    list = serializers.SlugRelatedField('name', read_only=True)
    parent = serializers.SlugRelatedField('name', read_only=True)
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterListSerializer
        model = Task
        fields = '__all__'


class ListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        exclude = ['is_default']


class ListListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField('username', read_only=True)

    class Meta:
        model = List
        exclude = ['is_default']


class ListDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    tasks = TaskDetailSerializer(many=True, read_only=True)

    class Meta:
        list_serializer_class = FilterListSerializer
        model = List
        exclude = ['is_default']
