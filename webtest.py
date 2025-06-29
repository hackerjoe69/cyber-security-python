# Full Penetration Testing Script

import requests
from bs4 import BeautifulSoup
import nmap
import os

# Function to test for SQL Injection using sqlmap
def sql_injection_test(url):
    print("\n[+] Running SQL Injection Test...")
    sqlmap_command = f"sqlmap -u {url} --batch --level=5 --risk=3"
    os.system(sqlmap_command)

# Function to scan for open ports using nmap
def port_scan(target):
    print("\n[+] Running Port Scan...")
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')
    for host in nm.all_hosts():
        print(f"    ↳ Host: {host}")
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                state = nm[host][proto][port]['state']
                print(f"        Port {port}/{proto} is {state}")

# Function to test for XSS vulnerabilities
def xss_test(url):
    print("\n[+] Testing for XSS Vulnerabilities...")
    payloads = ["<script>alert('XSS')</script>", "'><img src=x onerror=alert(1)>"]
    for payload in payloads:
        try:
            response = requests.get(url + "?search=" + payload, timeout=5)
            if payload in response.text:
                print(f"    ✅ XSS vulnerability found with payload: {payload}")
        except Exception as e:
            print(f"    [!] XSS test failed: {e}")

# Function to check for sensitive files
def sensitive_file_check(url):
    print("\n[+] Checking for Sensitive Files...")
    sensitive_files = ["/.env", "/config.php", "/backup.zip"]
    for file in sensitive_files:
        full_url = url.rstrip("/") + file
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                print(f"    ⚠️ Sensitive file found: {full_url}")
        except Exception as e:
            print(f"    [!] Failed to access {full_url}: {e}")

# Function to check user authentication
def user_authentication_test(url):
    print("\n[+] Testing for Weak Authentication...")
    login_url = url.rstrip("/") + "/login"
    credentials = [("admin", "password"), ("user", "password")]
    for username, password in credentials:
        try:
            response = requests.post(login_url, data={"username": username, "password": password}, timeout=5)
            if "Welcome" in response.text or "Dashboard" in response.text:
                print(f"    ✅ Logged in as {username} with weak password.")
        except Exception as e:
            print(f"    [!] Auth test failed: {e}")

# Function to analyze logs for errors
def log_analysis(log_file):
    print("\n[+] Analyzing Logs...")
    try:
        with open(log_file, 'r') as file:
            logs = file.readlines()
            for log in logs:
                if "ERROR" in log.upper():
                    print(f"    ⚠️ Error in logs: {log.strip()}")
    except FileNotFoundError:
        print(f"    [!] Log file {log_file} not found.")

# Entry Point
if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g., http://example.com): ").strip()

    sql_injection_test(target_url)
    port_scan(target_url.replace("http://", "").replace("https://", "").split('/')[0])  # Extract hostname for Nmap
    xss_test(target_url)
    sensitive_file_check(target_url)
    user_authentication_test(target_url)
    log_analysis("server.log")  # Ensure this exists locally if needed
    print("\n[+] Penetration testing completed.")
    print("[+] Review the output for vulnerabilities and issues found.")