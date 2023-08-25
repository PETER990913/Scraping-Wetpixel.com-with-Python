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
URL = "https://wetpixel.com/forums/"
driver.get(URL)
####################
Forum_Catogory_List = []
Forum_Name_List = []
Topic_List = []
PostedBy_List = []
PostedDate_List = []
PostedDetail_List = []
####################
Elements = driver.find_elements(By.XPATH, '//*[@id="ipsLayout_mainArea"]/section/ol/li')
for i in range(len(Elements)):
    try:
        Category = Elements[i].find_elements(By.TAG_NAME, 'a')[1].text
        Category_URL = Elements[i].find_elements(By.TAG_NAME, 'a')[1].get_attribute('href')
        print("Forum Category:", Category)
        print(Category_URL)
    except:
        pass
    driver1 = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
    driver1.maximize_window()    
    driver1.get(Category_URL)
    Forum_Elements = driver1.find_elements(By.XPATH, '//*[@id="ipsLayout_mainArea"]/div[2]/ol/li/div[2]/h4/a')
    for Forum_Element in Forum_Elements:
        Forum = Forum_Element.text
        Forum_URL = Forum_Element.get_attribute('href')
        print("Forum Name:", Forum)
        print(Forum_URL)
        driver2 = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
        driver2.maximize_window()    
        driver2.get(Forum_URL)
        pages_number_text = driver2.find_elements(By.CLASS_NAME, 'ipsPagination_pageJump')[0].text
        pages_number = int(re.findall(r'\d+', pages_number_text)[1])
        print(pages_number)        
        
        j = 0
        while j<pages_number:   
            Datatables = driver2.find_elements(By.CSS_SELECTOR, 'li[class="ipsDataItem ipsDataItem_responsivePhoto   "]')
            print(len(Datatables))
            for Datatable in Datatables:
                Final_URL = Datatable.find_elements(By.TAG_NAME, 'a')[0].get_attribute('href')
                print(Final_URL)
                driver3 = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
                driver3.maximize_window()
                driver3.get(Final_URL)
                ele = driver3.find_elements(By.XPATH, '//*[@id="ipsLayout_mainArea"]/div[1]/div[3]/div/h1/span')
                if len(ele) == 1:
                    Topic = driver3.find_elements(By.XPATH, '//*[@id="ipsLayout_mainArea"]/div[1]/div[3]/div/h1/span')[0].text
                else:
                    Topic = driver3.find_elements(By.XPATH, '//*[@id="ipsLayout_mainArea"]/div[1]/div[3]/div/h1/span')[1].text
                print("Topic:", Topic)
                el = driver3.find_elements(By.CLASS_NAME, 'ipsPagination_pageJump')
                print(len(el))
                if len(el)!=0:
                    print("---------------")
                    posts_pages_number_text = el[0].text
                    posts_pages_number = int(re.findall(r'\d+', posts_pages_number_text)[1])
                    print(posts_pages_number)
                    k=0
                    while k<posts_pages_number:
                        posts_elements = driver3.find_elements(By.TAG_NAME, 'article')
                        for posts_element in posts_elements:
                            PostedBy = posts_element.find_elements(By.TAG_NAME, 'strong')[0].text
                            print("PostedBy:", PostedBy)
                            postedDate = posts_element.find_elements(By.TAG_NAME, 'time')[0].text
                            print("PostedDate:", postedDate)
                            postedDetail = posts_element.find_element(By.CSS_SELECTOR, 'div[class="ipsType_normal ipsType_richText ipsContained"]').text   
                            elem = posts_element.find_element(By.CSS_SELECTOR, 'div[class="cPost_contentWrap ipsPad"]')
                            PicElements = elem.find_elements(By.TAG_NAME, 'img')
                            if len(PicElements)!=0:
                                for PicElement in PicElements:
                                    PicURL = PicElement.get_attribute('src')
                                    postedDetail = postedDetail + " :attached image URL: " + PicURL
                            print("PostedDetail:", postedDetail) 
                            Forum_Catogory_List.append(Category)
                            Forum_Name_List.append(Forum)
                            Topic_List.append(Topic)
                            PostedBy_List.append(PostedBy)
                            PostedDate_List.append(postedDate)
                            PostedDetail_List.append(postedDetail)
                        try:
                            driver3.find_elements(By.CLASS_NAME, 'ipsPagination_next')[0].click()
                        except:
                            print("can't find Next Button")
                        time.sleep(3)
                        k += 1
                        print("PostedDetailPagination:", k)                
                else:
                    print("++++++++++++++")
                    posts_elements = driver3.find_elements(By.TAG_NAME, 'article')
                    for posts_element in posts_elements:
                        PostedBy = posts_element.find_elements(By.TAG_NAME, 'strong')[0].text
                        print("PostedBy:", PostedBy)
                        postedDate = posts_element.find_elements(By.TAG_NAME, 'time')[0].text
                        print("PostedDate:", postedDate)
                        postedDetail = posts_element.find_element(By.CSS_SELECTOR, 'div[class="ipsType_normal ipsType_richText ipsContained"]').text 
                        elem = posts_element.find_element(By.CSS_SELECTOR, 'div[class="cPost_contentWrap ipsPad"]')
                        PicElements = elem.find_elements(By.TAG_NAME, 'img')
                        if len(PicElements)!=0:
                            for PicElement in PicElements:
                                PicURL = PicElement.get_attribute('src')
                                postedDetail = postedDetail + " :attached image URL: " + PicURL  
                        print("PostedDetail:", postedDetail)  
                        Forum_Catogory_List.append(Category)
                        Forum_Name_List.append(Forum)
                        Topic_List.append(Topic)
                        PostedBy_List.append(PostedBy)
                        PostedDate_List.append(postedDate)
                        PostedDetail_List.append(postedDetail)          
                driver3.close()
                dict = {'Forum_Cateogory': Forum_Catogory_List, 'Forum_Name': Forum_Name_List, 'Topic': Topic_List, 'PosetedBy': PostedBy_List,
                'PostedDate': PostedDate_List, 'PostedDetail': PostedDetail_List}

                df = pd.DataFrame(dict)

                df.to_csv('Result.csv')
                
            try:
                driver2.find_elements(By.CLASS_NAME, 'ipsPagination_next')[0].click()
            except:
                print("can't find the Next Button")
            time.sleep(3)
            j += 1
            print("Forum Pagination:", j)
        
        
        driver2.close()
    driver1.close()
    
print("------------Successfully finished-------------") 
while True:
    pass
