# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 05:42:32 2018

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
class department:
    def __init__(self):
        pass
    
    def setdephod(self,dep_id,hod):
        cursor.execute("UPDATE `mydb`.`department` SET Dep_HOD = '" +hod+ "' WHERE Dep_ID = '" +dep_id+ "';")
        db.commit()
    
    def setdep_building(self,dep_id,building):
        cursor.execute("UPDATE `mydb`.`department` SET Dep_Building = '" +building+ "' WHERE Dep_ID = '" +dep_id+ "';")
        db.commit()
    
    def setdepcontact(self,dep_id,contact):
        cursor.execute("UPDATE `mydb`.`department` SET Dep_Contact = '" + contact + "' WHERE Dep_ID = '" +dep_id+ "';")
        db.commit()
    
    def setdeprooms(self,dep_id,room):
        cursor.execute("UPDATE `mydb`.`department` SET Dep_Room = '" +room+ "' WHERE Dep_ID = '" +dep_id+ "';")
        db.commit()
    
    def setdepopd(self,dep_id,opd):
        cursor.execute("UPDATE `mydb`.`department` SET Dep_OPD = '" +opd+ "' WHERE Dep_ID = '" +dep_id+ "';")
        db.commit()
    
    def setdepname(self,dep_id,name):
        cursor.execute("UPDATE `mydb`.`department` SET Dep_Name = '" +name+ "' WHERE Dep_ID = '" +dep_id+ "';")
        db.commit()
    
    def getalldep(self,dep_id):
        cursor.execute("SELECT Dep_Name FROM mydb.department")
        print(cursor.fetchall())
    
    def getdepinfo(self,dep_id):
        cursor.execute("SELECT * FROM `mydb.department` WHERE Dep_ID='" +dep_id+ "';")
        print(cursor.fetchall()) 
    
    def getdepbuilding(self,dep_id):
        cursor.execute("SELECT Dep_Building Dep_Room FROM `mydb.department` WHERE Dep_ID='" +dep_id+ "';")
        print(cursor.fetchall())
    def getdepcontact(self,dep_id):
        cursor.execute("SELECT Dep_Contact FROM `mydb.department` WHERE Dep_ID='" +dep_id+ "';")
        print(cursor.fetchall())
    
    def getdeprooms(self,dep_id):
        cursor.execute("SELECT Dep_Room Dep_Building FROM `mydb.department` WHERE Dep_ID='" +dep_id+ "';")
        print(cursor.fetchall())
    
    def getdephod(self,dep_id):
        cursor.execute("SELECT Dep_HOD FROM `mydb.department` WHERE Dep_ID='" +dep_id+ "';")
        print(cursor.fetchall())
    
    def getdepid(self,dep_id):
        cursor.execute("SELECT Dep_ID FROM `mydb.department` WHERE Dep_ID='" +dep_id+ "';")
        print(cursor.fetchall())
