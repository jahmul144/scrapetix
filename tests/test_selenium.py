#First Test of Seleniumi
import unittest
from selenium import webdriver
from pyvirtualdisplay import Display

class SearchTest(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.driver = webdriver.Chrome(executable_path="/home/ubuntu/Downloads/chromedriver")
        
    
    def test_titleload(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        
    def tearDown(self):
        self.driver.quit()
        self.display.stop()

if __name__ == "__main__":
    unittest.main()
