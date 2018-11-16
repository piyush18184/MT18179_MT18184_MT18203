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
    def editpatient(self):
                    print(" __________________________________________________________________________ ")
                    print("|----------------PATIENT'S PERSONAL DETAILS EDIT WINDOW--------------------|")
                    print("|                                                                          |")
                    print("|                        1. EDIT PATIENT'S NAME                            |")
                    print("|                        2. EDIT PATIENT'S AGE                             |")
                    print("|                        3. EDIT PATIENT'S PHONE NUMBER                    |")
                    print("|                        4. EDIT PATIENT'S EMAIL                           |")
                    print("|                        5. EDIT PATIENT'S ADDRESS                         |")
                    print("|                        6. RETURN TO PREVIOUS PAGE                        |")
                    print("|__________________________________________________________________________|")
                    xx = int(input("Enter your choice:....."))
                    if xx == 1:
                        pid = input("| PATIENT ID:.. ")
                        self.getpatientall(pid)  ###### getting all details of
                        print(
                            " __________________________________________________________________________ ")
                        print(
                            "|------------------------IS THE INFORMATION CORRECT------------------------|")
                        print(
                            "|                                                                          |")
                        print(
                            "|                        1. YES                                            |")
                        print(
                            "|                        2. NO                                             |")
                        print(
                            "|__________________________________________________________________________|")
                        xxx = int(input("PLEASE SELECT THE OPTION:..."))
                        if xxx == 1:
                            nm = input("| PATIENT NAME:.. ")
                            print(
                                " __________________________________________________________________________ ")
                            print(
                                "|------------------------------CONFIRM-------------------------------------|")
                            print(
                                "|                                                                          |")
                            print(
                                "|                        1. YES                                            |")
                            print(
                                "|                        2. NO                                             |")
                            print(
                                "|__________________________________________________________________________|")
                            xxx = int(input("PLEASE CONFIRM..?"))
                            if xxx == 1:
                                self.setpateintname(nm, pid)
                                print(" ___________________________________ ")
                                print("| PATIENT NAME UPDATED SUCCESSFULLY:...|")
                                self.getpatientall(pid)
                            elif xxx == 2:
                                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                for i in range(1, 30000000):
                                    pass
                                ##continue
                            else:
                                print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                ##continue
                        elif xx == 2:
                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                            for i in range(1, 30000000):
                                pass
                            ##continue
                    elif xx == 2:
                        pid = input("| PATIENT ID:.. ")
                        self.getpatientall(pid)
                        print(
                            " __________________________________________________________________________ ")
                        print(
                            "|------------------------IS THE INFORMATION CORRECT------------------------|")
                        print(
                            "|                                                                          |")
                        print(
                            "|                        1. YES                                            |")
                        print(
                            "|                        2. NO                                             |")
                        print(
                            "|__________________________________________________________________________|")
                        xxx = int(input("PLEASE SELECT THE OPTION:..."))
                        if xxx == 1:
                            agee = input("| PATIENT AGE:.. ")
                            print(
                                " __________________________________________________________________________ ")
                            print(
                                "|------------------------------CONFIRM-------------------------------------|")
                            print(
                                "|                                                                          |")
                            print(
                                "|                        1. YES                                            |")
                            print(
                                "|                        2. NO                                             |")
                            print(
                                "|__________________________________________________________________________|")
                            xxx = int(input("PLEASE CONFIRM..?"))
                            if xxx == 1:
                                self.setpateintage(agee, pid)
                                print(" ___________________________________ ")
                                print("| PATIENT AGE UPDATED SUCCESSFULLY:...|")
                                self.getpatientall(pid)
                            elif xxx == 2:
                                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                for i in range(1, 30000000):
                                    pass
                                ##continue
                            else:
                                print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                ##continue
                        elif xx == 2:
                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                            for i in range(1, 30000000):
                                pass
                            ##continue
                    elif xx == 3:
                        pid = input("| PATIENT ID:.. ")
                        self.getpatientall(pid)
                        print(
                            " __________________________________________________________________________ ")
                        print(
                            "|------------------------IS THE INFORMATION CORRECT------------------------|")
                        print(
                            "|                                                                          |")
                        print(
                            "|                        1. YES                                            |")
                        print(
                            "|                        2. NO                                             |")
                        print(
                            "|__________________________________________________________________________|")
                        xxx = int(input("PLEASE SELECT THE OPTION:..."))
                        if xxx == 1:
                            phno = input("| PATIENT PHONE NUMBER:.. ")
                            print(
                                " __________________________________________________________________________ ")
                            print(
                                "|------------------------------CONFIRM-------------------------------------|")
                            print(
                                "|                                                                          |")
                            print(
                                "|                        1. YES                                            |")
                            print(
                                "|                        2. NO                                             |")
                            print(
                                "|__________________________________________________________________________|")
                            xxx = int(input("PLEASE CONFIRM..?"))
                            if xxx == 1:
                                self.setpatientphone(pid, phno)
                                print(" ___________________________________ ")
                                print("| PATIENT PHONE NUMBER UPDATED SUCCESSFULLY:...|")
                                self.getpatientall(pid)
                            elif xxx == 2:
                                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                for i in range(1, 30000000):
                                    pass
                                ##continue
                            else:
                                print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                ##continue
                        elif xx == 2:
                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                            for i in range(1, 30000000):
                                pass
                            ##continue
                    elif xx == 4:
                        pid = input("| PATIENT ID:.. ")
                        self.getpatientall(pid)
                        print(
                            " __________________________________________________________________________ ")
                        print(
                            "|------------------------IS THE INFORMATION CORRECT------------------------|")
                        print(
                            "|                                                                          |")
                        print(
                            "|                        1. YES                                            |")
                        print(
                            "|                        2. NO                                             |")
                        print(
                            "|__________________________________________________________________________|")
                        xxx = int(input("PLEASE SELECT THE OPTION:..."))
                        if xxx == 1:
                            emai = input("| PATIENT EMAIL:.. ")
                            print(
                                " __________________________________________________________________________ ")
                            print(
                                "|------------------------------CONFIRM-------------------------------------|")
                            print(
                                "|                                                                          |")
                            print(
                                "|                        1. YES                                            |")
                            print(
                                "|                        2. NO                                             |")
                            print(
                                "|__________________________________________________________________________|")
                            xxx = int(input("PLEASE CONFIRM..?"))
                            if xxx == 1:
                                self.setpatientemail(pid, emai)
                                print(" ___________________________________ ")
                                print("| PATIENT EMAIL UPDATED SUCCESSFULLY:...|")
                                self.getpatientall(pid)
                            elif xxx == 2:
                                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                for i in range(1, 30000000):
                                    pass
                                #continue
                            else:
                                print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                #continue
                        elif xx == 2:
                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                            for i in range(1, 30000000):
                                pass
                            #continue
                    elif xx == 5:
                        pid = input("| PATIENT ID:.. ")
                        self.getpatientall(pid)
                        print(
                            " __________________________________________________________________________ ")
                        print(
                            "|------------------------IS THE INFORMATION CORRECT------------------------|")
                        print(
                            "|                                                                          |")
                        print(
                            "|                        1. YES                                            |")
                        print(
                            "|                        2. NO                                             |")
                        print(
                            "|__________________________________________________________________________|")
                        xxx = int(input("PLEASE SELECT THE OPTION:..."))
                        if xxx == 1:
                            addr = input("| PATIENT ADDRESS:.. ")
                            print(
                                " __________________________________________________________________________ ")
                            print(
                                "|------------------------------CONFIRM-------------------------------------|")
                            print(
                                "|                                                                          |")
                            print(
                                "|                        1. YES                                            |")
                            print(
                                "|                        2. NO                                             |")
                            print(
                                "|__________________________________________________________________________|")
                            xxx = int(input("PLEASE CONFIRM..?"))
                            if xxx == 1:
                                self.setpatientaddress(pid, addr)
                                print(" ___________________________________ ")
                                print("| PATIENT ADDRESS UPDATED SUCCESSFULLY:...|")
                                self.getpatientall(pid)
                            elif xxx == 2:
                                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                for i in range(1, 30000000):
                                    pass
                                #continue
                            else:
                                print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                #continue
                        elif xx == 2:
                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                            for i in range(1, 30000000):
                                pass
                            #continue
                    elif xx == 6:
                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                        for i in range(1, 30000000):
                            pass
                        #continue
                    else:
                        print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                        #continue
