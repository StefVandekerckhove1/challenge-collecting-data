import pandas as pd
import numpy as np
import re
import string


df=pd.read_csv("immoweb_data_house.csv")

#df = df.iloc[:, :-1]

df = df.dropna(subset=[df.columns[0], df.columns[1]])

empty_cell_type_locality=df['Type of property'].isnull().sum()        #128
df['Type of property']=df["Type of property"].fillna('Apartment')

# print(df.head())

empty_cell_subtype=df['Subtype of property'].isnull().sum()    #7691
df['Subtype of property']=df['Subtype of property'].fillna('None')

empty_cell_price=df['Price'].isnull().sum()       #138
df['Price']=df['Price'].fillna('None')

empty_cell_Number_of_rooms=df['Number of rooms'].isnull().sum()    #1
df['Number of rooms']=df['Number of rooms'].fillna('None')

empty_cell_Living_Area=df['Living Area'].isnull().sum()    #220
df['Living Area']=df['Living Area'].fillna('None')

empty_cell_Fully_kitchen=df['Fully equipped kitchen'].isnull().sum()  #0
df['Fully equipped kitchen']=df['Fully equipped kitchen'].fillna('None')

empty_cell_Furnished=df['Furnished'].isnull().sum() 
df['Furnished']=df['Furnished'].fillna('None')


empty_cell_Open_fire=df['Open fire'].isnull().sum()   #128
df['Open fire']=df['Open fire'].fillna('None')
 
empty_cell_Terrace=df['Terrace'].isnull().sum()    #128
df['Terrace']=df['Terrace'].fillna('None')

empty_cell_Garden=df['Garden'].isnull().sum()    #5930
df['Garden']=df['Garden'].fillna('None')


empty_cell_Surface_of_the_land=df['Surface of the land'].isnull().sum()   # #5930
df['Surface of the land']=df['Surface of the land'].fillna('None')


empty_cell_Surface_of_the_plot_of_land=df['Surface area of the plot of land'].isnull().sum()  
df['Surface area of the plot of land']=df['Surface area of the plot of land'].fillna('None')


empty_cell_Number_of_facades=df['Number of facades'].isnull().sum()     #2031
df['Number of facades']=df['Number of facades'].fillna('None')


#empty_cell_Swimming_pool=df['Swimming pool'].isnull().sum()  
#df['Swimming pool']=df['Swimming pool'].fillna('None')

empty_cell_=df['State of the building'].isnull().sum()  
df['State of the building']=df['State of the building'].fillna('None')
df['State of the building'] = df['State of the building'].str.lower()
df['State of the building'] = df['State of the building'].replace({'as new': 5,'just renovated': 4,'good': 3,'to renovate': 2,'to be done up': 1, 'to restore': 0})


empty_cell_Code_Immoweb=df['Code Immoweb'].isnull().sum()  
df["Code Immoweb"]=df['Code Immoweb'].fillna('None')
df['Code Immoweb'] = pd.to_numeric(df['Code Immoweb'], errors='coerce').fillna(0).astype(int)


#Create a new column with the values of th Type of Sale
# # we keep here only tenement building
df['Tenement building'] = df.loc[:, 'Type of Sale']
df['Tenement building'] = df['Tenement building'].astype(str).str.strip().str.lower()
df['Tenement building'] = df['Tenement building'].replace({'yes': 1, 'no': 0})
df['Tenement building'] = df['Tenement building'].replace({
    "('under option', 'yes')": 1,
    "('under option', 'no')": 0,
    "('public sale', 'yes')": 1,
    "('public sale', 'no')": 0,
    "('Online sale', 'Yes')":1,
    "('Online sale', 'No')":0
})

df['Type of Sale']=df['Type of Sale'].fillna('None')
df['Type of Sale'] = df['Type of Sale'].astype(str).str.strip().str.lower()
df['Type of Sale'] = df['Type of Sale'].replace({
    "('under option', 'yes')": 1,
    "('under option', 'no')": 1,
    "('public sale', 'yes')": 2,
    "('public sale', 'no')": 2,
    "('Online sale', 'Yes')":3,
    "('Online sale', 'No')":3
})

df=df.drop_duplicates(subset=['Code Immoweb'])

df.reset_index(drop=True, inplace=True)

df.to_csv('Cleaned_data_house.csv')