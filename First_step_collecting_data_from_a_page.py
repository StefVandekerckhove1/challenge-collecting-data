from multiprocessing import Pool
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time
import re



path = "C:/Program Files (x86)/Google/chromedriver-win64/chromedriver.exe"

def init_driver():
    service = Service(path)
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def create_data(url_house):
    driver = init_driver()  
    try:
        driver.get(url_house)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        list_values_columns=[]
        myDict= dict.fromkeys(['Locality','Type of property','Subtype of property','Price','Number of rooms','Living Area',
                    'Fully equipped kitchen','Furnished','Open fire','Terrace','Garden', 'Surface of the land',
                    'Surface area of the plot of land','Number of facades','Swimming pool','State of the building','Code_Immoweb'], None)   
        
        Locality = soup.select_one('div.classified__information--address span.classified__information--address-row:last-of-type')
        Locality=' '.join(Locality.text.split())
        list_values_columns.append(Locality)
        
        title=soup.select_one('div.classified__header-primary-info h1.classified__title ')
        Title=' '.join(title.get_text().split())
        Title=Title.split()[0] 
        if (Title == 'House' or Title=='Apartment'):
            list_values_columns.extend([Title, None])
        else:
            list_values_columns.extend([None,Title])



        row_price=soup.find('th', string='Price')
        Price=row_price.find_next_sibling('td').text
        Price = Price[:int(len(Price)/2)]     
        Price=int(re.sub(r'[^\d]', '', Price)) 

        list_values_columns.append(Price)

        number_of_rooms=soup.select_one('div.text-block div.grid div.text-block__body div.overview__column div.overview__item span.overview__text')
        if number_of_rooms:
            Number_of_room=' '.join(number_of_rooms.get_text().split())
            Number_of_room=Number_of_room[:2]
            list_values_columns.append(int(Number_of_room))
        else:
            Number_of_room=None
            list_values_columns.append(Number_of_room)


        row_Living_Area = soup.find('th', string=re.compile(r'\s*Living area\s*'))
        if row_Living_Area:
            Living_Area=row_Living_Area.find_next_sibling('td')
            Living_Area=' '.join(Living_Area.get_text(strip=True).split())
            Living_Area=re.findall(r'\d+',Living_Area)
            list_values_columns.append(int(Living_Area[0]))
        else:
            Living_Area=None
            list_values_columns.append(Living_Area)

        row_Kitchen_type=soup.find('th', string='Kitchen type')
        if row_Kitchen_type:
            Kitchen_type=row_Kitchen_type.find_next_sibling('td')
            Kitchen_type=' '.join(Kitchen_type.get_text(strip=True).split())
            list_values_columns.append(1)
        else:
            list_values_columns.append(0)


        row_Furnished= soup.find('th', string="Furnished")
        if row_Furnished:
            Furnished=row_Furnished.find_next_sibling('td')
            Furnished=' '.join(Furnished.get_text(strip=True).split()) 
            list_values_columns.append(1)
        else:
            list_values_columns.append(0)


        row_Open_Fire= soup.find('th', string="How many fireplaces?")
        if row_Open_Fire:
            Open_Fire=row_Open_Fire.find_next_sibling('td')
            Open_Fire=' '.join(Open_Fire.get_text(strip=True).split())
            list_values_columns.append(1)
        else:
            Open_Fire=None
            list_values_columns.append(0)


        row_Terrace= soup.find('th', string="Terrace surface")
        if row_Terrace:
            Terrace=row_Terrace.find_next_sibling('td')
            Terrace=' '.join(Terrace.get_text(strip=True).split())
            Terrace=re.findall(r'\d+',Terrace)
            list_values_columns.append(int(Terrace[0]))
        else:
            Terrace=None
            list_values_columns.append(0)

        row_Garden= soup.find('th', string="Garden surface")
        if row_Garden:
            Garden=row_Garden.find_next_sibling('td')
            Garden=' '.join(Garden.get_text(strip=True).split())
            Garden=re.findall(r'\d+',Garden)
            list_values_columns.append(int(Garden[0]))
            Surface_of_the_land=int(Garden[0])
            list_values_columns.append(Surface_of_the_land)

        else:
            Garden=None
            Surface_of_the_land=None
            list_values_columns.extend([Garden, Surface_of_the_land])
    
        row_Surface_area_of_the_plot_of_land= soup.find('th', string="Surface of the plot")
        if row_Surface_area_of_the_plot_of_land:
            Surface_area_of_the_plot_of_land=row_Surface_area_of_the_plot_of_land.find_next_sibling('td')
            Surface_area_of_the_plot_of_land=' '.join(Surface_area_of_the_plot_of_land.get_text(strip=True).split())
            Surface_area_of_the_plot_of_land=re.findall(r'\d+',Surface_area_of_the_plot_of_land)
            list_values_columns.append(int(Surface_area_of_the_plot_of_land[0]))
            
        else:
            Surface_area_of_the_plot_of_land=None
            list_values_columns.append(Surface_area_of_the_plot_of_land)   

        row_Number_of_facades = soup.find('th', string=re.compile(r'\s*Number of frontages\s*'))
        if row_Number_of_facades:
            Number_of_facades = row_Number_of_facades.find_next_sibling('td')
            Number_of_facades = ' '.join(Number_of_facades.get_text(strip=True).split())
            list_values_columns.append(Number_of_facades)
        else:
            Number_of_facades=None
            list_values_columns.append(Number_of_facades)

        row_Swimming_pool=soup.find('th', string=re.compile(r'\s*Swimming pool\s*'))
        if row_Swimming_pool:
            Swimming_pool=row_Swimming_pool.find_next_sibling('td')
            Swimming_pool=' '.join(Swimming_pool.get_text(strip=True).split())
            list_values_columns.append(1)
        else:
            Swimming_pool=None
            list_values_columns.append(0)

        row_Bulding_Condition=soup.find('th', string=re.compile(r"\s*Building condition\s*"))
        if row_Bulding_Condition:
            State_of_the_building=row_Bulding_Condition.find_next_sibling('td')
            State_of_the_building=' '.join(State_of_the_building.get_text(strip=True).split())
            list_values_columns.append(State_of_the_building)
        else:
            State_of_the_building=None
            list_values_columns.append(State_of_the_building)
        
        Code_Immoweb=soup.select_one('div.classified__header--immoweb-code' )
        Code_Immoweb= int(' '.join(Code_Immoweb.text.split())[15::])
        list_values_columns.append(Code_Immoweb)
        

        row_Under_Option = soup.find('span', string='Under option')
        row_Public_Sale = soup.find('span', string='Online sale')
        row_Tenement_Building = soup.find('th', string=re.compile(r"\s*Tenement building\s*"))

        if row_Under_Option:
            Under_Option = ' '.join(row_Under_Option.get_text(strip=True).split())
            if row_Tenement_Building:
                Tenement_Building = row_Tenement_Building.find_next_sibling('td')
                Tenement_Building = ' '.join(Tenement_Building.get_text(strip=True).split())
                list_values_columns.append((Under_Option, Tenement_Building))

        elif row_Public_Sale:
            Public_Sale = ' '.join(row_Public_Sale.get_text(strip=True).split())
            if row_Tenement_Building:
                Tenement_Building = row_Tenement_Building.find_next_sibling('td')
                Tenement_Building = ' '.join(Tenement_Building.get_text(strip=True).split())
                list_values_columns.append((Public_Sale, Tenement_Building))


        else:
            if row_Tenement_Building:
                Tenement_Building = row_Tenement_Building.find_next_sibling('td')
                Tenement_Building = ' '.join(Tenement_Building.get_text(strip=True).split())
                list_values_columns.append(Tenement_Building)
       
        for key, value in zip(myDict.keys(), list_values_columns):
             myDict[key] = value

        return myDict

        

    finally:
        driver.quit()


# Import date with pandas
df= pd.read_csv('property_urls_1_to_111.csv')
#Create a list of the first 19 links and save it in urls
urls = df['Property URLs from page 1 to 111'][1:20].tolist()

if __name__ == "__main__":
    #Initialize a pool of 5 worker processes
    with Pool(processes=5) as pool: 
        # Use the pool to apply the create_data function to each URL  
        results = pool.map(create_data, urls)   

    for result in results:
        print(result)