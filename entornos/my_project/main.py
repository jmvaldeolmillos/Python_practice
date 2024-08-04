"""Haha."""

import numpy as np
import requests


# Function to fetch data from a public API
def fetch_data(url):
    """Hello!"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()  # Assuming the API returns JSON data
        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


# Example usage of fetch_data
api_url = "https://jsonplaceholder.typicode.com/posts"
data = fetch_data(api_url)

if data:
    # Assuming each item in data is a dictionary, and we want to process some numeric field
    # Here we will mock a simple numeric transformation with numpy
    user_ids = [item["userId"] for item in data]  # Extracting userId as an example
    user_ids_array = np.array(user_ids)

    # Perform some basic numpy operations
    mean_user_id = np.mean(user_ids_array)
    std_dev_user_id = np.std(user_ids_array)

    print(f"Mean of user IDs: {mean_user_id}")
    print(f"Standard deviation of user IDs: {std_dev_user_id}")
