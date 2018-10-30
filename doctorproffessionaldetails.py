# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 18:06:57 2018

@author: lenovo
"""

class doctorprofessionaldetails:
    def __init__(self,D_department,D_opd_time,D_types,D_specialization):
        self.D_department=D_department
        self.D_opd_time=D_opd_time
        self.D_types=D_types
        self.D_specialization=D_specialization
        
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