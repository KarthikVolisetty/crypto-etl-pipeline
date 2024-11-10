# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 23:11:27 2024

@author: karth
"""

import psycopg2
import pandas as pd

# import the transform_data and fetch_data from the scripts to call the functions
#from transform_data import transform_data
#from fetch_data import fetch_data

# Define sample data
df = pd.DataFrame({
    'cryptocurrency': ['Bitcoin', 'Ethereum'],
    'price_usd': [34000.50, 1800.75]
})

# Define the data loading function
def load_data(df):
    if df is None:
        print("No data to load")
        return
    
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",       # local machine IP: 192.168.56.1
        database="cryptodata",
        user="postgres",
        password="Karthik@1261"
    )
    cursor = conn.cursor()

    # Create table if it does not exist
    create_table = """
    CREATE TABLE IF NOT EXISTS prices (
        cryptocurrency VARCHAR(50),
        price_usd FLOAT
    );
    """
    cursor.execute(create_table)
    conn.commit()

    # Insert data into the table
    for _, row in df.iterrows():
        cursor.execute("INSERT INTO prices (cryptocurrency, price_usd) VALUES (%s, %s)", 
                       (row['cryptocurrency'], row['price_usd']))
    conn.commit()

    # Close database connection
    cursor.close()
    conn.close()
    print("Data loaded successfully")

# uncomment the below Calling functions to load data to get the output in console
#data = fetch_data()
#df = transform_data(data)
#load_data(df)
