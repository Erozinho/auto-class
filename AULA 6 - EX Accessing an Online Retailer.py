from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

user = os.path.expanduser('~')
service = Service(user+'\\Downloads\\chromedriver.exe')


def get_driver():
    """Opções para facilitar o acesso"""
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://titan22.com")
    return driver


def main():
    """Função principal"""
    driver = get_driver()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="shopify-section-header"]/div[1]/div/div[3]/a[2]').click()
    sleep(1)
    driver.find_element(By.ID, "CustomerEmail").send_keys("testeemail@gmail.com")
    sleep(1)
    driver.find_element(By.ID, "CustomerPassword").send_keys("teste@123"+Keys.RETURN)
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]").click()
    sleep(2)
    element = driver.find_element(By.XPATH, '//*[@id="shopify-section-page-contact-us"]/section/div/h1')
    return element.text


print(main())
