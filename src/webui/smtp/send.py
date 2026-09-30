import smtplib
from email.mime.text import MIMEText

# server
smtp_server = "localhost"  
port = 1025                
sender = "sender@example.com"
receiver = "receiver@example.com"

# content
message = MIMEText("test mail send from local server")
message["Subject"] = "Test Email to Local aiosmtpd Server"
message["From"] = sender
message["To"] = receiver

# establish connection then send mail
try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.sendmail(sender, receiver, message.as_string())
    print("Email successfully sent to the aiosmtpd server!")
except Exception as e:
    print(f"Failed to send email: {e}")