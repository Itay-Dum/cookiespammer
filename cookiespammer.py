from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)
cookie = driver.find_element_by_id("bigCookie")

first = [driver.find_element_by_id("productPrice0"), 0]
sec = [driver.find_element_by_id("productPrice1"), 0]
third = [driver.find_element_by_id("productPrice2"), 0]
frt = [driver.find_element_by_id("productPrice3"), 0]
fth = [driver.find_element_by_id("productPrice4"), 0]
sxth = [driver.find_element_by_id("productPrice5"), 0]

cookie_count = driver.find_element_by_id("cookies")

actions = ActionChains(driver)
actions.click(cookie)
while True:
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    if first[1] <= 10 and int(first[0].text) <= count:
        print(int(first[0].text))
        print(cookie_count)
        upgrade = ActionChains(driver)
        upgrade.move_to_element(first[0])
        upgrade.click()
        upgrade.perform()
        first[1] += 1
        continue
    elif sec[1] <= 25 and int(sec[0].text) <= count:
        print(int(sec[0].text))
        print(cookie_count)
        upgrade = ActionChains(driver)
        upgrade.move_to_element(sec[0])
        upgrade.click()
        upgrade.perform()
        sec[1] += 1
        continue
    try:
        if third[1] <= 20 and int(third[0].text) <= count:
            print(int(third[0].text))
            print(cookie_count)
            upgrade = ActionChains(driver)
            upgrade.move_to_element(third[0])
            upgrade.click()
            upgrade.perform()
            third[1] += 1
            continue
    except ValueError:
        continue
    try:
        if frt[1] <= 25 and int(frt[0].text) <= count:
            print(int(third[0].text))
            print(cookie_count)
            upgrade = ActionChains(driver)
            upgrade.move_to_element(frt[0])
            upgrade.click()
            upgrade.perform()
            frt[1] += 1
    except ValueError:
        continue
    try:
        if fth[1] <= 150 and int(fth[0].text) <= count:
            print(int(fth[0].text))
            print(cookie_count)
            upgrade = ActionChains(driver)
            upgrade.move_to_element(fth[0])
            upgrade.click()
            upgrade.perform()
            fth[1] += 1
    except ValueError:
        continue