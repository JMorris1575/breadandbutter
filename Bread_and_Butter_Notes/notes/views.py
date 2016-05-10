from django.shortcuts import redirect, render
from notes.models import Note


def add_note(request):
    Note.objects.create(contents=request.POST['note_text'])
    return redirect('/notes/')

def home_page(request):
    return redirect('/notes/')

def create_note(request):
    return render(request, 'create_note.html')

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})
