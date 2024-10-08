from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_notes ), 
    path('notes/', views.get_notes, name='get_notes'),  
    path('note/<int:note_id>/', views.get_note_by_id, name='get_note_by_id'),  
    path('note/<int:note_id>/delete/', views.delete_note_by_id, name='delete_note_by_id'),  
    path('note/<int:note_id>/update/', views.update_note, name='update_note'),  
]