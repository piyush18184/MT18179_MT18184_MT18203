# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:19:23 2018

@author: Jeet
"""
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
                           pass
                       elif ch == 2:
                           pass
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
               phoneno = input("Enter your phoneno:.....")
               age =  input("Enter the age:.....")
               adress = input("Enter your phone no:" )
               gender = input("enter the gender:.....")
               pateint_type = input("OPD or Location:..............")
               password1 = input("enter the password:..... ")
               password2 = input("enter your password agian:......")   ##### also rechecks the password 
               if password1 == password2:
               ####  ID generated automatically
                   print("your user id is ..... ")
                   print("than you yoU r regidteres please move forwrd with login.....") 
                
                
                
            elif x == 4:
               u_id = input("Enter Your user id :.. ")
               password = input("Enter Your password :.. ")
                ##### check for user if id and password matches and them move forward
               if u_id == "abc" and password == "1234":
                   print("## welcome to PATEINT mode")
                   print("1. SEARCH DOCTOR")        #### ON THE BASIS OF DEPARTMENT OR DOCTOR NAME ## INSIDE OOF DEPARTMENT 10 DOCTOR AYE 
                   print("2. SEE DOCTOR OPD TIMING")    
                   print("3. VIEW Doctor PROFILE")
                   print("4. VIEW HISTORY ")
                   print("5. VIEW PROFILE")
                   print("6. Automatic doctor assignment")
                   print("7. edit profile")
                   print("8. EXIT")      
                   
                   if x == 1:
                      ############
                      print("1. SEARCH BY NAME")
                      print("2. SEARCH BY ID")       #### WRITE LOGIC FOR EACH AND EVERY ONE
                      #### show available departments
                      print("3. SEARCH BY DEPARTMENT")
                      print("4. exit")
                      x = int(input())
                      if x==1:
                          ch = input("enetr doctor name")
                          pass
                      elif x==2:
                           ch = input("enetr department name")
                      elif x==3:
                            ch = input("enter doctor id name")
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