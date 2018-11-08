# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 05:36:43 2018

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
class doctorprofessionaldetails:
    def __init__(self):
        pass
        
    def getdocprofessinalall(self,did):
        cursor.execute("SELECT * FROM `mydb`.`doctor_professional_details` WHERE D_ID='" +did+ "';")
        print(cursor.fetchall())
    

    def setdoctordepartment(self,dep,did):
        cursor.execute("UPDATE `mydb`.`doctor_professional_details` SET D_Department = '" +dep+ "' WHERE D_ID = '" +did+ "';")
        db.commit()  
        
    def setopdstarttime(self,opdst,did):
         cursor.execute("UPDATE `mydb`.`doctor_professional_details` SET D_OPD_TIME_START = '" +opdst+ "' WHERE D_ID = '" +did+ "';")
         db.commit()
    def setopdendttime(self,opdet,did):
         cursor.execute("UPDATE `mydb`.`doctor_professional_details` SET D_OPD_TIME_END = '" +opdet+ "' WHERE D_ID = '" +did+ "';")
         db.commit()
    def setdoctype(self,dtyp,did):
         cursor.execute("UPDATE `mydb`.`doctor_professional_details` SET D_Type = '" +dtyp+ "' WHERE D_ID = '" +did+ "';")
         db.commit()
    
    def setdocspecialisation(self,spec,did):
         cursor.execute("UPDATE `mydb`.`doctor_professional_details` SET D_Specialization = '" +spec+ "' WHERE D_ID = '" +did+ "';")
         db.commit()
    def setextensionno(self,ext,did):
        cursor.execute("UPDATE `mydb`.`doctor_professional_details` SET D_ExtensionNo = '" +ext+ "' WHERE D_ID = '" +did+ "';")
        db.commit()
    def setroomno(self,rmno,did):
        cursor.execute("UPDATE `mydb`.`doctor_professional_details` SET D_RoomNo = '" +rmno+ "' WHERE D_ID = '" +did+ "';")
        db.commit()
    def getdocopd(self):
        for opdtime in self.D_opd_time:
            print(opdtime)
            
    def getdoctype(self):
        for types in self.D_types:
            print(types)
            
    def getdocspecialization(self):
        for specialization in self.D_specialization:
            print(specialization)
    
    def getdocroom_no(self):
        for room in self.D_room_no:
            print(room)
            
    def getdocextension_no(self):
        for extension in self.D_extension_no:
            print(extension)