# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 05:37:40 2018

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

class doctorpersonaldetails:
    def __init__(self):
         pass
        
    
    def setdoctorname(self,name,did):
        cursor.execute("UPDATE `mydb`.`doctor_details` SET D_Name = '" +name+ "' WHERE D_ID = '" +did+ "';")
        db.commit()
    
    def setdoctorage(self,ageee,did):
        cursor.execute("UPDATE `mydb`.`doctor_details` SET D_Age = '" +ageee+ "' WHERE D_ID = '" +did+ "';")
        db.commit()
    def setdoctorpno(self,pno,did):
        cursor.execute("UPDATE `mydb`.`patient_details` SET D_PNo = '" +pno+ "' WHERE D_ID = '" +did+ "';")
        db.commit()
    
    def setdoctoremail(self,emaii,did):
        cursor.execute("UPDATE `mydb`.`doctor_details` SET D_Email = '" +emaii+ "' WHERE D_ID = '" +did+ "';")
        db.commit()
    def setdoctoraddr(self,addr,did):
        cursor.execute("UPDATE `mydb`.`doctor_details` SET D_PNo = '" +addr+ "' WHERE D_ID = '" +did+ "';")
        db.commit()
    
    
    def getdocdetail(self,did):
         cursor.execute("SELECT * FROM `mydb`.`doctor_details` WHERE D_ID='" +did+ "';")
         print(cursor.fetchall())
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