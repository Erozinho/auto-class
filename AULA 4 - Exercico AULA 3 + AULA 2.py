from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service('C:\\Users\\felaraujo\\Downloads\\chromedriver.exe')


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
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def clean_text(text):
    """Extrair o valor exato de temperatura"""
    output = float(text.split(": ")[1])
    return output


def main():
    """Função principal"""
    driver = get_driver()
    driver.find_element(By.ID, "id_username").send_keys("automated")
    sleep(2)
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" +
    Keys.RETURN)
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    sleep(2)
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
    print(driver.current_url)
    return clean_text(element.text)



print(main())
