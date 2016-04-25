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

        # The header on the page says "Bread and Butter Notes"

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Bread and Butter Notes', header_text)

        # After logging in
        #
        # **** Create a test for this once you know how ****
        #
        # he comes to the note listing page which currently has no notes on it. It does, however,
        # have a "Write New Note" button . . . which he presses to enter the note composition page.

        # new_note_button = self.browser.find_element_by_id('id_new_note_button')
        # self.assertEqual(
        #     new_note_button.text, "Write New Note"
        # )
        #
        # Jim presses the Write New Note button to enter the note composition page.
        # new_note_button.click()
        # create_note_header_text = self.browser.find_element_by_tag_name('h2').text
        # self.assertIn('Create or Edit your Note Below:', create_note_header_text, "Failed to find Create Note Form Header")

        # Do the above once you know how.  For now, I am following Test Driven Development in Python Chapter 4 & 5

        # Jim is invited to enter a new note right away
        inputbox = self.browser.find_element_by_id('id_new_note')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Type a new note'
        )

        # He types "This is my first note." into a text box
        inputbox.send_keys('This is my first note.')

        # When he hits Enter, the page updates, and now the page lists
        # "This is my first note."
        note_list = self.browser.find_element_by_id('id_note_list')
        notes = note_list.find_elements_by_tag_name('li')
        self.assertTrue(
            any(note.text == 'This is my first note.' for note in notes),
            "New note did not appear in list."
        )

        self.fail('Jim, continue writing the functional tests!')
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