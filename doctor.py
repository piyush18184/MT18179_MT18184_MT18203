# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 21:26:14 2018

@author: lenovo
"""

class doctor:
    def __init__(self,D_ID,D_Name,D_Email,D_PNo,D_Add,D_department,D_opd_time,D_types,D_specialization):
        self.D_ID=D_ID
        self.D_Name=D_Name
        self.D_Email=D_Email
        self.D_PNo=D_PNo
        self.D_Add=D_Add
        self.D_department=D_department
        self.D_opd_time=D_opd_time
        self.D_types=D_types
        self.D_specialization=D_specialization
    
    def getdocid(self):
        for ids in self.D_ID:
            print(ids)
            
    def getdocname(self):
        for name in self.D_Name:
            print(name)
            
    def getdocemail(self):
        for email in self.D_Email :          
            print(email)       
            
    def getdocphone(self):
        for phone in self.D_PNo:
            print(phone)
         
    def getdocaddress(self):
        for address in self.D_Add:
            print(address)        
            
    def getdocdepartment(self):
        for department in self.D_department:
            print(department)
            
    def getdocopd(self):
        for opdtime in self.D_opd_time:
            print(opdtime)
            
    def getdoctype(self):
        for types in self.D_types:
            print(types)
            
    def getdocspecialization(self):
        for specialization in self.D_specialization:
            print(specialization)        