from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("Chromium.exe path")
driver = webdriver.Chrome(service=s)
driver.get("https://orteil.dashnet.org/cookieclicker/")


def buy_upgrade():
    available_upgrades = driver.find_elements(By.CSS_SELECTOR, '.enabled .price')
    max_price = 0
    selected_upgrade = 0
    for upgrade in available_upgrades:
        if int(upgrade.text) > max_price:
            max_price = int(upgrade.text)
            selected_upgrade = upgrade
    driver.execute_script("arguments[0].click();", selected_upgrade)


five_min = time.time() + 60*5
timeout = time.time() + 5
cookie = driver.find_element(By.ID, 'bigCookie')

while True:
    cookie.click()
    if time.time() > timeout:
        timeout += 5
        buy_upgrade()
    if time.time() > five_min:
        print(driver.find_element(By.ID, 'cookies').text)




