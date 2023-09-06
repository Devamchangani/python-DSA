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
sender_email = 'your_email@example.com'
sender_password = 'your_email_password'
subject = 'Subject of the Email'
message = 'Hello, this is the body of the email!'
recipient_emails = ['recipient1@example.com', 'recipient2@example.com', 'recipient3@example.com']
proxy_ips = ['proxy1_ip', 'proxy2_ip', 'proxy3_ip']
proxy_ports = [proxy1_port, proxy2_port, proxy3_port]  # Replace with actual proxy ports

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
