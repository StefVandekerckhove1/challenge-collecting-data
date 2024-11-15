# challenge-collecting-data

## 1. Description

In order to create our machine learning model ImmoEliza, we created a script that collects data of different estates on ImmoWeb such as: Locality, Type of property (House/apartment), Subtype of property (Bungalow, Chalet, Mansion, ...), Price, Type of sale (Exclusion of life sales), Number of rooms, Living Area, Fully equipped kitchen (Yes/No), Furnished (Yes/No), Open fire (Yes/No), Terrace (Yes/No) If yes: Area, Garden (Yes/No) If yes: Area, Surface of the land, Surface area of the plot of land, Number of facades, Swimming pool (Yes/No), State of the building (New, to be renovated, ...).
Our script returns a csv file with the required data for each property.

## 2. Installation

Our script requires the installation of following packages:
multiprocessing, selenium, beautifulsoup4, requests, time, re, pandas

## 3. Usage

Our script builds a dataset gathering information of 10.000 properties of ImmoWeb and stores it in a csv file.

## 4. Visuals

![GIF](https://www.breakthroughbroker.com/img/site_specific/uploads/Animated_GIF-downsized.gif)
## 5. Contributors

Imad, Vera, Stef

## 6. Timeline

| Tuesday 12/11              | Wednesday 13/11          | Thursday 14/11         |Friday 15/11    |
| ---------------------------| -------------------------|------------------------|----------------|
| Creation of repo           | adding number_of_facades to'create_data()' |adding concurrency to 'create_data()' |writing the README
| 'create_data()' function   | adding conditions to 'create_data()' |storing the data in columns in a csv|cleaning of data| testing and improving concurrency 
| 'Immo_get_urls.py'         | scraping urls with 'Immo_get_urls.py'  | check included if url link is valid  |

## 7. Presentation
### 7.1 How did we do it?

1) First, we divided the tasks for everyone:
   - Vera did the scraping of the required information on Immoweb for one estate
   - Imad worked on scraping urls of Immoweb
   - Stef tested the code on bugs 

2) Each worked at his own task.
3) Once someone finished their part, they pushed it on the github repo.
4) We improved the code by testing and debugging.
   
### 7.2 Who did what?

Vera:
- Prepared the function 'create_data(url)' in 'First_step_collecting_data_from_a_page.py' to extract the required information of an estate.
- Added multiprocessing to the function 'create_data(url)' to shorten the requesttime.
- cleaning the data

Imad:
- Prepared the scripts 'Immo_get_urls.py' which generated 'property_urls_1_to_333_apartment.csv' and 'property_urls_1_to_333_house.csv' containing a list of urls scraped from ImmoWeb.be,
- Prepared 'Immo_scraping.py' for scraping the urls retreived from the 'Immo_get_urls.py' file and storing the information in 'immoweb_data.csv'

Stef:
- Prepared the git repo + README
- Added the number of facades condition to  the 'create_data()' function
- Tested the 'create_data()' function on different URL links of ImmoWeb

### 7.3 What went wrong?

- During the scraping of different estates with 'create_data()' we encountered problems with urls not containing specific information like 'Number of facades', 'Surface of the land' and 'Surface area of the plot of land', 'Type of sale', 'State of the building'.
- We encountered issues during the multiprocessing of several urls on ImmoWeb.

### 7.4 How did we solve it?

- We added conditions to the 'create_data()' function for if some information was missing, the information was added as 'None' or 'No'.
- In the 'Immo_get_urls.py' there is a check included for if the url link is not valid.

