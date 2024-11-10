import requests

# Define the data extraction function
def fetch_data():
    # Set the API URL to fetch Bitcoin price in USD from CoinGecko
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print("Data fetched successfully:", data)  # Log success
        return data  # Return the fetched data
    else:
        print("Failed to fetch data")  # Log failure
        return None  # Return None if request failed


# Uncomment the below calling function to get the outputs on the console
# fetch_data()
