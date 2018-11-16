# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 05:40:14 2018

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
class HOD:
    def __init__(self):
        print("______HOD WINDOW_______")
        print("1. Change department name ")
        print("2. Change department contact ")
        print("3. Change department room ")
        print("4. Change department OPD ")
        print("5. Change department Building ")
    
    def setopdtiming(self):
        pass
    
    def gethodroom(self):
        pass
    
    def gethodcontact(self):
        pass
    
    
    def gethodqualification(self):
        pass
    
    def sethoddep(self):
        pass
    
    def sethodroom(self):
        pass

    def sethodcontact(self):
        pass
    
    def sethodqualification(self):
        pass
        
