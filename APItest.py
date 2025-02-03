# API Penetration Testing Script

import requests

# Define the target API endpoint
api_url = "https://example.com/api"

# Define a list of common endpoints to test
endpoints = [
    "/users",
    "/admin",
    "/login",
    "/register",
    "/data",
]

# Function to test endpoints
def test_endpoints():
    for endpoint in endpoints:
        url = api_url + endpoint
        response = requests.get(url)
        
        print(f"Testing {url} - Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("Success: Accessible endpoint.")
        elif response.status_code == 401:
            print("Unauthorized: Access denied.")
        elif response.status_code == 403:
            print("Forbidden: Access forbidden.")
        elif response.status_code == 404:
            print("Not Found: Endpoint does not exist.")
        else:
            print("Error: Unexpected status code.")

# Run the test
if __name__ == "__main__":
    test_endpoints()
