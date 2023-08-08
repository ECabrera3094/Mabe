import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.selenium_manager import SeleniumManager
from webdriver_manager.chrome import ChromeDriverManager

from TestCases.TC_13 import TC_13

class Mabe(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome() # version="114.0.5735.16"

    def test_Mabe(self):
        driver = self.driver
        tc_13 = TC_13(driver)
        tc_13.start()
 
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()