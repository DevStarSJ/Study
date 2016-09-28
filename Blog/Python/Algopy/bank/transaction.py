# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 16:18:08 2016

@author: 06411
"""

class Transaction(object) :
    def __init__(self,tr_no,event,account_no,amount):
        self.tr_no = tr_no
        #event :debt, credit,issue
        self.account_no = account_no
        self.event = event
       
        self.amount = amount
       
    def get_Transaction(self) :
        return (self.tr_no, self.event, self.account_no, self.amount)
        