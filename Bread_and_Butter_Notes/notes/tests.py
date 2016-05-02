from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.template import RequestContext

from notes.views import note_list
from notes.models import Note

class NoteListTest(TestCase):

    def test_root_url_resolves_to_note_list_view(self):
        found = resolve('/')
        self.assertEqual(found.func, note_list)

    def test_note_list_view_returns_correct_html(self):
        request = HttpRequest()
        response = note_list(request)
        expected_html = render_to_string('note_list.html', RequestContext(request))
        self.assertEqual(response.content.decode(), expected_html)

    def test_note_list_view_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['note_text'] = 'A new note'

        response = note_list(request)

        self.assertIn('A new note', response.content.decode())
        expected_html = render_to_string(
            'note_list.html',
            RequestContext(request, {'new_note_text': 'A new note'})
        )
        self.assertEqual(response.content.decode(), expected_html)

class NoteModelTest(TestCase):

    def test_saving_and_retrieving_notes(self):
        first_note = Note()
        first_note.contents = 'This could be my first note.'
        first_note.save()

        second_note = Note()
        second_note.contents = 'This could be the note written after the first note.'
        second_note.save()

        saved_notes = Note.objects.all()
        self.assertEqual(saved_notes.count(), 2)

        first_saved_note = saved_notes[0]
        second_saved_note = saved_notes[1]
        self.assertEqual(first_saved_note.contents, 'This could be my first note.')
        self.assertEqual(second_saved_note.contents, 'This could be the note written after the first note.')
