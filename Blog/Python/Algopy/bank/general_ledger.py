# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 16:15:51 2016

@author: 06411
"""

class BankDepositAccount(object) :
    def __init__(self) :
        self.account_code = 1
        self.debtamount =0
        self.creditamount= 0
        
    def get_DepositAccount(self) :
        return (self.account_code,self.debtamount, self.creditamount)
        
    def set_DepositAccout(self, tr) :
        print('tr_event', tr.event)
        if tr.event == "debt" :
            self.debtamount += tr.amount
        else :
            self.creditamount += tr.amount
            
class GeneralLedger(object) :
    def __init__(self) :
        self.GL_account =1
        self.GL_debt =0
        self.GL_credit =0
        
    def get_GL(self) :
        return (self.GL_account, self.GL_debt, self.GL_credit)
        
    def set_GL(self,tr) :
        
        if tr.event == "debt" :
            self.GL_debt += tr.amount
        else :
            self.GL_credit += tr.amount