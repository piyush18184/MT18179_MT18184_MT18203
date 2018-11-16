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
       cursor.execute("SELECT * FROM `mydb`.`doctor_professional_details` where D_Department = '" + dep + "';")
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
       cursor.execute("SELECT * FROM `mydb`.`appointments` where Appointed_D_ID = '"+did+"';")
       print(cursor.fetchall())
#######################################################################################################    
   def referpatients(self,name,a):
       cursor.execute("SELECT PAT_ID FROM `mydb`.`doctor_assignment` WHERE DOC_ID='"+name+"';")
       print(cursor.fetchall())
       y1=input("ENTER THE PATIENT'S ID TO BE REFFERED:")
       cursor.execute("SELECT COUNT(PAT_ID) FROM `mydb`.`doctor_assignment` WHERE PAT_ID='" + y1 + "' AND DOC_ID='" + name + "';")
       y2=cursor.fetchone()
       a.getpatientall(y1)
       p2=y2[0]
       if(p2>0):
        print(" __________________________________________________________________________ ")
        print("|------------------------IS THE INFORMATION CORRECT------------------------|")
        print("|                                                                          |")
        print("|                                1. YES                                    |")
        print("|                                2. NO                                     |")
        print("|__________________________________________________________________________|")
        xxx = int(input("PLEASE SELECT THE OPTION:..."))
        if xxx == 1:
            d2=input("ENTER THE DOCTOR's ID TO BE REFERRED TO:")
            cursor.execute("DELETE FROM `mydb`.`doctor_assignment` WHERE PAT_ID='"+y1+"';")
            db.commit()
            sql = "INSERT INTO `mydb`.`doctor_assignment` (`DOC_ID`, `PAT_ID`, `DOC_MAX_LMT`, `REF_DOC_ID`) VALUES('%s','%s',%s,'%s')"
            val = (d2, y1, 20,name)
            cursor.execute(sql % val)
            db.commit()
            print("Pateints successfully reffered.")
#######################################################################################################    
   def emergency(self):
        name = input("| NAME:.. ")
        types = input("| TYPE:.. ")
        age = input("| AGE:..")
        em = input("| EMAIL ID:..")
        cursor.execute("SELECT SUBSTRING(P_ID,3,5) FROM `mydb`.`patient_details` ORDER BY P_ID DESC LIMIT 1")
        p1 = cursor.fetchone()
        y = str(int(p1[0]) + 1)
        x = 'P_'
        E_ID = x + y
        sql = "INSERT INTO `mydb`.`patient_details` (P_ID,P_Name,P_AGE,P_EMAIL) VALUES('%s','%s',%s,'%s')"
        val = (E_ID, name, age, em)
        cursor.execute(sql % val)
        db.commit()
        psw = 'xyz'
        sql = "INSERT INTO `mydb`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
        val = (E_ID, psw, em)
        cursor.execute(sql % val)
        db.commit()
        print("| PATIENT ID:...", E_ID)
        print("| PATIENT PASSWORD:...", psw)
        print("| PLEASE KEEP A NOTE FOR FURTHER REFERENCE")
        sql = "INSERT INTO `mydb`.`patient_assignment` (E_NAME,E_ID,E_TYPE,E_AGE) VALUES('%s','%s','%s',%s)"
        val = (name, E_ID, types, age)
        cursor.execute(sql % val)
        db.commit()
        print("| PATIENT'S DETAILS SAVED SUCCESSFULLY")
        cursor.execute("SELECT * FROM `mydb`.`patient_assignment` WHERE E_ID='" + E_ID + "';")
        print(cursor.fetchall())
    
########################################################################################################    
   def setdoctors(self):
        pass
    
   def setdepartments(self):
        pass
    
   def setpatients(self):
       pass
   
