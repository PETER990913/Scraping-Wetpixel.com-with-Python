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
URL = "https://www.hfsaa.org/bayarea/"
driver.get(URL)
# time.sleep(10)
####################
Business_Name_list = []
Business_Address_list = []
Business_Phone_list = []
for j in range(0, 2):
    tables = driver.find_elements(By.CSS_SELECTOR, 'div[class="fusion-column-wrapper fusion-column-has-shadow fusion-flex-justify-content-flex-start fusion-content-layout-column"]')
    print(len(tables))
    for i in range(5, len(tables)-7):
        Business_name = tables[i].find_elements(By.TAG_NAME, 'div')[0].text
        if Business_name == "Restaurants":
            continue
        if Business_name == "Meat Markets":
            continue
        Business_Name_list.append(Business_name)
        print(Business_name)
        TDs = tables[i].find_elements(By.TAG_NAME, 'div')
        Business_address = TDs[1].find_elements(By.TAG_NAME, 'p')[0].text
        Business_Address_list.append(Business_address)
        print(Business_address)
        Business_phone = TDs[1].find_elements(By.TAG_NAME, 'p')[1].text
        Business_Phone_list.append(Business_phone)
        print(Business_phone)
    print(len(Business_Name_list))    
    print(len(Business_Address_list))    
    print(len(Business_Phone_list))    
    try:
        driver.find_element(By.XPATH, '//*[@id="post-2399"]/div/div[11]/a').click()
    except:
        pass
    time.sleep(5)
dict = {'Business Name': Business_Name_list, 'Business Address': Business_Address_list, 'Business Phone Number': Business_Phone_list}

df = pd.DataFrame(dict)

df.to_csv('Business1.csv')
    
print("------------Successfully finished-------------") 
while True:
    pass
