# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 05:45:34 2018

@author: Jeet
"""

import pymysql
db = pymysql.connect( 
                    host='127.0.0.1',
                    user="root",
                    passwd="6%w<RPl4",
                    db="mydb"
                    )
#print(db)
cursor = db.cursor()


class patientmedicalreport:
    def __init__(self):
        pass
    
    def setpateientpres(self):
        print(" Enter the Pateint ID whose prescriton needs to be edited::")
        x1 = input()
        y1 = input("Enter prescription::")
        cursor.execute("UPDATE `mydb`.`patient_medical_history` SET Prescription = '" +y1+ "' WHERE P_ID = '" +x1+ "';")
        db.commit()
    def setpatienthistory(self):
        print(" Enter the Pateint ID whose Reports needs to be edited::")
        x1 = input()
        y1 = input("Enter Reports for updation::")
        cursor.execute("UPDATE `mydb`.`patient_medical_history` SET Prescription = '" +y1+ "' WHERE P_ID = '" +x1+ "';")
        db.commit()
        
#    def setpatientid(self):
#        self.patient_id=patient_id
#        
#    def setpatientreferral_id(self):
#        self.patient_referral=patient_referral
#        
#    def getpatientreferral_id(self):
#        return self.patient_referral
#    
#    def getpatientid(self):
#        return self.patient_id
#    
#    def getpatienthistory(self):
#        return self.patient_history
#    
#    def getpatientpres(self):
#        self.patient_prescription
