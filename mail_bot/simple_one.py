import smtplib

try:  # you can make this varibles as evniron variable as they contain sensitive information
    Email_Address = input('Email Address: ')
    Password = input("Password: ")
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(Email_Address, Password)

    sender_mail_address = input("Enter sender mail address: ")
    name = input("Person's Name: ")
    print("If you add addition information then, enter Y for yes or any key for no: ")
    a = input()
    if a == "Y":
        addition_info = input('info: ')
        msg = f'Hi {name},\n{addition_info}'
    else:
        msg = f'Hi {name}'

    smtp.sendmail(Email_Address, sender_mail_address, msg)
    print("Mail successfully send")
except:
    print('Email failed to send')
"""https://myaccount.google.com/u/0/lesssecureapps?pli=1 
   go through  this link and set 'Allow less secure apps' option on but after completing the work set it off for security reasons."""