#################################################################################################################################################################    
                        
    def editpatientself(self):
                print(" __________________________________________________________________________ ")
                print("|----------------------------EDIT PROFILE----------------------------------|")
                print("|                                                                          |")
                print("|                            1. EDIT NAME :                                |")
                print("|                            2. EDIT EMAIL ID:                             |")
                print("|                            3. EDIT ADDRESS:                              |")
                print("|                            2. EDIT PHONE NO:                             |")
                print("|                            3. EDIT AGE:                                  |")
                print("|__________________________________________________________________________|")
                ### edit patients id
                x = int(input("| ENTER YOUR CHOICE:..."))
                y = input("| ENTER YOUR ID AGAIN:...")
#                self = p()
                self.getpatientall(y)
                if x == 1:
                    ######### name ########
                    print("| 1. Confirm")
                    print("| 2. RETURN TO PREVIOUS WINDOW:... ")
                    choice = int(input("| ENTER YOUR CHOICE:..."))
                    if choice == 1:
                        paswrd = input("enter your password please")

                        if paswrd == self.getpatientpswrd(y):
                            name = input("enter name to be changed")
                            self.setpateintname(name, y)
                            print("pleas wait .............")
                            i = 1000000
                            while i >= 0:
                                i = i - 1
                            print("your name has been changed")
                            self.getpatientall(y)
                        else:
                            print("Sorry you entered wrong password")
                            return False
                    elif choice == 2:
                        pass
                    else:
                        print("wrong choice")
                        pass
                elif x == 2:
                    ######### Email #####
                    print("| 1. Confirm")
                    print("| 2. RETURN TO PREVIOUS WINDOW:... ")
                    choice = int(input("| ENTER YOUR CHOICE:..."))
                    if choice == 1:
                        paswrd = input("enter your password please")

                        if paswrd == self.getpatientpswrd(y):
                            email = input("enter email to be changed")
                            self.setpatientemail(email, y)
                            print("pleas wait .............")
                            i = 1000000
                            while i >= 0:
                                i = i - 1
                            print("your email has been changed")
                            self.getpatientall(y)
                        else:
                            print("Sorry you entered wrong password")
                            return False
                    elif choice == 2:
                        pass
                    else:
                        print("wrong choice")
                        pass
                elif x == 3:
                    ################ Adressss ##########
                    print("| 1. Confirm")
                    print("| 2. RETURN TO PREVIOUS WINDOW:... ")
                    choice = int(input("| ENTER YOUR CHOICE:..."))
                    if choice == 1:
                        paswrd = input("enter your password please")

                        if paswrd == self.getpatientpswrd(y):
                            addr = input("enter address to be changed")
                            self.setpatientaddress(addr, y)
                            print("pleas wait .............")
                            i = 1000000
                            while i >= 0:
                                i = i - 1
                            print("your email has been changed")
                            self.getpatientall(y)
                        else:
                            print("Sorry you entered wrong password")
                            return False
                    elif choice == 2:
                        return False
                    else:
                        print("wrong choice")
                        return False
                elif x == 4:
                    ######### phone number
                    print("| 1. Confirm")
                    print("| 2. RETURN TO PREVIOUS WINDOW:... ")
                    choice = int(input("| ENTER YOUR CHOICE:..."))
                    if choice == 1:
                        paswrd = input("enter your password please")

                        if paswrd == self.getpatientpswrd(y):
                            phno = input("enter address to be changed")
                            self.setpatientphone(phno, y)
                            print("pleas wait .............")
                            i = 1000000
                            while i >= 0:
                                i = i - 1
                            print("your email has been changed")
                            self.getpatientall(y)
                        else:
                            print("Sorry you entered wrong password")
                            return False
                    elif choice == 2:
                        return False
                    else:
                        print("wrong choice")
                        return False
                elif x == 5:
                    print("| 1. Confirm")
                    print("| 2. RETURN TO PREVIOUS WINDOW:... ")
                    choice = int(input("| ENTER YOUR CHOICE:..."))
                    if choice == 1:
                        paswrd = input("enter your password please")

                        if paswrd == self.getpatientpswrd(y):
                            age = input("enter age to be changed")
                            self.setpatientaddress(age, y)
                            print("pleas wait .............")
                            i = 1000000
                            while i >= 0:
                                i = i - 1
                            print("your age has been updated")
                            self.getpatientall(y)
                        else:
                            print("Sorry you entered wrong password")
                            return False
                    elif choice == 2:
                        return False
                    else:
                        print("wrong choice")
                        return False
                else:
                    print("WRONG SELECTION...REDIRECTING TO PREVIOUS PAGE..!!")
