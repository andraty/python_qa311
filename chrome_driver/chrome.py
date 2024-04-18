# Подключение библиотек
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path=r"C:\Users\ADMIN\PycharmProjects\qa\pythonProject1\chrome_driver\chromedriver.exe")
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


url = "https://tutorialsninja.com/demo/"

try:
    driver.get(url)
    time.sleep(3)

    add_to_cart_iphone = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div/div[3]/button[1]")
    add_to_cart_iphone.click()
    time.sleep(5)

    driver.refresh()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()




