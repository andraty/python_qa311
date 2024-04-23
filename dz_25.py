import selenium
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def test_title():
    driver.get("https://www.saucedemo.com/")
    title = driver.title
    assert title == "lkbpiu7gpi"

