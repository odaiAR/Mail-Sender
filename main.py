import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(LstOfReceivers):
    sender = "htzone.club@gmail.com"
    password = "htzone2022"
    print("login into your gmail account", sender, "in ur browser and make sure that its the account that ur "
                                                   "currently on")
    print("less security is already enabled so don't worry, i've done that for you :)")
    link = 'https://accounts.google.com/b/0/DisplayUnlockCaptcha'
    print("press on this link : ", link, "then click on continue")
    print("if you did all the previous steps press enter to continue")
    input()
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(sender, password)
    print("login success")
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "ht-zone invitation"
    msg['From'] = sender
    msg['To'] = LstOfReceivers[0]
    text = "Hi!\nhow are you?\n"
    html = """\
    <html>
      <head></head>
      <body>
        <p style="color:black;font-size:16px"> 
            <img src = "cid:image1" alt = "Logo" title = "htzone" width = "350" style = "vertical-align:middle;margin:0px 25%">
            <br>
            <br>
        מאחלים לכם שנה טובה ומתוקה,<br>     
             אנו שמחים להודיע לכם שחברת Siraj Technologies הצטרפה לקבוצת חברות מועדון שלנו.<br>
             בהיותכם עובדי החברה הנכם זכאים להטבה בשווי 250 ש"ח בקנייה הראשונה המוענקת מחברת סיראג', <br>
              ובכל קנייה נוספת תצברו נקודות.<br>
              ** מנוי בחינם <br>
              להרשמה וקבלת ההטבה >>>> <a href="http://htzone.club">http://htzone.club</a>
        </p>
      </body>
    </html>
    """
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    fp = open('htzone.jpg', 'rb')
    msgImage = MIMEImage(fp.read(), name='htzone.jpg')
    fp.close()
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)
    smtp.sendmail(sender, LstOfReceivers, msg.as_string())
    smtp.quit()
    print("email has been sent to ", LstOfReceivers)


print(
    "Please insert a list of mails that you want to phish, please make sure mails are space separated and press enter "
    "when you are done")
string = input()
ListofReceivers = string.split(" ")
print(string)
send_mail(ListofReceivers)
print("mail sent successfully")
