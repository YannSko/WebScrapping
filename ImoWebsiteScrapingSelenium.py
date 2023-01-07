driver = webdriver.Firefox()
data1=[]
Checklist=[]

for p in range(0,3):
    driver.get(f'https://www.bienici.com/recherche/achat/paris-75000?page={p}')
    time.sleep(3)
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
                    PriceMeter = Offer.find_elements(By.CLASS_NAME,"ad-price__price-per-square-meter")
                    MeterTot = Offer.find_elements(By.XPATH, '/html/body/div[2]/section/div/div[3]/section[3]/div[1]/div[4]/span')
                    RoomNbr = Offer.find_elements(By.XPATH, '/html/body/div[2]/section/div/div[3]/section[3]/div[1]/div[5]/span')
                    DescripAppart = Offer.find_elements(By.CLASS_NAME,"descriptionContent")
                    DescripTieks = Offer.find_elements(By.CLASS_NAME,"neighborhoodDescription")
                    
                    print(Adress[0].text)
                    print(Price[0].text)
                    print(PriceMeter[0].text)
                    print(MeterTot[0].text)
                    print(RoomNbr[0].text)
                    print( DescripAppart[0].text)
                    try:
                        print( DescripTieks[0].text)
                        DescripTiek= DescripTieks[0].text
                    except:
                        print("Pas de Description")
                        DescripTiek = "Pas de Description"
                    
                    data1.append([Adress[0].text,Price[0].text,PriceMeter[0].text,MeterTot[0].text,RoomNbr[0].text,DescripAppart[0].text,DescripTiek])
                    print('Page navigated after click: ' + driver.title)
                    Checklist.append(driver.title)
            
            
            else:
                pass
#or link in LinkAppart:
    #or a in range(len(dAdress)):
for o in range (len(data1)):
    print(data1[o])
with open('ImoParisBienIci.csv', 'wt',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Adress', 'Price', 'PirceMeter','MeterTot','RoomNbr','DescripAppart','DescripQuartier'])    
    writer.writerows(data1)