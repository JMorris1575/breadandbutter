from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from notes.views import note_list

class NoteListTest(TestCase):

    def test_root_url_resolves_to_note_list_view(self):
        found = resolve('/')
        self.assertEqual(found.func, note_list)

    def test_note_list_view_returns_correct_html(self):
        request = HttpRequest()
        response = note_list(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>BnB Notes</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

