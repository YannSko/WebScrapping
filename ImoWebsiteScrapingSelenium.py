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
data1=[]
Checklist=[]

for p in range(0,100):
    try:
        driver.execute_script(f"location.href='https://www.bienici.com/recherche/achat/paris-75000?page={p}';")
    #driver.get(f'https://www.bienici.com/recherche/achat/paris-75000?page={p}')
        time.sleep(3)
    except:
        pass
    #Manger le cookie
    try:
    
        CookieButton = driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]')
        CookieButton.click()
    except:     
        #histoire de savoir combien la page comporte dappart    
        NbrAppart = driver.find_elements(By.CLASS_NAME,"sideListItemContainer")

        time.sleep(3)
        print( f" we are at the{p} and there are " + str(len(NbrAppart))+ " Appartements ")
#On recupe les liens de chaque offre un par un 
        LinkAppart = driver.find_elements(By.CLASS_NAME,"detailedSheetLink")


        page_tabs = [x.get_attribute('href') for x in driver.find_elements(By.CLASS_NAME,"detailedSheetLink")]
        for i in range(len(page_tabs)):
    
            driver.get(page_tabs[i])
            time.sleep(3)
            if driver.title not in Checklist :
                Offers = WebDriverWait(driver, 3).until 
                EC.presence_of_element_located((By.CLASS_NAME,"detailedSheetContainer"))
                Offers= driver.find_elements(By.CLASS_NAME,"detailedSheetContainer")
        
                for Offer in Offers:
                    Adress = Offer.find_elements(By.CLASS_NAME,"fullAddress")
                    Price = Offer.find_elements(By.CLASS_NAME,"ad-price__the-price")
                    PriceMeters = Offer.find_elements(By.CLASS_NAME,"ad-price__price-per-square-meter")
                    MeterTots = Offer.find_elements(By.XPATH, '/html/body/div[2]/section/div/div[3]/section[3]/div[1]/div[4]/span')
                    RoomNbrs = Offer.find_elements(By.XPATH, '/html/body/div[2]/section/div/div[3]/section[3]/div[1]/div[5]/span')
                    DescripApparts = Offer.find_elements(By.CLASS_NAME,"descriptionContent")
                    DescripTieks = Offer.find_elements(By.CLASS_NAME,"neighborhoodDescription")
                    
                    print(Adress[0].text)
                    Adresse = Adress[0].text
                    chaine = Adresse
                    pos1 = chaine.find("750")
                    pos2 = chaine.find(" (")
                    Arrondissement= chaine[pos1:pos2]
                    neighborhood = chaine[pos2:]
                    print(f"l'Arrondissement est {Arrondissement}")
                    print(f"Le Quartier est {neighborhood}")
                    print(Price[0].text)
                    try:
                        print(PriceMeters[0].text)
                        PriceMeter=PriceMeters[0].text
                    except:
                        print( "Prix metre carré non renseingné")
                        PriceMeter= "NaN"
                    try:
                        print(MeterTots[0].text)
                        MeterTot = MeterTots[0].text
                    except:
                        print(" Pas de superficie total renseigné")
                        MeterTot = "NaN"
                    try:
                        print(RoomNbrs[0].text)
                        RoomNbr = RoomNbrs[0].text
                    except:
                        print("Nombre de pièce non renseigné")
                        RoomNbr = "NaN"
                        
                    try:
                        print( DescripApparts[0].text)
                        DescripAppart = DescripApparts[0].text
                    except:
                        print( " pas de description appart")
                        DescripAppart= "NaN"
                    try:
                        print( DescripTieks[0].text)
                        DescripTiek= DescripTieks[0].text
                    except:
                        print("Pas de Description")
                        DescripTiek = "NaN"
                    
                    data1.append([Arrondissement,neighborhood ,Price[0].text,PriceMeter,MeterTot,RoomNbr,DescripAppart,DescripTiek])
                    print('Page navigated after click: ' + driver.title)
                    Checklist.append(driver.title)
            
            
            else:
                pass
#or link in LinkAppart:
    #or a in range(len(dAdress)):
#for o in range (len(data1)):
    #print(data1[o])
print(data1)
data = sorted(data1)

with open('ImoParisBienIci.csv', 'wt',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Arrondissement', 'Neighborhood', 'Price', 'PriceMeter','MeterTot','RoomNbr','DescripAppart','DescripQuartier'])    
    writer.writerows(data)

