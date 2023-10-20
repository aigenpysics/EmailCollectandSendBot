from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pandas as pd
import random
import csv
import chromedriver_autoinstaller
import os

chromedriver_autoinstaller.install() 
headers = {"accept-language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7","accept-encoding":"gzip, deflate, br","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-mode":"document","sec-fetch-mode":"navigate", "sec-fetch-site":"none","sec-fetch-user":"?1","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(ChromeDriverManager().install())  #version 업데이트

def BackToList(my_lst):
    my_set = set(my_lst)
    lst = list(my_set)
    print(len(lst))
    return lst

def write_list_to_csv(lst, filename):
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for item in lst:
            if item in open(filename, 'r').read():
                continue  # Skip writing the item if it already exists in the file
            writer.writerow([item])

#Start
email_count = 0 
delay = random.randint(2, 5)

for j in range(199):    #change page until it's 200   
    start_time = time.time()
    page = j+1 #335
    print(f"Current Page: {page} page") 
    time.sleep(delay)
    url = f'https://search.shopping.naver.com/search/category/100010989?catId=50000554&iq=%EC%97%AC%EC%84%B1&origQuery&pagingIndex={page}&pagingSize=40&productSet=&query&sort=rel&spec=M10013455%7CM10537277&timestamp=&viewType=list'


    driver.get(url)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #scroll down
    driver.implicitly_wait(4)
    table = driver.find_elements(By.CSS_SELECTOR, ".product_mall__hPiEH.linkAnchor")
    link_urls = []
    email_lst = []
    for i in table:
        link_urls.append(i.get_attribute('href'))
    #debug
    #print(len(link_urls))

    for link_url in link_urls:
        try:
            driver.get(link_url)
            time.sleep(delay)
            cur_url = driver.current_url
            if 'smartstore.naver.com' in cur_url:       #page move to '판매자정보'   
                cur_url = cur_url.replace('https://smartstore.naver.com/','') 
                cur_url = cur_url.split('?')            #casting to lst, cur_url[0], id
                url = f'https://smartstore.naver.com/{cur_url[0]}/profile?cp=1'
                driver.get(url)
                time.sleep(delay)
                temp = driver.find_elements(By.CSS_SELECTOR, '._2PXb_kpdRh')
                print(f"Number of emails saved: {email_count + 1}")
                email_count += 1
                for a in temp:
                    if '@' in a.text: #re
                        print(a.text)
                        email_lst.append(a.text)

            else:
                pass
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Refreshing the page...")
            driver.refresh()
        
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time} seconds")  #1p 1분 30초
    write_list_to_csv(BackToList(email_lst), 'emailGathering2.csv')
    print("Save to data...")
