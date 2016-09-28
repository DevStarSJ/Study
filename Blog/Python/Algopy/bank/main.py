
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 16:36:27 2016

@author: 06411
"""

import transaction as ttt
import general_ledger as ggg
import Account as ddd
            
print(" create bank account  ")
ba = ggg.BankDepositAccount()
gl = ggg.GeneralLedger()
    
print(" issue deposit account ")
tr0 = ttt.Transaction(1,"issue",0,100)

print(" issue customer account ")
da = ddd.DepositAccount(tr0)
tr0.account_no = da.account_no
print(" DAlist ", da.dalist.get_DAList())

da.set_account(tr0)
ba.set_DepositAccout(tr0)
gl.set_GL(tr0)
print(" inquery customer account :",da.get_account())
print(" inquery deposit account  :",ba.get_DepositAccount())
print(" inquery general ledager  :",gl.get_GL())
print(" DAlist ", da.dalist.get_DAList())


print(" credit deposit account ")
tr1 = ttt.Transaction(1,"credit",1,100)
da.set_account(tr1)
ba.set_DepositAccout(tr1)
gl.set_GL(tr1)

print(" inquery customer account :",da.get_account())
print(" inquery deposit account  :",ba.get_DepositAccount())
print(" inquery general ledager  :",gl.get_GL())


print(" debt deposit accoutn ")
print(" debt deposit account ")

tr2 = ttt.Transaction(1,"debt",1,100)
da.set_account(tr2)
ba.set_DepositAccout(tr2)
gl.set_GL(tr2)
print(" inquery customer account :",da.get_account())
print(" inquery deposit account  :",ba.get_DepositAccount())
print(" inquery general ledager  :",gl.get_GL())

print(" create another bank account  ")
tr0 = ttt.Transaction(2,"issue",0,100)
da2 = ddd.DepositAccount(tr0)
print(da2.account_no)
tr0.account_no = da2.account_no

da2.set_account(tr0)
ba.set_DepositAccout(tr0)
gl.set_GL(tr0)

print(" inquery customer account :",da2.get_account())
print(" inquery deposit account  :",ba.get_DepositAccount())
print(" inquery general ledager  :",gl.get_GL())

print(" DAlist ", da.dalist.get_DAList())
print(" DAlist2 ", da2.dalist.get_DAList())