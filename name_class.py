# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:14:09 2018

@author: natalial
"""

class NameClass (object):
    
    def __init__(self, n1, n2):  
        self.first_name = n1
        self.last_name = n2
    
    def say_hello(self):
       speech = f'Hello Dear {self.first_name} {self.last_name}! ' + \
       f'Ok {self.first_name}, let`s start!'

       return speech
 