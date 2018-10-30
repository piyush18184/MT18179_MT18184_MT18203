# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:19:23 2018

@author: Jeet
"""
import random
from pateint import patient as p
import pymysql
db = pymysql.connect( 
                    host='127.0.0.1',
                    user="root",
                    passwd="6%w<RPl4",
                    db="mydb"
                    )
print(db)
cursor = db.cursor()
print(cursor)

def main():

        print("######## Smart Hospital Sytem ########")
        while True:
            print("1. ADMIN LOGIN")
            print("2. DOCTOR LOGIN")
            print("3. NEW USER AS PATEINT")
            print("4. EXISTING USER")
            print("5. RESET PASSWORD")
            print("6. EMERGENCY")
            print("7. Exit")
            x = int(input())
            if x == 1:
               pswrd = input("Enter password: ")
               if pswrd == '1234':
                   while True:
                       print("Welcome to administrative mode")
                       print("1. View All Doctors")
                       print("2. View All Pateints")
                       print("3. Assign Doctors")
                       print("4. Add Doctors")
                       print("5. Exit")
                       ch = int(input("Enter your choice:"))
                       if ch == 1:
                           cursor.execute("select * from mydb.doctor_details")
                           for x in cursor:
                               print(x)
                           
                       elif ch == 2:
                           cursor.execute("select * from mydb.patient_details")
                           for x in cursor:
                              print(x)
                       elif ch == 3:
                           pass
                       elif ch == 4:
                           pass
                       elif ch == 5:
                           break
                       else:
                          print("Wrong choice")
               else:
                   print("error")
            elif x == 2:
               name = input("Enter Your user ID:.. ")
               pswrd = input("Enter Your password:.. ")
               
               if (name == 'sumit' and pswrd == '1234'):
                   print("sorry")
               else:   
                   while True:
                       ##############  Doctor functionality 
                        print("1. SEE PATEINT ALLOCATED")
                        print("2. EDIT PROFILE")
                        print("3. SORT PATEINT LIST")
                        print("4. LEAVE MANAGEMENT")
                        print("5. VIEW PROFILE")
                        print("6. REFERRAL")
                        print("7. EXIT")
                        x = int(input("Enter your choice:....."))
                        if x==1:
                            ###  view list of pateints allocated to him
                            pass
                            print()
                        elif x==2:
                            #### edit doctor profile
                            pass
                        elif x==3:
                            
                            ### sort of pateint depending upon department, id 
                            pass
                        elif x==4:
                            #### leave of doctors
                            pass
                        elif x==5:
                            ######  view profile
                            pass
                        elif x==6:
                            #### refereral if required 
                            pass
                        elif x==7:
                            pass
                        else:
                            return False
            elif x == 3:
               name = input("Enter Your name:.. ")
               email = input("Enter Your email:.. ")
               phoneno = int(input("Enter your phoneno:....."))
               age =  int(input("Enter the age:....."))
               adress = input("Enter your address no:" )
#               gender = input("enter the gender:.....")
#               pateint_type = input("OPD or Location:..............")
               password1 = input("enter the password:..... ")
               password2 = input("enter your password again:......")   ##### also rechecks the password 
               if password1 == password2:
              
                   ######### need to be changed according to table
                   cursor.execute("SELECT SUBSTRING(P_ID,3,5) FROM `mydb`.`patient_details` ORDER BY P_ID DESC LIMIT 1")
                   p1 = cursor.fetchone()
                   y= str(int(p1[0])+1)
                   x = 'P_'
                   P_ID = x + y
                   sql = "INSERT INTO `mydb`.`patient_details` (P_ID,P_Name,P_Age,P_PNo,P_Add,P_Email) VALUES('%s','%s',%s,%s,'%s','%s')"
                   val = (P_ID,name,age,phoneno,adress,email)
                   cursor.execute(sql%val)
                   db.commit()
                   print("your user id is ..... ",P_ID)
                   print("than you r regidteres please move forwrd with login.....") 
                   sql = "INSERT INTO `mydb`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
                   val = (P_ID,password1,email)
                   cursor.execute(sql%val)
                   db.commit()
                
            elif x == 4:
               u_id = input("Enter Your user id :.. ")
               password = input("Enter Your password :.. ")
               if(cursor.execute("SELECT ID FROM `mydb`.`admin` where ID='"+u_id+"' AND Password='"+password+"';")==None):
                   print("xyz")
               else:
                   while True:
                       print("## welcome to PATEINT mode")
                       print("1. SEARCH DOCTOR")        #### ON THE BASIS OF DEPARTMENT OR DOCTOR NAME ## INSIDE OOF DEPARTMENT 10 DOCTOR AYE 
                       print("2. SEE DOCTOR OPD TIMING")    
                       print("3. VIEW Doctor PROFILE")
                       print("4. VIEW HISTORY ")
                       print("5. VIEW PROFILE")
                       print("6. NEW APPOINTMENT")
                       print("7. edit profile")
                       print("8. EXIT")      
                       x = int(input("Enter your choice:"))
                       if x == 1:
                          ############
                          print("1. SEARCH BY DOCTOR NAME")
                          print("2. SEARCH BY ID")       #### WRITE LOGIC FOR EACH AND EVERY ONE
                          #### show available departments
                          print("3. SEARCH BY DEPARTMENT")
                          print("4. exit")
                          x = int(input("enter your choice:..."))
                          if x==1:
                              ch = input("enter doctor name")
                              print("list of doctors")
                              cursor.execute("SELECT * FROM `mydb`.'doctor_details` where D_Name = '"+ch+"';")
                              cursor.fetchall()
                              print("1. Want an appointment:")
                              print("2. go back")
                              x = int(input("ENter your choice:"))
                              if x == 1:
                                  ##### random exception handling sholud be used
                                  y = input("Enter doctor Id for appointment:")
                                  ######### apointment table should be used
                                  pass
                              else:
                                  
                          elif x==2:
                              ch = input("enetr department name")
                              print("list of doctors")
                              print("enter doctor id for appointment")
                          elif x==3:
                              ch = input("enter doctor id name")
                              print("list of doctors")
                              print("enter doctor id for appointment")
                          else:
                             return False
                       elif x == 2:
                           ##### search doctor id and show to pateint  
                           ### pateint can able to selct the coctor also
                           d_id = input("enter doctor id")
                       elif x==3:
                           #### show doctor profile to pateint
                           d_id = input("enter doctor id")
                           
                       elif x==4:
                           #### show pateint his history
                           pass
                       elif x==5:
                           #### pateints profile
                           pass
                       elif x==6:
                           ### assignment automatic 
                           pass
                       elif x==7:
                           ### edit pateints id
                           pass
                       else:
                           return False
                
            elif x == 5:
                    #### forgot password
                    pass
            
            elif x == 6:
                print("critical pateint")
                #### critical pateint 
                pass    
            elif x==7:
                sys.exit()
        else:
            print("Error")




if __name__ == "__main__":
   main()   






db.close()