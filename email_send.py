import smtplib


def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('tiusoro@gmail.com', 'wcih wcih wcih wcih')
    server.sendmail('tiusoro@gmail.com', 'pythonelearning101@gmail.com' , 'This is basically to test Email Automation')
    server.close()
    print("Email Successfully sent")
    
    
sendEmail()



