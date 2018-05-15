
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

		#updates and lists her item in a list
		inputbox.send_keys(Keys.ENTER)
		import time
		time.sleep(10)
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')

		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])


		#she is invited to add another, page repdates
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Buy pacock feathers', [row.text for row in rows])
		self.assertIn(
			'2: Use peacock feathers to make a fly' ,
			[row.text for row in rows]
		)
		
		#user wants to remember the list, then sees site has 
		#generated unique url

		#user visits list

		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')

browser.quit()

