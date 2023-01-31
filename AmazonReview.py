driver = webdriver.Firefox()
data = []

for p in range(0, 2):
    driver.get('https://www.amazon.fr/s?rh=n%3A429879031&fs=true&ref=lp_429879031_sar')
    time.sleep(3)

    # Handle cookie
    try:
        cookie_button = driver.find_element(By.CLASS_NAME, 'a-link-emphasis')
        cookie_button.click()
    except:
        # Get number of products on the page
        nbr_products = driver.find_elements(By.CLASS_NAME,"sg-col-inner")
        print(len(nbr_products))
        links_product = [x.get_attribute('href') for x in driver.find_elements(By.XPATH,('//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]'))]
        print(links_product)
        for link in range(len(links_product)):
            driver.get(links_product[link])
            time.sleep(1)
            product = driver.find_elements(By.ID,"dp-container")
            for feature in product:
                time.sleep(1)
                name = feature.find_element(By.XPATH,'//span[@class="a-size-large product-title-word-break"]').text
                price = feature.find_element(By.XPATH, '//span[@class="a-price-whole"]').text
                rating = feature.find_element(By.XPATH, '//span[@class="a-icon-alt"]').get_attribute('textContent')
                table = []
                for info_table in feature.find_elements(By.XPATH, '//table[@class="a-keyvalue prodDetTable"]'):
                    for row in info_table.find_elements(By.XPATH, '//tr'):
                        key = row.find_element(By.XPATH, '//th[@class="a-color-secondary a-size-base prodDetSectionEntry"]').text
                        value = row.find_element(By.XPATH, '//td[@class="a-size-base prodDetAttrValue"]').text
                        table = [key,value]
                data.append({"Name": name, "Price": price, "Rating": rating, "InfoSupplementaire": table})
                print(data)

driver.quit()



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup
import urllib
import re
import requests
import csv
import time