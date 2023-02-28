from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .serializers import NoteSerializer,ThinNoteSerializer

from notes.models import Note
# @api_view(['GET','POST'])
# def notes_list(request):
#     if request.method == 'GET':
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class NoteListAPIView(APIView):
#     def get(self,request):
#         context = {'request': request}
#         notes = Note.objects.all()
#         serializer = ThinNoteSerializer(notes,many=True,context=context)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class NoteListView(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    GenericAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#     def get(self,request,*args,**kwargs):
#         self.serializer_class = ThinNoteSerializer
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class NoteListView(ListCreateAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#     def list(self, request, *args, **kwargs):
#         notes = Note.objects.all()
#         context = {'request': request}
#         serializer = ThinNoteSerializer(notes,many=True,context=context)
#         return Response(serializer.data,status=status.HTTP_200_OK)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    def list(self, request, *args, **kwargs):
        notes = Note.objects.all()
        context = {'request': request}
        serializer = ThinNoteSerializer(notes,many=True,context=context)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



# @api_view(['GET','PUT','DELETE'])
# def note(request:HttpRequest,pk):
#     try:
#         note = Note.objects.get(pk=pk)
#     except None.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = NoteSerializer(note)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = NoteSerializer(note,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class NoteDetailView(APIView):
#     name = 'notes-detail'
#     def get_object(self,pk):
#         try:
#             note = Note.objects.get(pk=pk)
#             return note
#         except None.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     def get(self,request,pk):
#         note = self.get_object(pk=pk)
#         serializer = NoteSerializer(note)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def put(self,request,pk):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         note = self.get_object(pk)
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class NoteDetailView(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      GenericAPIView):
#     name = 'notes-detail'
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

# class NoteDetailView(RetrieveUpdateDestroyAPIView):
#     name = 'notes-detail'
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer