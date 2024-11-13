import csv 
from First_step_collecting_data_from_a_page import create_data
data = create_data()

def import_csv(data):
    with open('data_collection.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in data.items():
            writer.writerow([key, value])

import_csv(data)
