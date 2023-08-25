from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    options=options, executable_path="C:\Program Files (x86)\chromedriver\chromedriver.exe")

print("-----------Automation process is successfully started------------")
# driver = uc.Chrome(driver_executable_path=ChromeDriverManager(version='114.0.5735.90').install())
driver.maximize_window()
URL = "https://www.prioritypass.com/join-prioritypass"
driver.get(URL)

try:
    driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
except:
    pass

driver.find_element(By.XPATH, '//*[@id="join-process"]/section/div[2]/div/div/div/div/div/div/div[4]/article[2]/div/form/header/div[2]/button').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="personal-details"]/div[2]/form/div[1]/div[3]/div/div[1]/div/span').click()


# Create an ActionChains object
actions = ActionChains(driver)

# Perform the action to press the arrow down key
actions.send_keys(Keys.ARROW_DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()

driver.find_element(By.XPATH, '//*[@id="personal-details"]/div[2]/form/div[1]/div[4]/div/div[1]/div/span').click()
actions.send_keys(Keys.ARROW_DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()

driver.find_element(By.XPATH, '//*[@id="Forename_FormField"]').send_keys("aa")
driver.find_element(By.XPATH, '//*[@id="Surname_FormField"]').send_keys("aa")
driver.find_element(By.XPATH, '//*[@id="Email_FormField"]').send_keys("aaaa@gmail.com")
driver.find_element(By.XPATH, '//*[@id="PersonalDetails.Rendering.ConfirmEmail_FormField"]').send_keys("aaaa@gmail.com")

driver.find_element(By.XPATH, '//*[@id="personal-details"]/div[2]/form/div[1]/div[9]/div/div[1]/div[1]/div/span').click()
for _ in range(13):
    actions.send_keys(Keys.ARROW_DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()

driver.find_element(By.XPATH, '//*[@id="personal-details"]/div[2]/form/div[1]/div[9]/div/div[1]/div[2]/div/span').click()
for _ in range(11):
    actions.send_keys(Keys.ARROW_DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()

driver.find_element(By.XPATH, '//*[@id="personal-details"]/div[2]/form/div[1]/div[9]/div/div[1]/div[3]/div/span').click()
for _ in range(11):
    actions.send_keys(Keys.ARROW_DOWN)
actions.send_keys(Keys.ENTER)
actions.perform()

driver.find_element(By.XPATH, '//*[@id="Telephone_FormField"]').send_keys("00972544349958")
driver.find_element(By.XPATH, '//*[@id="CountryOfResidence"]').send_keys("Israel")

driver.find_element(By.XPATH, '//*[@id="personal-details"]/div[2]/form/div[2]/div/button').click()

time.sleep(5)




while True:
    pass