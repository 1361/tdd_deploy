from selenium import webdriver
import unittest
browser = webdriver.Firefox()

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)	
	def tearDown(self):
		self.browser.quit()
	def test_can_start_a_list_and_retrieve_it_later(self):
		#user goes to website
		self.browser.get('http://localhost:8000')

		#user sees title of 'to-do' list
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!') 

		#she is prompted to start a list

		#she types an item into teext box and hits enter, page 
		#updates and lists her item in a list

		#she is invited to add another, page repdates


		#user wants to remember the list, then sees site has 
		#generated unique url

		#user visits list
if __name__ == '__main__':
	unittest.main(warnings='ignore')

browser.quit()

