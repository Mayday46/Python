import smtplib
from Credentials import myEmail, emailPassword
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart





# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()  # Secure the connection
# connection.login(user= myEmail, password=emailPassword)
# connection.sendmail(from_addr=myEmail, to_addrs=myEmail, msg="test test")
# connection.close()


# def sendMail(message):
#     connection = smtplib.SMTP("smtp.gmail.com")
#     connection.starttls()  # Secure the connection
#     connection.login(user= myEmail, password=emailPassword)
#     connection.sendmail(from_addr=myEmail, to_addrs=myEmail, msg=message)
#     connection.close()

def sendMail(article):
    # Create the email message
    message = MIMEMultipart()
    message['From'] = myEmail
    message['To'] = myEmail
    message['Subject'] = 'Stock Price Alert'

    # Add the article content
    message.attach(MIMEText(article, 'plain', 'utf-8'))

    # Send the email
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()  # Secure the connection
    connection.login(user=myEmail, password=emailPassword)
    connection.sendmail(from_addr=myEmail, to_addrs=myEmail, msg=message.as_string())
    connection.close()
