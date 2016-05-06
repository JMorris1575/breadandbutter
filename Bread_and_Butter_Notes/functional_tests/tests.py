from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_note_in_list(self, note_text):
        note_list = self.browser.find_element_by_id('id_note_list')
        notes = note_list.find_elements_by_tag_name('li')
        self.assertIn(note_text, [note.text for note in notes])

    def test_writing_a_note_and_retrieve_it_later(self):
        # Jim has just completed the website and enters it to write the first note.

        # Although he simply enters the root url of the website, he is redirected to the note display page
        # which has a url of <root>/note/
        self.browser.get(self.live_server_url)
        home_url = self.browser.current_url
        self.assertRegex(home_url, '/notes/')

        # He notes that the title of the webpage is "BnB Notes"

        #self.browser.get(self.live_server_url)

        self.assertIn('BnB Notes', self.browser.title)

        # and that the header on the page says "Bread and Butter Notes"

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
        inputbox.send_keys(Keys.ENTER)

        # When he hits Enter, the page updates, and now the page lists
        # "This is my first note."
        self.check_for_note_in_list('This is my first note.')

        # Just for fun, Jim decides to add another note, and now the page
        # lists both of the notes
        inputbox = self.browser.find_element_by_id('id_new_note')
        inputbox.send_keys('This is a second note added just for fun.')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_note_in_list('This is my first note.')
        self.check_for_note_in_list('This is a second note added just for fun.')

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
