from django.shortcuts import redirect, render
from notes.models import Note

def home_page(request):
    return redirect('/notes/')

def note_list(request):
    if request.method == 'POST':
        Note.objects.create(contents=request.POST['note_text'])
        return redirect('/notes/')

    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})
