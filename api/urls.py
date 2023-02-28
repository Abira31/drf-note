from django.urls import path
from api import views

urlpatterns = [
    path('notes/',views.NoteListAPIView.as_view()),
    path('notes/<int:pk>/',views.NoteDetailView.as_view(),
         name=views.NoteDetailView.name),
]