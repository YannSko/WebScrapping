import os
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


driver = webdriver.Firefox()
data = []

# for i in range (0,27):
driver.get('https://www.achat-ski.com/INTERSHOP/web/WFS/EKO-HASKI-Site/fr_FR/-/EUR/ViewStandardCatalog-ProductPaging?PageNumber='+str(i) +
           '&SortingAttribute=M_T_MEA-desc&PageSize=24&CatalogID=6&CategoryName=1024&FacetName=ProductDiscountPercent&ForMobile=true&SearchParameter=%26%40QueryTerm%3D*%26ContextCategoryUUID%3DK.LAqNYzb20AAAFsoo8cBvhK%26OnlineFlag%3D1')
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]').click()

for i in range(0, 27):
    driver.get('https://www.achat-ski.com/INTERSHOP/web/WFS/EKO-HASKI-Site/fr_FR/-/EUR/ViewStandardCatalog-ProductPaging?PageNumber='+str(i) +
               '&SortingAttribute=M_T_MEA-desc&PageSize=24&CatalogID=6&CategoryName=1024&FacetName=ProductDiscountPercent&ForMobile=true&SearchParameter=%26%40QueryTerm%3D*%26ContextCategoryUUID%3DK.LAqNYzb20AAAFsoo8cBvhK%26OnlineFlag%3D1')

    NomObjet = driver.find_elements(By.CLASS_NAME, 'item_name')
    Price = driver.find_elements(By.CLASS_NAME, 'new_price')
    Marque = driver.find_elements(By.CLASS_NAME, 'brandTitle')
    PageObjet = driver.find_elements(By.CLASS_NAME, 'list_item-link')
    # OtherPage = driver.find_elements(By.PARTIAL_LINK_TEXT('www.achat-ski.com').click();

    for i in range(0, len(NomObjet)):
        print(NomObjet[i].text)
        print(Price[i].text)
        print(Marque[i].text)
        data.append([NomObjet[i].text, Price[i].text, Marque[i].text])


with open('DataAchatSki.csv', 'wt', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['NomObjet', 'PrixObjet', 'MarqueObjet'])
    writer.writerows(data)
#elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)

    #writer.writerow([NomObjet.encode('utf-8'), Price.encode('utf-8'), Marque.encode('utf-8')])
file.close()
driver.close()


# pour supprimer le csv

path = './DataAchatSki.csv'
File_exist = os.path.exists(path)
print(File_exist)
if(File_exist):
    # Permet d'effacer le fichier csv s'il existe ( permet de le mettre à jour sans conflit )
    os.remove('./DataAchatSki.csv')
