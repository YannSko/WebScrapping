
driver = webdriver.Firefox()
data = []

for p in range(0, 2):  # change the range to the number of pages you want to scrape
    driver.get(f'https://www.cdiscount.com/search/10/ordinateur+portable.html#_his_&page={p}')
    time.sleep(3)

    # Handle cookie
    try:
        cookie_button = driver.find_element(By.CLASS_NAME, 'a-link-emphasis')
        cookie_button.click()
    except:
        pass

    # Get number of products on the page
   

    links_product = [x.get_attribute('href') for x in driver.find_elements(By.XPATH,('//a[@class="jsPrdtBILA prdtBILA"]'))]
    print(f"Links to products on page {p}: {links_product}")

    for link in range(len(links_product)):
        driver.get(links_product[link])
        time.sleep(1)
        product = driver.find_elements(By.ID,"fpContent")
        for feature in product:
            time.sleep(1)
            name = feature.find_element(By.XPATH,'//h1[@class=""]').text
            price = feature.find_element(By.XPATH, '//span[@class="fpPrice price priceColor jsMainPrice jsProductPrice hideFromPro"]').text
            rating = feature.find_element(By.XPATH, '//span[@itemprop="ratingValue"]').get_attribute('textContent')
            table = {}
            for info_table in feature.find_elements(By.XPATH, '//tbody[@class="table__body"]'):
                keys = info_table.find_elements(By.XPATH, '//th[@class="table__cell"]')
                values = info_table.find_elements(By.XPATH, '//td[@class="table__cell"]')
                for i in range(min(len(keys), len(values))):
                    key = keys[i].text
                    value = values[i].text
                    table[key] = value
            data.append({"Name": name, "Price": price, "Rating": rating, "InfoSupplementaire": table})
            print(data)

driver.quit()