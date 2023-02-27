from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers import NoteSerializer

from notes.models import Note
@api_view(['GET','POST'])
def notes_list(request:HttpRequest):
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = NoteSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def note(request:HttpRequest,pk):
    try:
        note = Note.objects.get(pk=pk)
    except None.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = NoteSerializer(note,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





