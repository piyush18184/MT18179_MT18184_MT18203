# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:10:06 2018

@author: lenovo
"""

class department:
    def __init__(self,hod,senior_specialist,specialist,senior_resident,junior_resident):
        self.hod=hod
        self.senior_specialist=senior_specialist
        self.specialist=specialist
        self.senior_resident=senior_resident
        self.junior_resident=junior_resident
        
    def gethod(self):
        for hod in self.hod:
            print(hod)
            
    def getsenior_specialist(self):
        for ssp in self.senior_specialist:
            print(ssp)
            
    def getspecialist(self):
        for sp in self.specialist:
            print(sp)
            
    def getsenior_resident(self):
        for sr in self.senior_resident:
            print(sr)
            
    def getjunior_resident(self):
        for jr in self.junior_resident:
            print(jr)
            
        
        
        