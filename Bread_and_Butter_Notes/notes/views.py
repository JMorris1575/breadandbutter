from django.shortcuts import redirect, render
from notes.models import Note

def note_list(request):
    if request.method == 'POST':
        Note.objects.create(contents=request.POST['note_text'])
        return redirect('/')

    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})
