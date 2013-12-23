import unittest
import time
from selenium import webdriver


class RunTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    # @unittest.skip
    def test_openGoogle(self):
        self.browser.get('http://www.google.co.uk/')
        self.browser.find_element_by_name('q')
        self.browser.close()

    def test_searchEbay(self):
        self.browser.get('http://www.ebay.co.uk')
        self.browser.find_element_by_id('gh-ac').send_keys('mac book pro 15')
        self.browser.find_element_by_id('gh-btn').click()

        X = self.browser.find_element_by_id('ResultSetItems')
        img_elements = X.find_elements_by_class_name('img')
        all_links = [alink.get_attribute('href') for alink in img_elements if alink.tag_name == 'a']
        for link in all_links:
            print(link)
            self.browser.get(link)
            time.sleep(1)
        self.browser.close()

    def tearDown(self):
        self.browser.close()
        self.browser.stop_client()


if __name__ == '__main__':
    unittest.main()