#                    input("PRESS ANY KEY TO CONTINUE:..")
                    
                      
#################################################################################################################################################################    
    def setpateintname(self,nm,pid):
        cursor.execute("UPDATE `mydb`.`patient_details` SET P_Name = '" +nm+ "' WHERE P_ID = '" +pid+ "';")
        db.commit()
#################################################################################################################################################################        
    def setpatientemail(self,emai,pid):
        cursor.execute("UPDATE `mydb`.`patient_details` SET P_Email = '" +emai+ "' WHERE P_ID = '" +pid+ "';")
        db.commit()     
#################################################################################################################################################################
    def setpatientphone(self,phno,pid):
        cursor.execute("UPDATE `mydb`.`patient_details` SET P_PNo = '" +phno+ "' WHERE P_ID = '" +pid+ "';")
        db.commit()
#################################################################################################################################################################
    def setpateintage(self,age,pid):
        cursor.execute("UPDATE `mydb`.`patient_details` SET P_Age = '" +age+ "' WHERE P_ID = '" +pid+ "';")
        db.commit()
#################################################################################################################################################################
    def setpatientaddress(self,pid,addr):
        cursor.execute("UPDATE `mydb`.`patient_details` SET P_Add = '" +addr+ "' WHERE P_ID = '" +pid+ "';")
        db.commit()  
