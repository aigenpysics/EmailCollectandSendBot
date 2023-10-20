import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create a MIME message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add the message content
    msg.attach(MIMEText(message, 'plain'))

    # Create a SMTP session
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)


recipient_email = 'asap____@naver.com'  # Assuming email address is in the first column
#Debug
#print(f"{idx+1}, {recipient_email}")
subject = "근호형님에게 ..."  # Set your desired email subject
message = "여소좀 ㅎ"  # Set your desired email message

# Set your sender email and password
sender_email = 'gimjeongheon38@gmail.com'
sender_password = 'zkcbxmysbswlolqy'

# Call the function to send the email
send_email(sender_email, sender_password, recipient_email, subject, message)
