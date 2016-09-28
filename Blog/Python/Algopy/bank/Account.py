# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 12:09:56 2016

@author: 06411
"""


import AccountNumber as an

class DepositAccount(object) :
    
    def __init__(self,tr) :
        
        if tr.event == 'issue' :
            self.account_no = an.Account_Nubmer.get_AN()
        else :
            self.account_no = tr.account_no
        self.amount = 0
        self.dalist_no =0
        self.dalist = DAList(self.account_no,self.get_dalist(),tr.event,tr.amount)
            

    def get_account(self) :
        return (self.account_no,self.amount)
        
    def get_dalist(self) :
        self.dalist_no +=1
        return self.dalist_no
            
    def set_account(self,tr) :
        
        if tr.event == "issue" :
            pass
        else : 
            self.dalist = DAList(self.account_no,self.get_dalist(),tr.event,tr.amount)
        
        if tr.event == 'debt' :
            self.amount -= tr.amount
        else :
            self.amount += tr.amount
                
class DAList(object) :
    dalist= list()
    def __init__(self,account_no,no,event,amount) :
        self.account_no = account_no
        self.no = no
        self.event = event
        self.amount = amount
        self.dalist.append(self)
    
    def get_DAList(self) :
        v = []
        for ll  in self.dalist :
            v.append(ll.__dict__)
        return v
            