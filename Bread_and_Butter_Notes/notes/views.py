from django.shortcuts import render
from notes.models import Note

def note_list(request):
    if request.method == 'POST':
        new_note_contents = request.POST['note_text']
        Note.objects.create(contents=new_note_contents)
    else:
        new_note_contents = ''

    return render(request, 'note_list.html', {
        'new_note_contents': new_note_contents
    })
