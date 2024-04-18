# Подключение библиотек
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path=r"C:\Users\ADMIN\PycharmProjects\qa\pythonProject1\chrome_driver\chromedriver.exe")
option = webdriver.ChromeOptions()
# юзер агент
# option.add_argument("--user-agent=AAAAAAA")
# проверка на робота
# option.add_argument("--disable-blink-features=AutomationControlled")
# режим инкогнито
# option.add_argument("--incognito")
# размеры окна
# option.add_argument("--window-size=1920,1080")
# игнорирование ssl сертификатов
# option.add_argument("--ignore-certificate-errors")
# стратегия загрузки страницы normal / eager
# option.page_load_strategy = 'normal'
# option.page_load_strategy = 'eager'

prefs = {
    "download.default_directory": fr"{os.getcwd()}\download"
}
option.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=service, options=option)

url = "https://the-internet.herokuapp.com/download"

driver.get(url)
time.sleep(5)
driver.find_elements("xpath", "//a")[2].click()
time.sleep(5)

driver.close()

