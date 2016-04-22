from django.shortcuts import render
from django.http import HttpResponse

def note_list(request):
    print('Got to note_list view')
    return HttpResponse('<html><title>BnB Notes</title></html>')
