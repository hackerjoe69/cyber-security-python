import os
from utils import send_request, is_vulnerable

def load_payloads(file_path):
    """
    Load SQL injection payloads from a file.
    """
    if not os.path.exists(file_path):
        print(f"Payload file {file_path} not found.")
        return []
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# loads = load_payloads("payloads.txt")

# for load in loads:
#     print(load)

def test_sql_injection(url):
    """
    Test the target URL for SQL injection vulnerabilities.
    """
    payloads = load_payloads("payloads.txt")
    if not payloads:
        return
    
    print(f"Testing URL: {url} for SQL injection vulnerabilities...")
    
    for payload in payloads:
        print(f"Trying payload: {payload}")
        response = send_request(url, payload)
        if is_vulnerable(response):
            print(f"[!] Potential SQL Injection vulnerability found with payload: {payload}")
            return
        else:
            print(f"No payload found for {payload}")
    print("[+] No vulnerabilities detected.")

if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g., http://example.com/page?id=): ")
    test_sql_injection(target_url)
