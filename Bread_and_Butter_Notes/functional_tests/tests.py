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

        # a smaller heading says that this is the Note List page
        subheading = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Note List:', subheading)

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

        # Jim notices a button marked 'Add New Note'
        new_note_button = self.browser.find_element_by_id('id_new_note_button')
        self.assertIn(
            new_note_button.text,
            'Write New Note'
        )

        # when he clicks the button he is transferred to a new page
        # where he can write a new note
        new_note_button.click()
        subheading = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Add a Note:', subheading)

        # where he is invited to enter a new note
        # into a textbox
        inputbox = self.browser.find_element_by_id('id_new_note_box')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Type a new note here.'
        )

        # He types "This is my first note." into the text box
        inputbox.send_keys('This is my first note.')
        inputbox.send_keys(Keys.ENTER)

        # When he hits Enter, he is returned to the note list page which now lists
        # "This is my first note."
        self.check_for_note_in_list('This is my first note.')

        # Just for fun, Jim decides to add another note,
        new_note_button = self.browser.find_element_by_id('id_new_note_button')
        new_note_button.click()
        inputbox = self.browser.find_element_by_id('id_new_note_box')
        inputbox.send_keys('This is a second note added just for fun.')
        inputbox.send_keys(Keys.ENTER)

        # and now the note list page
        # lists both of the notes
        self.check_for_note_in_list('This is my first note.')
        self.check_for_note_in_list('This is a second note added just for fun.')

        # Jim leaves the website to see if his notes will remain when he returns.
        # When he returns to the website he is happy to see his two notes are still there
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

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
