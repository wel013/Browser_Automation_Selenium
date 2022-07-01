#This programs performs the process of opening tinder.com, logging with FB, 
# accept conditions and cookies, like/dislike people (based on your choice)

url = "https://tinder.com/"
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException
count = 0
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:/Development/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
driver.get(url)
#Signing in on the main page
time.sleep(3)
signin_btn = driver.find_element(by=By.XPATH, value='//*[@id="q-996647900"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
signin_btn.click()
time.sleep(3)
fb_log_in = driver.find_element(by=By.XPATH, value='//*[@id="q1569938320"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_log_in.click()


#Signing in with FB on a pop up window
FB_EMAIL = "wenqianli010524@gmail.com"
FB_PASSWORD = os.environ['FB_PASSWORD']
time.sleep(2)

driver.window_handles
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
email = driver.find_element(by=By.ID, value='email')
email.send_keys(FB_EMAIL)
driver.switch_to.window(fb_login_window)
password = driver.find_element(by=By.ID, value="pass")
password.send_keys(FB_PASSWORD)


fb_log = driver.find_element(by=By.CSS_SELECTOR, value='label input')
fb_log.click()
time.sleep(3)

#switch back to the main page to perform actions: allow conditions/cookies
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)
allow = driver.find_element(by=By.XPATH, value='//*[@id="q1569938320"]/div/div/div/div/div[3]/button[1]')
allow.click()
time.sleep(5)

not_int = driver.find_element(by=By.XPATH, value='//*[@id="q1569938320"]/div/div/div/div/div[3]/button[2]')
not_int.click()
time.sleep(5)

accept = driver.find_element(by=By.XPATH, value='//*[@id="q-996647900"]/div/div[2]/div/div/div[1]/div[1]/button')
accept.click()

# #just disliking everyone
# dislike = driver.find_element(by=By.XPATH, value='//*[@id="q-996647900"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
# for n in range(100):
#     # how many can you dislike? I'll do 100 too
#     time.sleep(2)
#     # wait 2 sec after each dislike so that I dont look like a bot (but I am)
#     dislike.click()

# now liking everyone
for n in range(100):
    time.sleep(2)
    #but for sure you only have 100 "Likes"
    # try:
    #     close_notes = driver.find_element(by=By.CSS_SELECTOR, value="#q1569938320 button")
    #     close_notes.click()
    #     time.lksleep(3)
    # except ElementClickInterceptedException:
    #     print("shit is prob broker=n notes shit")
    try:
        #like_btn = driver.find_element(by=By.CSS_SELECTOR, value='#q-996647900 main button')
        # like_btn.click()
        # print("liked")
        #for some reason my like button says exception everytime it's abrout to be pressed
        body = driver.find_element(By.CSS_SELECTOR, "body")
        body.send_keys(Keys.ARROW_RIGHT)
    except StaleElementReferenceException:
        # I nevered encountered a match so I took the code from the solution
        try:
            # match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            # match_popup.click()
            body = driver.find_element(By.CSS_SELECTOR, "body")
            body.send_keys(Keys.ESCAPE)
        except NoSuchElementException:
            time.sleep(2)
time.sleep(10)
driver.quit()
