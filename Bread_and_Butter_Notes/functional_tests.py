from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_writing_a_note(self):
        # Jim has just completed the website and enters it to write the first note.
        # He notes that the title of the webpage is "BnB Notes"

        self.browser.get('http://localhost:8000')

        self.assertIn('BnB Notes', self.browser.title)
        self.fail('Jim, continue writing the functional tests.')

        # After logging
        # in he comes to the note listing page which currently has no notes on it. It does, however,
        # have a "Write New Note" button which he presses to enter the note composition page.
        #
        # Composing and Saving a Note
        # ---------------------------
        # In the note composition page Jim finds a blank area in which to compose his note. Instructions
        # printed on the page indicate that his note should be short, 1024 characters or less, counting
        # spaces and punctuation. He writes a note about building the website and his hopes for it. As
        # he writes, there is a running countdown as to how many characters he has left. When he is
        # finished composing the note he clicks on the "Submit" ("Publish", "Save"?) button to submit
        # the note. There is also a "Cancel" button that, if clicked, would leave the compostion page
        # without saving the note. Either way, Jim returns to the Note listing page with his new note
        # (if submitted) now visible.
        #


# Visiting the Website
# During development, Jim visits the website to be sure that the title includes "BnB Notes."

if __name__=='__main__':
    unittest.main(warnings='ignore')