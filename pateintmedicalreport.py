# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 05:45:34 2018

@author: Jeet
"""
class patientmedicalreport:
    def __init__(self):
        pass
    
    def setpateientpres(self):
        self.patient_prescription=patient_prescription
        
    def setpatienthistory(self):
        self.patient_history=patient_history
        
    def setpatientid(self):
        self.patient_id=patient_id
        
    def setpatientreferral_id(self):
        self.patient_referral=patient_referral
        
    def getpatientreferral_id(self):
        return self.patient_referral
    
    def getpatientid(self):
        return self.patient_id
    
    def getpatienthistory(self):
        return self.patient_history
    
    def getpatientpres(self):
        self.patient_prescription
