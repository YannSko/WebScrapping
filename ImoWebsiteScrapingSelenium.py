driver = webdriver.Firefox()
data1=[]


driver.get('https://www.bienici.com/recherche/achat/paris-75000/appartement')
time.sleep(3)
#Manger le cookie
CheckCookie = 1
if CheckCookie == 1:
    CookieButton = driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]')
    CookieButton.click()
    CheckCookie = 0
#histoire de savoir combien la page comporte dappart    
NbrAppart = driver.find_elements(By.CLASS_NAME,"sideListItemContainer")


print(len(NbrAppart))
#On recupe les liens de chaque offre un par un 
LinkAppart = driver.find_elements(By.CLASS_NAME,"detailedSheetLink")


page_tabs = [x.get_attribute('href') for x in driver.find_elements(By.CLASS_NAME,"detailedSheetLink")]
for i in range(len(page_tabs)):
    
    driver.get(page_tabs[i])
    time.sleep(5)
    
    Offers= driver.find_elements(By.CLASS_NAME,"detailedSheetContainer")
    for Offer in Offers:
        Adress = Offer.find_elements(By.CLASS_NAME,"fullAddress")
        print(Adress[0].text)
        AdressStock = Adress[0].text
        data1.append(AdressStock)
        print('Page navigated after click: ' + driver.title)
#or link in LinkAppart:
    #or a in range(len(dAdress)):
        for o in range (len(data1)):
            print(data1[o])
   #OneAppart = link.get_attribute('href')
   #print(OneAppart)
   #OneAppart.click()
    
        
    #  print(OneAppart)

# On va parser chaque offre et recupe les infos que l'on souhaite
  # dAdress = driver.find_elements(By.CLASS_NAME,"fullAddress")
    #dPrice = driver.find_elements(By.CLASS_NAME,"ad-price__the-price")
    #dPriceMeter = driver.find_elements(By.CLASS_NAME,"ad-price__price-per-square-meter")
    #dHono = driver.find_elements(By.CLASS_NAME,"ad-price__fees-infos")
    #dSuperficie = driver.find_elements(By.XPATH,"/html/body/div[2]/section/div/div[3]/section[3]/div[1]/div[4]/span")
    #dNbrRoom = driver.find_elements(By.XPATH,"/html/body/div[2]/section/div/div[3]/section[3]/div[1]/div[5]/span")
    #dNbrChamber = driver.find_elements(By.XPATH,"/html/body/div[2]/section/div/div[3]/section[3]/div[1]/div[6]/span")
    #dTieksDescrip = driver.find_elements(By.CLASS_NAME,"neighborhoodDescription")
#Convertir en un type " exploitable"
   #for a in range(len(dAdress)):
   #Adress = dAdress.text
    #Price = dPrice.Text
    #PriceMeter = dPriceMeter.text
    #Hono = dHono.text
    #Superficie = dSuperficie.text
    #NbrRoom = dNbrRoom.text
    #NbrChamber = dNbrChamber.text
    #TieksDescrip = dTieksDescrip.text
    #   print(dAdress[a].text)
#driver.navigate().back();
#LinkAppart = driver.find_elements(By.CLASS_NAME,"listing-item-link")
#for i in range (0,len(NbrAppar)):
    #print(LinkAppart[i].text)
    #print(Price[i].text)
    #print(SuperficieRoom [i].text)
    #print(Localisation [i].text)
    #print(Description [i].text)
    #data.append([Localisation [i].text,Price[i].text,SuperficieRoom[i].text],Description [i].text)
#for b in range (1,len(NbrAppart)-1):
   # elementBot =  driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/div[3]/div/div[2]/section/div/div[1]/article['+str(b)+']/div/div/div/div[1]/div/div[2]/div/div[2]/a').click()
   # elementBot.click()

#driver.back()
   
       
   
    #with open('DataAchatSki.csv', 'wt',encoding='utf-8') as file:
    #writer = csv.writer(file)
    #writer.writerow(['NomObjet', 'PrixObjet', 'MarqueObjet'])    
    #writer.writerows(data)
#elem = driver.find_element(By.NAME, "q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
        
    #writer.writerow([NomObjet.encode('utf-8'), Price.encode('utf-8'), Marque.encode('utf-8')])
#file.close()
#driver.close