#################################################################################################################################################################    
    def getidpno(self,pno):
        cursor.execute("SELECT P_ID FROM `mydb`.`patient_details` WHERE P_PNo='" +pno+ "';")
        x = cursor.fetchone()
        return x[0]
#################################################################################################################################################################    
    
    def setpassword(self,age,pid):
        cursor.execute("UPDATE `mydb`.`admin` SET Password = '" +age+ "' WHERE ID = '" +pid+ "';")
        db.commit()
#################################################################################################################################################################    
    def registerpatient(self):
        name = input("| NAME:.. ")
        email = input("| EMAIL ID:.. ")
        phoneno = int(input("| PHONE NUMBER:....."))
        age = int(input("| AGE:....."))
        adress = input("| ADDRESS:")
        #               gender = input("enter the gender:.....")
        #               pateint_type = input("OPD or Location:..............")
        password1 = input("| PASSWORD:..... ")
        password2 = input("| RE-TYPE PASSWORD:......")  ##### also rechecks the password
        if password1 == password2:
            ######### need to be changed according to table
            cursor.execute("SELECT SUBSTRING(P_ID,3,5) FROM `mydb`.`patient_details` ORDER BY P_ID DESC LIMIT 1")
            p1 = cursor.fetchone()
            y = str(int(p1[0]) + 1)
            x = 'P_'
            P_ID = x + y
            sql = "INSERT INTO `mydb`.`patient_details` (P_ID,P_Name,P_Age,P_PNo,P_Add,P_Email) VALUES('%s','%s',%s,%s,'%s','%s')"
            val = (P_ID, name, age, phoneno, adress, email)
            cursor.execute(sql % val)
            db.commit()
            print(" ___________________________________ ")
            print("| PATIENT REGISTRATION COMPLETED:...|")
            print("| USER ID:... ", P_ID)
            print("| PLEASE PROCEED WITH LOGIN WINDOW..")
            sql = "INSERT INTO `mydb`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
            val = (P_ID, password1, email)
            cursor.execute(sql % val)
            db.commit()
#################################################################################################################################################################
    def pateintlogin(self,u_id,password):     
        cursor.execute("SELECT count(*) FROM `mydb`.`admin` where BINARY ID='" + u_id + "' AND BINARY Password='" + password + "';")
        p1 = cursor.fetchone()
        return p1
#################################################################################################################################################################        
    
    
    def getpatientname(self,val):
#        sql = 
        #cursor.execute("select * from mydb.patient_details where P_ID="+P_ID+";")
#        cursor.execute("select * from mydb.patient_details where P_ID='"+val+"';")
#        m1=cursor.fetchone()
#        print(m1)
         pass
        #print(self.name)
#################################################################################################################################################################        
    def getpatientall(self,pid):
        cursor.execute("SELECT * FROM `mydb`.`patient_details` WHERE P_ID='" +pid+ "';")
        print(cursor.fetchall())
#################################################################################################################################################################            
    def getpatientemail(self,pid):
        cursor.execute("SELECT * FROM `mydb`.`patient_details` WHERE P_ID='" +pid+ "';")
        print(cursor.fetchall())       
#################################################################################################################################################################        
    def getpatientpswrd(self,pid):
        cursor.execute("SELECT Password FROM `mydb`.`admin` WHERE ID='" +pid+ "';")
        x = cursor.fetchone()
        return x[0]
#################################################################################################################################################################
    def getpatientphone(self,pid):
        cursor.execute("SELECT P_Pno FROM `mydb`.`patient_details` WHERE P_ID='" +pid+ "';")
        print(cursor.fetchall())
#################################################################################################################################################################            
    def getpatientaddress(self,pid):
        cursor.execute("SELECT P_Add FROM `mydb`.`patient_details` WHERE P_ID='" +pid+ "';")
        print(cursor.fetchall())       
    
#    def getpatientid(self,pid):
#        cursor.execute("SELECT * FROM `mydb`.`patient_details` WHERE P_ID='" +pid+ "';")
#        print(cursor.fetchall())
#            
    def getpatientage(self,pid):
        cursor.execute("SELECT P_Age FROM `mydb`.`patient_details` WHERE P_ID='" +pid+ "';")
        print(cursor.fetchall())
            
#    def getpatientgender(self,pid):
#        cursor.execute("SELECT * FROM `mydb`.`patient_details` WHERE P_ID='" +pid+ "';")
#        print(cursor.fetchall())
        
#        
#p = patient()  
#val = 'P_109'      
#p.getpatientall(val)
#y = p.getpatientpswrd(val)
#print(y[0])
#db.close()
