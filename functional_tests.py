
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)	
	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		row = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])




	def test_can_start_a_list_and_retrieve_it_later(self):
		#user goes to website
		self.browser.get('http://localhost:8000')

		#user sees title of 'to-do' list
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#she is prompted to start a list
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
				'Enter a to-do item'
		)

		#she types an item into teext box and hits enter, page 
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		#updates and lists her item in a list
		import time
		time.sleep(10)
		table = self.browser.find_element_by_id('id_list_table')
		row = table.find_elements_by_tag_name('tr')
		
		#she is invited to add another, page repdates
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		
		#user wants to remember the list, then sees site has 
		#generated unique url

		#user visits list

		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')

browser.quit()

