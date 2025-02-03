import subprocess

def test_sql_injection(target_url):
    # Run sqlmap to test for SQL injection vulnerabilities
    command = f"sqlmap -u {target_url} --batch --risk=3 --level=5"
    subprocess.run(command, shell=True)

target_url = 'http://tiktok.com/vulnerable_page.php?id=1'  # Replace with target URL
test_sql_injection(target_url)
