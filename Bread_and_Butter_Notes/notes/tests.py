from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from notes.views import note_list

class NoteListTest(TestCase):

    def test_root_url_resolves_to_note_list_view(self):
        found = resolve('/')
        self.assertEqual(found.func, note_list)

    def test_note_list_view_returns_correct_html(self):
        request = HttpRequest()
        response = note_list(request)
        expected_html = render_to_string('note_list.html')
        print('exptected_html = ', expected_html)
        self.assertEqual(response.content.decode(), expected_html)
