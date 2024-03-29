# import smtplib
# from email.mime.text import MIMEText

# def send_email(name, email, msg, phoneno):
#     sender_email = "email@gmail.com"  # Replace with your email address
#     recipients = ["devemchangani.co21d1@scet.ac.in"]  # Replace with the recipient's email address

#     # Create the message
#     message = MIMEText(msg + "\n" + str(phoneno))
#     message['From'] = email
#     message['To'] = ", ".join(recipients)
#     message['Subject'] = 'New message from ' + name + ' for Coding Blog'

#     # Connect to the SMTP server
#     smtp_server = "smtp.gmail.com"  # Replace with your SMTP server address
#     smtp_port = 587  # Replace with your SMTP port
#     smtp_username = "devemchangani.co21d1@scet.ac.in"  # Replace with your SMTP username
#     smtp_password = "gatv hmwr rggd awfc"  # Replace with your SMTP password

#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()  # Start TLS encryption
#         server.login(smtp_username, smtp_password)  # Login to the SMTP server
#         server.send_message(message)  # Send the email

# # Example usage
# if __name__ == "__main__":
#     name = "DC"
#     email = "dc@example.com"
#     msg = "Hello, how are you?"
#     phoneno = 1234567892

#     send_email(name, email, msg, phoneno)


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

def send_email(name, email, msg, phoneno):
    sender_name = "DC"  # Replace with the name you want to appear as the sender
    sender_email = "dc@example.com"  # Replace with your Gmail email address
    recipients = ["email"]  # Replace with the recipient's email address

    # Create the message container
    message = MIMEMultipart()
    message['From'] = formataddr((str(Header(sender_name, 'utf-8')), sender_email))
    message['To'] = ", ".join(recipients)
    message['Subject'] = 'New message from ' + name + ' for Coding Blog'

    # Add the message body
    body = msg + "\n" + str(phoneno)
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "email"  # Replace with your Gmail email address
    smtp_password = "pass"  # Replace with your application-specific password

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)

# Example usage
if __name__ == "__main__":
    name = "DC"
    email = "dc@example.com"
    msg = "Hello, how are you?"
    phoneno = 1234567892

    send_email(name, email, msg, phoneno)
