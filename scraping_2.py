from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
print("-----------Automation Scraping is successfully started------------")
driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
driver.maximize_window()
URL = "https://hmsusa.org/certified-listing.html"
driver.get(URL)
time.sleep(10)
####################
driver.find_element(By.XPATH, '//*[@id="showAll"]').click()

select = Select(driver.find_element(By.XPATH, '//*[@id="certifiedListingTable_length"]/label/select'))
select.select_by_value('100')

pagination_bar = driver.find_element(By.XPATH, '//*[@id="certifiedListingTable_paginate"]/ul')
pagination_count = pagination_bar.find_elements(By.TAG_NAME, 'li')[-2].text
print(pagination_count)
Name_list = []
Address_list = []
Phone_list = []
for i in range(0, int(pagination_count)):
    tbody = driver.find_element(By.XPATH, '//*[@id="certifiedListingTable"]/tbody')
    tables = tbody.find_elements(By.TAG_NAME, 'tr')
    for table in tables:
        Name = table.find_elements(By.TAG_NAME, 'td')[1].text
        print(Name)
        Name_list.append(Name)
        Address = table.find_elements(By.TAG_NAME, 'td')[2].text
        print(Address)
        Address_list.append(Address)
        Phone = table.find_elements(By.TAG_NAME, 'td')[3].text
        print(Phone)
        Phone_list.append(Phone)
    try:
        driver.find_element(By.XPATH, '//*[@id="certifiedListingTable_next"]/a').click()
        time.sleep
    except:
        print("can't find the next button")
dict = {'Business Name': Name_list, 'Business Address': Address_list, 'Business Phone Number': Phone_list}

df = pd.DataFrame(dict)

df.to_csv('Business2.csv')

print("------------Successfully finished-------------") 
while True:
    pass
