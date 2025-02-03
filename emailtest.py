import smtplib

def send_test_email(sender_email, receiver_email, smtp_server, smtp_port):
    message = """\
    Subject: Test Email for Penetration Testing
    This is a test email for penetration testing purposes."""
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.sendmail(sender_email, receiver_email, message)
            print("Test email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")

send_test_email('cyberdon43@gmail.com', 'josephdeyon3@gmail.com', 'smtp.gmail.com', 587)
