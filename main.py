# EMAIL CLIENT

import smtplib
import time
import sys

def chooseServer():
    gmailServerAddress = 'smtp.gmail.com:587'
    yahooServerAddress = 'smtp.mail.yahoo.com:587'
    outlookServerAddress = 'smtp-mail.outlook.com:587'
    hotmailServerAddress = 'smtp.live.com:587'
    aolServerAddress = 'smtp.aol.com:587'
    
    while True:
        print('''Choose a server to log into:
        [1]: Gmail
        [2]: Yahoo
        [3]: Outlook
        [4]: Hotmail/Live
        [5]: AOL
        ''')
        sc = input('Server: ').lower()

        if sc == '1' or 'gmail' in sc:
            server = smtplib.SMTP(gmailServerAddress)
            return server
            break
        elif sc == '2' or 'yahoo' in sc:
            server = smtplib.SMTP(yahooServerAddress)
            return server
            break
        elif sc == '3' or 'outlook' in sc:
            server = smtplib.SMTP(outlookServerAddress)
            return server
            break
        elif sc == '4' or 'hotmail' in sc or 'live' in sc:
            server = smtplib.SMTP(hotmailServerAddress)
            return server
            break
        elif sc == '5' or 'aol' in sc:
            server = smtplib.SMTP(aolServerAddress)
            return server
            break
        else:
            print("Please choose a valid option! Try again.\n")
            True

def login(user, passw, server):
    try:
        server.ehlo()
        server.starttls()
        server.login(user, passw)
    except:
        errorLoginFailed()

def errorLoginFailed():
    global server
    print("Login failed. Your email address or password is incorrect. Try again.")
    print("\nEnter your email address and password.\nNOTE: Password will be visible.\n")
    user = input('Email address: ')
    passw = input('Password: ')
    login(user, passw, server)

def composeMessage():
    sub = input('\nMessage Subject: ')
    print("Compose message (Press Enter then Ctrl+D when done):")
    txt = sys.stdin.read()
    msg = 'Subject: {}\n\n{}'.format(sub, txt)
    return msg

def sendMail(server,user,receiver,msg):
    try:
        server.sendmail(user,receiver,msg)
        print("Email sent!")
    except:
        errorReciever()

def errorReceiver():
    global server
    global user
    global msg
    print("Message could not be sent. Receiver address does not exist. Try again.")
    print("\nEnter the receiver(s) address(es) (if more than one, separate with a space).")
    receiver = input()
    if ' ' in receiver:
        receiver = receiver.split()
    sendMail(server,user,receiver,msg)



print("-- EMAIL CLIENT --\n")

server = chooseServer()

print("\nEnter your email address and password.\nNOTE: Password will be visible.\n")
user = input('Email address: ')
passw = input('Password: ')
login(user, passw, server)

msg = composeMessage()

print("\nEnter the receiver(s) address(es) (if more than one, separate with a space).")
receiver = input()
if ' ' in receiver:
    receiver = receiver.split()
sendMail(server,user,receiver,msg)

time.sleep(1)

while True:
    print("\nPress 1 to send another email.")
    print("Press 2 to log into another account.")
    print("Press 3 to log out and quit.")
    action = input()
    if action == '1':
        msg = composeMessage()
        print("\nEnter the receiver(s) address(es) (if more than one, separate with a space).")
        receiver = input()
        if ' ' in receiver:
            receiver = receiver.split()
        sendMail(server,user,receiver,msg)
        True
    elif action == '2':
        server.quit()
        server = chooseServer()
        print("\nEnter your email address and password.\nNOTE: Password will be visible.\n")
        user = input('Email address: ')
        passw = input('Password: ')
        login(user, passw, server)
        msg = composeMessage()
        print("\nEnter the receiver(s) address(es) (if more than one, separate with a space).")
        receiver = input()
        if ' ' in receiver:
            receiver = receiver.split()
        sendMail(server,user,receiver,msg)
        True
    elif action == '3':
        server.quit()
        print("Logged out.")
        sys.exit(0)
    else:
        print("Choose a valid option.")
        True
