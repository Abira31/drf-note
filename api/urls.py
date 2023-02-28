from django.urls import path
from api import views

notes_list = views.NoteViewSet.as_view({
    'get':'list',
    'post':'list'
})
notes_detail = views.NoteViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'

})

urlpatterns = [
    # path('notes/',views.NoteViewSet.as_view()),
    # path('notes/<int:pk>/',views.NoteDetailView.as_view(),
    #      name=views.NoteDetailView.name),
    path('notes/',notes_list,name='notes-list'),
    path('notes/<int:pk>/',notes_detail,name='notes-detail'),
]