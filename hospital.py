# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 05:30:17 2018

@author: Jeet
"""
import pymysql
import datetime
db = pymysql.connect( 
                    host='127.0.0.1',
                    user="root",
                    passwd="6%w<RPl4",
                    db="mydb"
                    )
cursor = db.cursor()

class Hospital:
   list_of_patients=[];
   list_of_doctors=[];
   list_of_departments=[];
    
   def __init__(self):
        pass
   
##################################################################################################    
   def getdoctorsname(self,name):
       cursor.execute("SELECT * FROM `mydb`.`doctor_details` where D_Name = '" + name + "';")
       print(cursor.fetchall())
########################################################################################
   def getdoctorsid(self,id):
       cursor.execute("SELECT * FROM `mydb`.`doctor_details` where D_DID = '" + id + "';")
       print(cursor.fetchall())
###############################################################################################  
   def getdoctorsdept(self,dep):
       cursor.execute("SELECT * FROM `mydb`.`doctor_details` where D_Department = '" + dep + "';")
       print(cursor.fetchall())
###############################################################################################
   def getappointmentdept(self,dep,u_id):
       now = datetime.datetime.now()
       cursor.execute("SELECT Dep_sym FROM `mydb`.`department` where D_Name = '" + dep + "';")
       x = cursor.fetchone()
       cursor.execute(
                "SELECT SUBSTRING(P_Appointment_ID,5,7) FROM `mydb`.`appointments` ORDER BY D_ID DESC LIMIT 1")
       p1 = cursor.fetchone()
       y = str(int(p1[0]) + 1)
       a = x + y   ####genearted pateint id
       #############################################################################
       ###### NEED TO ENSURE THAT DOCTOR ID ALLOCATED BY SYSTEM SHOULD BE OF SAME DEPARTMENT
       sql = "INSERT INTO `mydb`.`appointments` (`P_Appointment_ID`, `Appointed_D_ID`, `P_Appointment_Date`, `P_Appointment_Time`, `P_ID`)VALUES('%s','%s','%s','%s','%s','%s')" 
       val =  (a, 'D_112', now.date(), now.time(), u_id)
       cursor.execute(sql % val)
       db.commit()
###############################################################################################       
   def getappointmentid(self,dep,u_id):
       now = datetime.datetime.now()
       cursor.execute("SELECT D_Department FROM `mydb`.`doctor_professional_details` where D_DID = '" + dep + "';")
       x = cursor.fetchone()
       cursor.execute("SELECT Dep_sym FROM `mydb`.`department` where D_Name = '" + x + "';")
       b = cursor.fetchone()
       cursor.execute(
                "SELECT SUBSTRING(P_Appointment_ID,5,7) FROM `mydb`.`appointments` ORDER BY D_ID DESC LIMIT 1")
       p1 = cursor.fetchone()
       y = str(int(p1[0]) + 1)
       a = b + y   ####genearted pateint id
       #############################################################################
       ###### NEED TO ENSURE THAT DOCTOR ID ALLOCATED BY SYSTEM SHOULD BE OF SAME DEPARTMENT
       sql = "INSERT INTO `mydb`.`appointments` (`P_Appointment_ID`, `Appointed_D_ID`, `P_Appointment_Date`, `P_Appointment_Time`, `P_ID`)VALUES('%s','%s','%s','%s','%s','%s')" 
       val =  (a, dep, now.date(), now.time(), u_id)
       cursor.execute(sql % val)
       db.commit() 
###############################################################################################     
   def checkavailability(self,id):
       
       ### write sql query for searching the no of p[ateimts assigned to a doctor id]
       ### for no of pateintsas well as for for timings
       pass
   
###############################################################################################    
   def gettiming(self,did):
        cursor.execute("SELECT D_OPD_TIME_START, D_OPD_TIME_END FROM `mydb`.`doctor_professional_details` where D_DID = '" + did + "';")
        print(cursor.fetchall()) 
###############################################################################################
   def getdepartments(self):
       cursor.execute("SELECT `department`.`Dep_Name` FROM `mydb`.`department`")
       print(cursor.fetchall())  
###############################################################################################
   def getdoctordetail(self,did):
       cursor.execute("SELECT * FROM `mydb`.`doctor_details` where D_ID = '" + did + "';")
       print(cursor.fetchall())
###############################################################################################    
   def getpateinthistory(self,pid):
       cursor.execute("SELECT * FROM `mydb`.`patient_medical_history` where Pat_ID = '"+pid+"';")
       print(cursor.fetchall())
###############################################################################################    
    
   def getpatientsallocated(self,did):
       cursor.execute("SELECT * FROM `mydb`.`appointment` where Appointed_D_ID = '"+did+"';")
       print(cursor.fetchall())
    
   def setdoctors(self):
        pass
    
   def setdepartments(self):
        pass
    
   def setpatients(self):
        pass