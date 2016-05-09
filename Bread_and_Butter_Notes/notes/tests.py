from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.template import RequestContext

from notes.views import create_note, home_page, note_list
from notes.models import Note

class NoteListTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_root_url_redirects_to_note_list_view(self):
        request = HttpRequest()
        request.method = 'GET'
        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/notes/')

    def test_note_list_view_returns_correct_html(self):
        request = HttpRequest()
        response = note_list(request)
        expected_html = render_to_string('note_list.html', RequestContext(request))
        self.assertEqual(response.content.decode(), expected_html)

    # def test_note_list_view_can_save_a_POST_request(self):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['note_text'] = 'A new note'
    #
    #     response = note_list(request)
    #
    #     self.assertEqual(Note.objects.count(), 1)
    #     new_note = Note.objects.first()
    #     self.assertEqual(new_note.contents, 'A new note')

    # def test_create_note_page_returns_to_note_list_after_POST(self):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['note_text'] = 'A new note'
    #
    #     response = create_note(request)
    #
    #     self.assertIn('Note List:', str(response.content))

    def test_note_list_only_saves_items_when_necessary(self):
        request = HttpRequest()
        note_list(request)
        self.assertEqual(Note.objects.count(), 0)

    def test_can_connect_to_create_note_view(self):
        request = HttpRequest()
        response = create_note(request)

        self.assertIn('Add a Note:', str(response.content))

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


class NoteViewTest(TestCase):

    def test_displays_all_notes(self):
        Note.objects.create(contents='Hi Jim!')
        Note.objects.create(contents='How are you?')

        response = self.client.get('/notes/')

        self.assertContains(response, 'Hi Jim!')
        self.assertContains(response, 'How are you?')

class NewNoteTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/notes/create',
            data={'note_text': 'A new note'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_note = Item.objects.first()
        self.assertEqual(new_note.text, 'A new note')

    def test_create_note_returns_to_note_list_after_POST(self):
        response = self.client.post(
            '/notes/create',
            data={'note_text': 'A new note'}
        )
        self.assertTemplateUsed(response, 'note_list.html')

