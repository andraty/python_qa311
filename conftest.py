import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture() # fixture позволяет что-то делать до начала теста и после того как тест закончиться
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.set_window_size(1920,1080)
    yield driver # все что до yeld будет выполняться вначале теста, а посел как тест закончится выполниться driver.quit()
    driver.close()

