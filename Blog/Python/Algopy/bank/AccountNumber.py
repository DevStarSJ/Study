
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 16:58:53 2016

@author: 06411
"""


class Account_Nubmer(object) :
    _Account_No = 0
    @classmethod
    def set_AN(cls) :
        cls._Account_No  +=1
        
    @classmethod
    def get_AN(cls) :
        if not cls._Account_No  :
            cls.set_AN()
        return cls._Account_No 