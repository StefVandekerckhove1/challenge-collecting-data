import pandas as pd
import numpy as np
import re
import string


df=pd.read_csv("immoweb_data.csv")

empty_cell_type_locality=df['Type of property'].isnull().sum()        #128
df['Type of property']=df["Type of property"].fillna('House')

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


empty_cell_Swimming_pool=df['Swimming pool'].isnull().sum()  
df['Swimming pool']=df['Swimming pool'].fillna('None')

empty_cell_=df['State of the building'].isnull().sum()  
df['State of the building']=df['State of the building'].fillna('None')

empty_cell_Code_Immoweb=df['Code Immoweb'].isnull().sum()  
df["Code Immoweb"]=df['Code Immoweb'].fillna('None')




#Create a new column with the values of th Type of Sale
# we keep here only tenement building
df['Tenement building'] = df.loc[:, 'Type of Sale']

df['Tenement building'] = df['Tenement building'].astype(str).str.strip().str.lower()

df['Tenement building'] = df['Tenement building'].replace({'yes': 1, 'no': 0})


df['Tenement building'] = df['Tenement building'].replace({
    "('under option', 'no')": 'None',
    "('under option', 'yes')": 'None',
    "('public sale', 'yes')": 'None',
    "('public sale', 'no')": 'None'
})

#In this one we keep only unde option/public sale
df['Type of Sale']=df['Type of Sale'].astype(str).str.strip().str.lower()
df['Type of Sale'] = df['Type of Sale'].replace({'yes': 'None', 'no': 'None'})


df=df.drop_duplicates(subset=['Code Immoweb'])

df.to_csv('blavla.csv')