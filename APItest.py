# API Penetration Testing Script

import requests

# Define a list of common endpoints to test
endpoints = [
    "/users",
    "/admin",
    "/login",
    "/register",
    "/data",
]

# Function to test endpoints
def test_endpoints(api_url):
    print(f"\n[*] Testing API base: {api_url}")
    for endpoint in endpoints:
        url = api_url + endpoint
        try:
            response = requests.get(url, timeout=5)
            print(f"\n[+] Testing {url}")
            print(f"    ↳ Status Code: {response.status_code}")
            
            if response.status_code == 200:
                print("    ✅ Success: Accessible endpoint.")
            elif response.status_code == 401:
                print("    🔒 Unauthorized: Access denied.")
            elif response.status_code == 403:
                print("    ⛔ Forbidden: Access forbidden.")
            elif response.status_code == 404:
                print("    ❌ Not Found: Endpoint does not exist.")
            else:
                print("    ⚠️  Unexpected status code.")
        except requests.exceptions.RequestException as e:
            print(f"    ❌ Request failed: {e}")

# Run the test
if __name__ == "__main__":
    domain = input("Enter the target domain (e.g., https://example.com): ").strip().rstrip('/')
    api_url = domain + "/api"
    test_endpoints(api_url)
