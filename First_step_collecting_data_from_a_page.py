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


service = Service(path)
options = Options()

driver = webdriver.Chrome(service=service, options=options)

try:
    url_house='https://www.immoweb.be/en/classified/house/for-sale/sprimont/4140/20312392'

    house=driver.get(url_house)
   

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    def create_data() :
       
        list_values_columns=[]
        myDict= dict.fromkeys(['Locality','Type of property','Subtype of property','Price','Number of rooms','Living Area',
                    'Fully equipped kitchen','Furnished','Open fire','Terrace','Garden', 'Surface of the land',
                    'Surface area of the plot of land','Number of facades','Swimming pool','State of the building'], None)   
        

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
            list_values_columns.append(Number_of_room)
        else:
            Number_of_room=None
            list_values_columns.append(Number_of_room)


        row_Living_Area = soup.find('th', string="Living room surface")
        if row_Living_Area:
            Living_Area=row_Living_Area.find_next_sibling('td')
            Living_Area=' '.join(Living_Area.get_text(strip=True).split())
            list_values_columns.append(Living_Area)
        else:
            Living_Area=None
            list_values_columns.append(Living_Area)

        row_Kitchen_type=soup.find('th', string='Kitchen type')
        if row_Kitchen_type:
            Kitchen_type=row_Kitchen_type.find_next_sibling('td')
            Kitchen_type=' '.join(Kitchen_type.get_text(strip=True).split())
            list_values_columns.append(Kitchen_type)
        else:
            Kitchen_type=None
            list_values_columns.append(Kitchen_type)


        row_Furnished= soup.find('th', string="Furnished")
        if row_Furnished:
            Furnished=row_Furnished.find_next_sibling('td')
            Furnished=' '.join(Furnished.get_text(strip=True).split()) 
            list_values_columns.append(Furnished)
        else:
            Furnished=None
            list_values_columns.append(Furnished)


        row_Open_Fire= soup.find('th', string="How many fireplaces?")
        if row_Open_Fire:
            Open_Fire=row_Open_Fire.find_next_sibling('td')
            Open_Fire=' '.join(Open_Fire.get_text(strip=True).split())
            list_values_columns.append(Open_Fire)
        else:
            Open_Fire=None
            list_values_columns.append(None)


        row_Terrace= soup.find('th', string="Terrace surface")
        if row_Terrace:
            Terrace=row_Terrace.find_next_sibling('td')
            Terrace=' '.join(Terrace.get_text(strip=True).split())
            list_values_columns.append(Terrace)
        else:
            Terrace=None
            list_values_columns.append(Terrace)

        row_Garden= soup.find('th', string="Garden surface")
        if row_Garden:
            Garden=row_Garden.find_next_sibling('td')
            Garden=' '.join(Garden.get_text(strip=True).split())
            list_values_columns.append(Garden)
            Surface_of_the_land=Garden
            list_values_columns.append(Surface_of_the_land)

        else:
            Garden=None
            Surface_of_the_land=None
            list_values_columns.extend([Garden, Surface_of_the_land])
    
        row_Surface_area_of_the_plot_of_land= soup.find('th', string="Surface of the plot")
        if row_Surface_area_of_the_plot_of_land:
            Surface_area_of_the_plot_of_land=row_Surface_area_of_the_plot_of_land.find_next_sibling('td')
            Surface_area_of_the_plot_of_land=' '.join(Surface_area_of_the_plot_of_land.get_text(strip=True).split())
            list_values_columns.append(Surface_area_of_the_plot_of_land)
        else:
            Surface_area_of_the_plot_of_land=None
            list_values_columns.append(Surface_area_of_the_plot_of_land)   

        row_Swimming_pool=soup.find('th', string=re.compile(r'\s*Swimming pool\s*'))
        if row_Swimming_pool:
            Swimming_pool=row_Swimming_pool.find_next_sibling('td')
            Swimming_pool=' '.join(Swimming_pool.get_text(strip=True).split())
            list_values_columns.append(Swimming_pool)
        else:
            Swimming_pool=None
            list_values_columns.append(Swimming_pool)

        row_Bulding_Condition=soup.find('th', string=re.compile(r"\s*Building condition\s*"))
        if row_Bulding_Condition:
            State_of_the_building=row_Bulding_Condition.find_next_sibling('td')
            State_of_the_building=' '.join(State_of_the_building.get_text(strip=True).split())
            list_values_columns.append(State_of_the_building)
        else:
            State_of_the_building=None
            list_values_columns.append(State_of_the_building)
        
        for key, value in zip(myDict.keys(), list_values_columns):
             myDict[key] = value

        return myDict
       
   
    print(create_data())
    
finally:
    
    driver.quit()