from rest_framework import serializers
from notes.models import Note

# class NoteSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True,max_length=250)
#     text = serializers.CharField(required=False,allow_blank=True)
#     def create(self, validated_data:dict):
#         return Note.objects.create(**validated_data)
#     def update(self, instance:Note, validated_data:dict):
#         instance.title = validated_data.get('title',instance.title)
#         instance.text = validated_data.get('text',instance.text)
#         instance.save()
#         return instance

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
