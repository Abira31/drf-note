from django.urls import path
from api import views

urlpatterns = [
    path('notes/',views.notes_list),
    path('notes/<int:pk>/',views.note),
]