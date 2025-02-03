import requests
from bs4 import BeautifulSoup

def check_vulnerability(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"Scanning {url} for vulnerabilities...")
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Basic checks for information leakage
            if "admin" in soup.text.lower():
                print("Potential admin panel found!")
            if "error" in soup.text.lower():
                print("Error messages detected, potential information leakage.")
            
            # Check for security headers
            security_headers = ['X-Frame-Options', 'Content-Security-Policy', 'X-Content-Type-Options']
            for header in security_headers:
                if header not in response.headers:
                    print(f"Missing security header: {header}")

        else:
            print(f"Failed to access {url}, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_url = input("Enter the URL to scan: ").strip()
    if target_url:
        check_vulnerability(target_url)
    else:
        print("Invalid URL. Please try again.")
