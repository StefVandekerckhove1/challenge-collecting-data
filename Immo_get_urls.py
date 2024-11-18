from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

driver = webdriver.Chrome()

path = "C:\\Users\\vande\\chromedriver-win64\\chromedriver.exe"

base_url = "https://www.immoweb.be/en/search/house/for-sale?countries=BE&isALifeAnnuitySale=false&isAnInvestmentProperty=false&isAPublicSale=false&isNewlyBuilt=false&isUnderOption=false&minPrice=50000&page=1&orderBy=cheapest"

property_urls = []

start_page = 1
end_page = 4

for page in range(start_page, end_page):
    url = f"{base_url}{page}"

    driver.get(url)
    time.sleep(3)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    listings = soup.find_all("a", class_="card__title-link")

    for listing in listings[:30]:
        property_url = listing['href']
        property_urls.append(property_url)
    print(f'Page {page} is done')    
    
driver.quit()
end_page = end_page - 1
csv_filename = f"property_urls_{start_page}_to_{end_page}.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([f"Property URLs from page {start_page} to {end_page}"])
    for url in property_urls:
        writer.writerow([url])