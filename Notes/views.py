from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Note
from django.utils import timezone


def get_notes(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        return render(request, 'note_list.html', {'notes': notes})

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            note = Note(title=title, content=content)
            note.save()
        return redirect('get_notes')

    if request.method == 'DELETE':
        Note.objects.all().delete()
        return redirect('get_notes')  
    

def get_note_by_id(request, note_id):
    note = get_object_or_404(Note, note_id=note_id) 
    return render(request, 'note_detail.html', {'note': note})


def delete_note_by_id(request, note_id):
    note = get_object_or_404(Note, note_id=note_id)  
    if request.method == 'DELETE':
        note.delete()
    return redirect('get_notes')

def update_note(request, note_id):
    note = get_object_or_404(Note, note_id=note_id)

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        note.title = title
        note.content = content
        note.save()
        
        return redirect('get_note_by_id', note_id=note.note_id)

    return render(request, 'note_form.html', {'note': note})