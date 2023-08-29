import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'devemchangani.co21d1@scet.ac.in'
sender_password = 'cfyvquvbmgjvvjvz'
subject = 'Subject of the Email'
message = 'Hello'

# List of recipient emails
recipient_emails = ['devamchangani@gmail.com', 'devamchangani812@gmail.com', 'sd.empiricinfotech1@gmail.com']

# List of proxy IPs EMAIL

proxy_ips = ['2.56.119.93:5074', '185.199.229.156:7492', '185.199.228.220:7300']

for recipient_email, proxy_ip in zip(recipient_emails, proxy_ips):
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Establish a proxy connection
    # proxy = {
    #     "http": f"http://{proxy_ip}",
    #     "https": f"http://{proxy_ip}",
    # }

    session = requests.Session()
    session.proxies = {
        "http": f"http://{proxy_ip}",
        "https": f"http://{proxy_ip}",
    }

    # Send the email using SMTP with the proxy
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print(f"Email sent to {recipient_email} using proxy {proxy_ip}")
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {e}")
