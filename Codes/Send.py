import smtplib
from email.mime.text import MIMEText
import time
import os.path

smtp_ssl_host = 'smtp.yandex.com.tr' #I used yandex smtp if you want another one change this.
smtp_ssl_port = 465
username = 'yourmail@example.com'
password = 'yourpassword'
sender = 'yourmail@example.com'

#READING EMAILS FROM emails.TXT FILE
def read_email(receive_list):
    email_file = input("Please enter emails file name :")
    if(os.path.exists(email_file)):  #File is exist or not exist ?
        print("Your emails files are : {} Please wait 2 sec file is reading...".format(email_file))
        time.sleep(2)
        f = open("emails.txt", "r")
        f1 = f.readlines()
        for mail in f1:
            receive_list.append(mail)
        return receive_list
    else:
        print("File doesn't exist.. Check your file name")
        quit()

#READING MESSAGE FROM message.txt
def read_message():     
    message_file = input("Please enter messages file name : ")
    if(os.path.exists(message_file)):  #File is exist or not exist ?
        print("Your file is = {} Please wait 2 sec file is reading...".format(message_file))
        time.sleep(2)
        f2 = open(message_file,"r")
        f3 = f2.readlines()
        for message in f3:
            return message
    else:
        print("File doesn't exist.. Check your file name")
        quit()
    
#SENDING E-MAIL
def send_email():
    liste = list()
    mails = read_email(liste)
    counter = 1 #How many e-mail sent ? we can see with counter.
    message = read_message()
    while(True):
        msg = MIMEText(message)
        msg['Subject'] = "Subject" #This is your Subject
        msg['From'] = sender 
        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(sender, mails, msg.as_string())
        server.quit()
        print("We've sent {} mails.. If you want to continue please press c or you want to quit please press q".format(counter))
        time.sleep(3)
        keyword = input("")
        if(keyword=="c"):
            counter+=1
        elif(keyword=="q"):
            print("We've sent {} Successfully now exiting...".format(counter))
            break
            


send_email()
            
        




