# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:03:18 2024

@author: karth
"""

import pandas as pd  # Import pandas for data manipulation

#from fetch_data import fetch_data  # Import fetch_data function from the fetch_data.py Script to get the output of the script
# Define the data transformation function
def transform_data(data):
    # Check if data exists
    if not data:
        print("No data to transform")  # Log if there's no data
        return None  # Return None if data is empty
    
    # Convert the dictionary to a DataFrame and reset the index
    df = pd.DataFrame.from_dict(data, orient='index').reset_index()
    
    # Rename columns for readability
    df.columns = ['cryptocurrency', 'price_usd']
    
    print("Data transformed successfully:", df)  # Log successful transformation
    return df  # Return the transformed DataFrame


# Fetch the data from the API(calling the fetch_data function located in the fetch_data.py script)
#data = fetch_data()

# Pass the fetched data to transform_data
#transformed_data = transform_data(data)