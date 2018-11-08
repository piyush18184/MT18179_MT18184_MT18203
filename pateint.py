# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 19:26:49 2018

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

class patient:
    def __init__(self):
        pass
#   
        
    def setpateintname(self,nm,pid):
        cursor.execute("UPDATE `mydb`.`patient_details` SET P_Name = '" +nm+ "' WHERE P_ID = '" +pid+ "';")
        db.commit()
        
    def setpatientemail(self,emai,pid):
        cursor.execute("UPDATE `mydb`.`patient_details` SET P_Email = '" +emai+ "' WHERE P_ID = '" +pid+ "';")
        db.commit()     
    def setpatientphone(self,phno,pid):
        cursor.execute("UPDATE `mydb`.`patient_details` SET P_PNo = '" +phno+ "' WHERE P_ID = '" +pid+ "';")
        db.commit()
    def setpateintage(self,age,pid):
        cursor.execute("UPDATE `mydb`.`patient_details` SET P_Age = '" +age+ "' WHERE P_ID = '" +pid+ "';")
        db.commit()
    def setpatientaddress(self,pid,addr):
        cursor.execute("UPDATE `mydb`.`patient_details` SET P_Email = '" +addr+ "' WHERE P_ID = '" +pid+ "';")
        db.commit()  
    
    def getidpno(self,pno):
        cursor.execute("SELECT P_ID FROM `mydb`.`patient_details` WHERE P_PNo='" +pno+ "';")
        x = cursor.fetchone()
        return x[0]
    
    
    def setpassword(self,age,pid):
        cursor.execute("UPDATE `mydb`.`admin` SET Password = '" +age+ "' WHERE ID = '" +pid+ "';")
        db.commit()
    
    def getpatientname(self,val):
#        sql = 
        #cursor.execute("select * from mydb.patient_details where P_ID="+P_ID+";")
#        cursor.execute("select * from mydb.patient_details where P_ID='"+val+"';")
#        m1=cursor.fetchone()
#        print(m1)
         pass
        #print(self.name)
    def getpatientall(self,pid):
        cursor.execute("SELECT * FROM `mydb`.`patient_details` WHERE P_ID='" +pid+ "';")
        print(cursor.fetchall())
            
    def getpatientemail(self,pid):
        cursor.execute("SELECT * FROM `mydb`.`patient_details` WHERE P_ID='" +pid+ "';")
        print(cursor.fetchall())       
        
    def getpatientpswrd(self,pid):
        cursor.execute("SELECT Password FROM `mydb`.`admin` WHERE ID='" +pid+ "';")
        x = cursor.fetchone()
        return x[0]
    def getpatientphone(self):
        print(self.phone)
            
    def getpatientaddress(self):
        print(self.address)        
    
    def getpatientid(self):
        print(self.P_ID)
            
    def getpatientage(self):
        print(self.P_Age) 
            
    def getpatientgender(self):
        print(self.P_Gender)
        
#        
#p = patient()  
#val = 'P_109'      
#p.getpatientall(val)
#y = p.getpatientpswrd(val)
#print(y[0])
#db.close()