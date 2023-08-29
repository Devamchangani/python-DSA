import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import time

def send_email(sender_email, sender_password, recipient_email, proxy_ip, proxy_port, subject, message):
    try:
        with smtplib.SMTP(proxy_ip, proxy_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Email sent to {recipient_email} using proxy {proxy_ip}:{proxy_port}")
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {e}")

# Email configuration
sender_email = 'devemchangani.co21d1@scet.ac.in'
sender_password = 'cfyvquvbmgjvvjvz'
subject = 'Subject of the Email'
message = 'Hello, this is the body of the email!'
recipient_emails = ['devamchangani@gmail.com', 'devamchangani812@gmail.com', 'sd.empiricinfotech1@gmail.com']
proxy_ips = ['2.56.119.93', '185.199.229.156', '185.199.228.220']
proxy_ports = [5074, 7492, 7300]  # Replace with actual proxy ports

for recipient_email in recipient_emails:
    # Choose a proxy randomly from the list
    proxy_index = random.randint(0, len(proxy_ips) - 1)
    proxy_ip = proxy_ips[proxy_index]
    proxy_port = proxy_ports[proxy_index]

    # Create the email content and send email
    send_email(sender_email, sender_password, recipient_email, proxy_ip, proxy_port, subject, message)

    # Add a delay before sending the next email (to avoid overloading)
    time.sleep(5)  # Adjust the delay duration as needed

print("All emails sent.")
