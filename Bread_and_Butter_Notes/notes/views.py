from django.http import HttpResponse
from django.shortcuts import render

def note_list(request):
    return render(request, 'note_list.html', {
        'new_note_text': request.POST.get('note_text', ''),
    })
