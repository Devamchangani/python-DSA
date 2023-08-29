import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, proxy_ip, proxy_port, subject, message):
    try:
        with smtplib.SMTP(proxy_ip, proxy_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Email sent to {recipient_email} using proxy {proxy_ip}:{proxy_port}")
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {e}")

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'devemchangani.co21d1@scet.ac.in'
sender_password = 'lzaczyekwblnmnkl'
subject = 'Subject of the Email'
message = 'Hello, this is the body of the email!'
recipient_emails = ['devamchangani@gmail.com', 'devamchangani812@gmail.com', 'sd.empiricinfotech1@gmail.com']
proxy_ips = ['2.56.119.93', '185.199.229.156', '185.199.228.220']
proxy_ports = [5074, 7492, 7300]  # Replace with actual proxy ports

for recipient_email, proxy_ip, proxy_port in zip(recipient_emails, proxy_ips, proxy_ports):
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    send_email(sender_email, sender_password, recipient_email, proxy_ip, proxy_port, subject, message)

print("All emails sent.")
