driver = webdriver.Firefox()
data1=[]
Checklist=[]

for p in range(0,101):
    driver.get(f'https://www.bienici.com/recherche/achat/paris-75000?page={p}')
    time.sleep(3)
    #Manger le cookie
    try:
    
        CookieButton = driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]')
        CookieButton.click()
    except:     
        #histoire de savoir combien la page comporte dappart    
        NbrAppart = driver.find_elements(By.CLASS_NAME,"sideListItemContainer")


        print(len(NbrAppart))
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
                    print(Adress[0].text)
                    AdressStock = Adress[0].text
                    data1.append(AdressStock)
                    print('Page navigated after click: ' + driver.title)
                    Checklist.append(driver.title)
            
            
            else:
                pass
#or link in LinkAppart:
    #or a in range(len(dAdress)):
for o in range (len(data1)):
    print(data1[o])