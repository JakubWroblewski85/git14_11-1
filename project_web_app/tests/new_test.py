import unittest
from selenium import webdriver
from pages.home_page import HomePage
from tests.test_data import TestData
from selenium.webdriver.chrome.options import Options

class NewTest(unittest.TestCase):
    '''
    base clas for each test
    '''

    def setUp(self):
    	# for jenkins
    	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	self.driver = webdriver.Chrome('/home/<user>/chromedriver',chrome_options=chrome_options)
	
        # 1. Z otwartą przeglądarką
        # self.driver = webdriver.Chrome()
        # do jenkinsa
        # self.driver = webdriver.Firefox()
        # self.driver.maximize_window()

        # 2. Przeglądarka działa w tle (czyli przeglądarka się nie odpali) a testy idą normalnie.
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        # self.driver = webdriver.Chrome(chrome_options=options)

        self.driver.get('http://automationpractice.com/')
        self.driver.implicitly_wait(10)
        self.home_page = HomePage(self.driver)
        self.test_data = TestData()

    def tearDown(self):
        self.driver.quit()
