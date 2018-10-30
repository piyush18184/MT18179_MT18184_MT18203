# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:02:26 2018

@author: lenovo
"""

class patient:
    def __init__(self,P_ID,P_Name,P_Age,P_Email,P_PNo,P_Add,P_Gender):
        self.P_ID=P_ID
        self.P_Name=P_Name
        self.P_Age=P_Age
        self.P_Email=P_Email
        self.P_PNo=P_PNo
        self.P_Add=P_Add
        self.P_Gender=P_Gender
        
    def getpatientname(self):
        for name in self.P_Name:
            print(name)
            
    def getpatientemail(self):
        for email in self.P_Email:
            print(email)       
        
    def getpatientphone(self):
        for phone in self.P_PNo:
            print(phone)
            
    def getpatientaddress(self):
        for address in self.P_Add:
            print(address)        
    
    def getpatientid(self):
        for ids in self.P_ID:
            print(ids)
            
    def getpatientage(self):
        for age in self.P_Age:
            print(age) 
            
    def getpatientgender(self):
        for gen in self.P_Gender:
            print(gen)
            