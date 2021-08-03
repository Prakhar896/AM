import smtplib, ssl
import time

port = 465  # For SSL
sender_email = input("Enter your email: ")
password = input("Type your password and press enter: ")
print('Logging in...')

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    try:
        server.login(sender_email, password)
    except:
        print('Auth error. Please enter password correctly.')
        exit()
        
    # TODO: Send email here
    receiver_email = input('Enter recipient email: ')
    message = 'Subject: {}\n\n{}'.format('ROUND 2', 'HWHHEHEHEEHEH gotem\nhaha get rekt')
    try:
        server.sendmail(sender_email, receiver_email, message)
    except:
        print('Error occurred in sending mail. Program failed.')
    print('Email sent!')