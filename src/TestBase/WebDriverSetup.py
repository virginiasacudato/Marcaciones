import unittest
from selenium import webdriver
import urllib3
import os
from os.path import join, dirname
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/Marcaciones/.env')
load_dotenv(dotenv_path)

# Environment Variables
URL = os.getenv('URL_BASE')
USER = os.getenv('USER_TEST')
PASSWORD = os.getenv('PASSWORD_TEST')


# Run python -m pytest --html=report-unido.html --self-contained-html

class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(URL)
        self.driver.find_element(By.ID, 'Usuario').send_keys(USER)
        self.driver.find_element(By.ID, 'password').send_keys(PASSWORD)
        self.driver.find_element(By.ID, 'btnIngresar').click()
