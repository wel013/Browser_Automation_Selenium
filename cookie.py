from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:/Development/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
url = 'http://orteil.dashnet.org/experiments/cookie/'
driver.get(url)
ON = True
timeout = time.time() + 5
five_min = time.time() + 300


indexx = 1

cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
while True:

    cookie.click()
    current = driver.find_element(By.ID, "money").text
    crr_money = int(current.replace(",", ""))
    if time.time() > timeout:
        price_list = []
        prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        range1 = len(prices) - 1
        for n in range(range1):
            index = len(prices[n].text.split()) - 1
            num_str = prices[n].text.split()[index].replace(",", "")
            num = num_str.strip()
            price_list.append(int(num))

        for n in range(range1):
            if crr_money > price_list[n]:
                 idx = price_list.index(price_list[n])
                 indexx = idx
            else:
                pass

        to_buy = item_ids[indexx]


        driver.find_element(by=By.ID, value=to_buy).click()
        timeout = time.time() + 5

    if time.time() > five_min:
            cookie_per_s = driver.find_element(by=By.ID, value="cps").text
            print(cookie_per_s)
            break

driver.quit()





