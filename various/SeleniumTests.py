import unittest
from selenium import webdriver

class RunTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_openGoogle(self):
        self.browser.get('http://www.google.co.uk/')
        self.browser.find_element_by_name('q')

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()