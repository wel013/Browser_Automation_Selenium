URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102965250&keywords=python%20developer&location=Ann%20Arbor%2C%20Michigan%2C%20United%20States"

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service('C:/Development/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
driver.get(URL)


# TODO: after opening the page, automatically sign in to linkedin
btn = driver.find_element(by=By.LINK_TEXT, value="Sign in")
btn.click()

email = "wenqianli010524@gmail.com"
pswd = os.environ['linkedin_pswd']
#when publishing on internet, put this into the env var

email_add = driver.find_element(by=By.ID, value="username")
email_add.send_keys(email)

password = driver.find_element(by=By.ID, value="password")
password.send_keys(pswd)

btn1 = driver.find_element(by=By.CSS_SELECTOR, value="div button")
btn1.click()
driver.maximize_window()
time.sleep(5)


# TODO: easy apply, but save the application instead of
#  sending meaningless apps
# first_job = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-search-results__list a")
# first_job.click()
# time.sleep(5)

# TODO: now save all the job on the page (for practice purpose)
job_list = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
for job in job_list:
    job.click()
    time.sleep(5)
    save_btn = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
    save_btn.click()
    time.sleep(3)



#path1 for actual app
# #leave enough time for the website to respond, 3 secs failed in many instanced
# app_btn = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
# app_btn.click()
# phone_num = "xxxxxxxxx"
# phone_number_fill = driver.find_element(by=By.CSS_SELECTOR, value=".display-flex input")
# phone_number_fill.send_keys(phone_num)
# next_btn = driver.find_element(By.CSS_SELECTOR, "footer button")
# next_btn.click()
# time.sleep(3)
#
# review_btn = driver.find_element(By.CSS_SELECTOR, "footer button")
# review_btn.click()
# #last step would be to apply, which is not what I want to actually do in this project
# submit = driver.find_element(By.CSS_SELECTOR, "footer .artdeco-button__text")
# submit.click()

#alt path for saving the job
# save_btn = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
# save_btn.click()

time.sleep(5)
driver.quit()

# update the project when ready to apply for real job,
# skip everything that is not easy apply (such as have to leave a not, etc)






