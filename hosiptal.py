# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:51:30 2018

@author: lenovo
"""

class Hospital:
   list_of_patients=[];
   list_of_doctors=[];
   list_of_departments=[];
    
    def __init__(self,doctors,departments,patients):
        self.doctors=doctors
        self.departments=departments
        self.pateints=patients
        
    def getdoctors(self):
        return self.doctors
    
    def getdepartments(self):
        return self.dpeartments
    
    def getpatients(self):
        return self.patients
    
    def setdoctors(self):
        pass
    
    def setdepartments(self):
        pass
    
    def setpatients(self):
        pass