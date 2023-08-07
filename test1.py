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
driver = uc.Chrome(driver_executable_path=ChromeDriverManager(version='114.0.5735.90').install())
driver.maximize_window()
URL = "https://wetpixel.com/forums/index.php?/topic/71304-is-wetpixelcom-dead-or-dying/"
# URL = "https://wetpixel.com/forums/index.php?/topic/71203-a-useful-product/"
driver.get(URL)
ele = driver.find_elements(By.XPATH, '//*[@id="ipsLayout_mainArea"]/div[1]/div[3]/div/h1/span')
if len(ele) == 1:
    Topic = driver.find_elements(By.XPATH, '//*[@id="ipsLayout_mainArea"]/div[1]/div[3]/div/h1/span')[0].text
else:
    Topic = driver.find_elements(By.XPATH, '//*[@id="ipsLayout_mainArea"]/div[1]/div[3]/div/h1/span')[1].text
print(Topic)
el = driver.find_elements(By.CLASS_NAME, 'ipsPagination_pageJump')
print(len(el))
if len(el)!=0:
    print("---------------")
    posts_pages_number_text = el[0].text
    posts_pages_number = int(re.findall(r'\d+', posts_pages_number_text)[1])
    print(posts_pages_number)
    k=0
    while k<posts_pages_number:
        posts_elements = driver.find_elements(By.TAG_NAME, 'article')
        for posts_element in posts_elements:
            PostedBy = posts_element.find_elements(By.TAG_NAME, 'strong')[0].text
            print(PostedBy)
            postedDate = posts_element.find_elements(By.TAG_NAME, 'time')[0].text
            print(postedDate)
            postedDetail = posts_element.find_element(By.CSS_SELECTOR, 'div[class="ipsType_normal ipsType_richText ipsContained"]').text   
            elem = posts_element.find_element(By.CSS_SELECTOR, 'div[class="cPost_contentWrap ipsPad"]')
            PicElements = elem.find_elements(By.TAG_NAME, 'img')
            if len(PicElements)!=0:
                for PicElement in PicElements:
                    PicURL = PicElement.get_attribute('src')
                    postedDetail = postedDetail + " :attached image URL: " + PicURL
            print(postedDetail) 
        try:
            driver.find_elements(By.CLASS_NAME, 'ipsPagination_next')[0].click()
        except:
            print("can't find Next Button")
        time.sleep(3)
        k += 1
        print(k)
        
else:
    print("++++++++++++++")
    posts_elements = driver.find_elements(By.TAG_NAME, 'article')
    for posts_element in posts_elements:
        PostedBy = posts_element.find_elements(By.TAG_NAME, 'strong')[0].text
        print(PostedBy)
        postedDate = posts_element.find_elements(By.TAG_NAME, 'time')[0].text
        print(postedDate)
        postedDetail = posts_element.find_element(By.CSS_SELECTOR, 'div[class="ipsType_normal ipsType_richText ipsContained"]').text   
        elem = posts_element.find_element(By.CSS_SELECTOR, 'div[class="cPost_contentWrap ipsPad"]')
        PicElements = elem.find_elements(By.TAG_NAME, 'img')
        if len(PicElements)!=0:
            for PicElement in PicElements:
                PicURL = PicElement.get_attribute('src')
                postedDetail = postedDetail + " :attached image URL: " + PicURL
        print(postedDetail) 

print("000000000000000000")
while True:
    pass