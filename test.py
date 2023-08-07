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
URL = "https://wetpixel.com/forums/index.php?/forum/10-announcements/"
driver.get(URL)
pages_number_text = driver.find_elements(By.CLASS_NAME, 'ipsPagination_pageJump')[0].text
pages_number = int(re.findall(r'\d+', pages_number_text)[1])
print(pages_number)
# wait = WebDriverWait(driver, 30)  # Maximum wait time of 10 seconds
# element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#myElement")))
# element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ips_uid_3640_13"]')))

# for i in range(1, pages_number): 
i = 0
while i<pages_number:   
    Datatables = driver.find_elements(By.CSS_SELECTOR, 'li[class="ipsDataItem ipsDataItem_responsivePhoto   "]')
    print(len(Datatables))
    for Datatable in Datatables:
        Final_URL = Datatable.find_elements(By.TAG_NAME, 'a')[0].get_attribute('href')
        print(Final_URL)
        driver1 = uc.Chrome(driver_executable_path=ChromeDriverManager(version='114.0.5735.90').install())
        driver1.maximize_window()
        driver1.get(Final_URL)
        ele = driver1.find_elements(By.XPATH, '//*[@id="ipsLayout_mainArea"]/div[1]/div[3]/div/h1/span')
        if len(ele) == 1:
            Topic = driver1.find_elements(By.XPATH, '//*[@id="ipsLayout_mainArea"]/div[1]/div[3]/div/h1/span')[0].text
        else:
            Topic = driver1.find_elements(By.XPATH, '//*[@id="ipsLayout_mainArea"]/div[1]/div[3]/div/h1/span')[1].text
        print(Topic)
        el = driver1.find_elements(By.CLASS_NAME, 'ipsPagination_pageJump')
        print(len(el))
        if len(el)!=0:
            print("---------------")
            posts_pages_number_text = el[0].text
            posts_pages_number = int(re.findall(r'\d+', posts_pages_number_text)[1])
            print(posts_pages_number)
            k=0
            while k<posts_pages_number:
                posts_elements = driver1.find_elements(By.TAG_NAME, 'article')
                for posts_element in posts_elements:
                    PostedBy = posts_element.find_elements(By.TAG_NAME, 'strong')[0].text
                    print(PostedBy)
                    postedDate = posts_element.find_elements(By.TAG_NAME, 'time')[0].text
                    print(postedDate)
                    postDetail = posts_element.find_element(By.CSS_SELECTOR, 'div[class="ipsType_normal ipsType_richText ipsContained"]').text   
                    print(postDetail) 
                try:
                    driver1.find_elements(By.CLASS_NAME, 'ipsPagination_next')[0].click()
                except:
                    print("can't find Next Button")
                time.sleep(3)
                k += 1
                print(k)                
        else:
            print("++++++++++++++")
            posts_elements = driver1.find_elements(By.TAG_NAME, 'article')
            for posts_element in posts_elements:
                PostedBy = posts_element.find_elements(By.TAG_NAME, 'strong')[0].text
                print(PostedBy)
                postedDate = posts_element.find_elements(By.TAG_NAME, 'time')[0].text
                print(postedDate)
                postDetail = posts_element.find_element(By.CSS_SELECTOR, 'div[class="ipsType_normal ipsType_richText ipsContained"]').text   
                print(postDetail)            
        driver1.close()
    try:
        driver.find_elements(By.CLASS_NAME, 'ipsPagination_next')[0].click()
    except:
        print("can't find the Next Button")
    time.sleep(3)
    i += 1
    print(i)


# pages_number = int(pages_number_text)
# print(pages_number)
# print(type(pages_number))

while True:
    pass
