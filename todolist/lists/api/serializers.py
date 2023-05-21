from rest_framework import serializers

from ..models import List, Task, Folder


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'completed', 'parent_list')


class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = ('title', 'tasks', 'parent_folder')


class FolderSerializer(serializers.ModelSerializer):
    lists = ListSerializer(many=True, read_only=True)

    class Meta:
        model = Folder
        fields = ('title', 'lists')
