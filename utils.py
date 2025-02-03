import requests
import re
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def send_request(url, payload):
    """
    Send an HTTP GET request with a given payload to the target URL.
    """
    try:
        response = requests.get(url + payload, timeout=5)
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        return None

def is_vulnerable(response):
    """
    Check the response content for common SQL error patterns.
    """
    error_patterns = [
        "you have an error in your sql syntax",
        "warning: mysql",
        "unclosed quotation mark",
        "quoted string not properly terminated",
        "ORA-01756"
    ]
    if response:
        for pattern in error_patterns:
            if re.search(pattern, response.text, re.IGNORECASE):
                return True
    return False
