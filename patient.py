import pymysql
import datetime
db = pymysql.connect(
    host='127.0.0.1',
    user="root",
    passwd="",
    db="project"
)
# print(project)
cursor = db.cursor()


class patient:
    def __init__(self,id='',name='',address='',location='',assdoc='',dov='',tov=''):
        self.id=id
        self.name=name
        self.address=address
        self.location=location
        self.assdoc=assdoc
        self.dov=dov
        self.tov=tov
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
            self.id = input("| PATIENT ID:.. ")
            self.getpatientall(self.id)  ###### getting all details of
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
                    self.setpateintname(nm, self.id)
                    print(" ___________________________________ ")
                    print("| PATIENT NAME UPDATED SUCCESSFULLY:...|")
                    self.getpatientall(self.id)
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
            self.id = input("| PATIENT ID:.. ")
            self.getpatientall(self.id)
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
                    self.setpateintage(agee, self.id)
                    print(" ___________________________________ ")
                    print("| PATIENT AGE UPDATED SUCCESSFULLY:...|")
                    self.getpatientall(self.id)
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
            self.id = input("| PATIENT ID:.. ")
            self.getpatientall(self.id)
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
                    self.setpatientphone(self.id, phno)
                    print(" ___________________________________ ")
                    print("| PATIENT PHONE NUMBER UPDATED SUCCESSFULLY:...|")
                    self.getpatientall(self.id)
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
            self.id = input("| PATIENT ID:.. ")
            self.getpatientall(self.id)
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
                    self.setpatientemail(self.id, emai)
                    print(" ___________________________________ ")
                    print("| PATIENT EMAIL UPDATED SUCCESSFULLY:...|")
                    self.getpatientall(self.id)
                elif xxx == 2:
                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                    for i in range(1, 30000000):
                        pass
                    # continue
                else:
                    print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                    # continue
            elif xx == 2:
                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                for i in range(1, 30000000):
                    pass
                # continue
        elif xx == 5:
            self.id = input("| PATIENT ID:.. ")
            self.getpatientall(self.id)
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
                    self.setpatientaddress(self.id, addr)
                    print(" ___________________________________ ")
                    print("| PATIENT ADDRESS UPDATED SUCCESSFULLY:...|")
                    self.getpatientall(self.id)
                elif xxx == 2:
                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                    for i in range(1, 30000000):
                        pass
                    # continue
                else:
                    print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                    # continue
            elif xx == 2:
                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                for i in range(1, 30000000):
                    pass
                # continue
        elif xx == 6:
            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
            for i in range(1, 30000000):
                pass
            # continue
        else:
            print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
            # continue

    #################################################################################################################################################################

    def editpatientself(self):
        print(" __________________________________________________________________________ ")
        print("|----------------------------EDIT PROFILE----------------------------------|")
        print("|                                                                          |")
        print("|                            1. EDIT NAME :                                |")
        print("|                            2. EDIT EMAIL ID:                             |")
        print("|                            3. EDIT ADDRESS:                              |")
        print("|                            4. EDIT PHONE NO:                             |")
        print("|                            5. EDIT AGE:                                  |")
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
    def setpateintname(self, nm, pid):
        self.id=pid
        cursor.execute("UPDATE `project`.`patient_details` SET P_Name = '" + nm + "' WHERE P_ID = '" + self.id + "';")
        db.commit()

    #################################################################################################################################################################
    def setpatientemail(self, emai, pid):
        self.id=pid
        cursor.execute("UPDATE `project`.`patient_details` SET P_Email = '" + emai + "' WHERE P_ID = '" + self.id + "';")
        db.commit()

    #################################################################################################################################################################
    def setpatientphone(self, phno, pid):
        self.id=pid
        cursor.execute("UPDATE `project`.`patient_details` SET P_PNo = '" + phno + "' WHERE P_ID = '" + self.id + "';")
        db.commit()

    #################################################################################################################################################################
    def setpateintage(self, age, pid):
        self.id=pid
        cursor.execute("UPDATE `project`.`patient_details` SET P_Age = '" + age + "' WHERE P_ID = '" + self.id + "';")
        db.commit()

    #################################################################################################################################################################
    def setpatientaddress(self, pid, addr):
        self.id=pid
        cursor.execute("UPDATE `project`.`patient_details` SET P_Add = '" + addr + "' WHERE P_ID = '" + self.id + "';")
        db.commit()

    #################################################################################################################################################################
    def getidpno(self, pno):
        cursor.execute("SELECT P_ID FROM `project`.`patient_details` WHERE P_PNo='" + pno + "';")
        x = cursor.fetchone()
        return x[0]

    #################################################################################################################################################################

    def setpassword(self, age, pid):
        self.id=pid
        cursor.execute("UPDATE `project`.`admin` SET Password = '" + age + "' WHERE ID = '" + self.id + "';")
        db.commit()

    #################################################################################################################################################################
    # def registerpatient(self):
    #     name = input("| NAME:.. ")
    #     email = input("| EMAIL ID:.. ")
    #     phoneno = int(input("| PHONE NUMBER:....."))
    #     age = int(input("| AGE:....."))
    #     adress = input("| ADDRESS:")
    #     #               gender = input("enter the gender:.....")
    #     #               pateint_type = input("OPD or Location:..............")
    #     password1 = input("| PASSWORD:..... ")
    #     password2 = input("| RE-TYPE PASSWORD:......")  ##### also rechecks the password
    #     if password1 == password2:
    #         ######### need to be changed according to table
    #         cursor.execute("SELECT SUBSTRING(P_ID,3,5) FROM `project`.`patient_details` ORDER BY P_ID DESC LIMIT 1")
    #         p1 = cursor.fetchone()
    #         y = str(int(p1[0]) + 1)
    #         x = 'P_'
    #         P_ID = x + y
    #         sql = "INSERT INTO `project`.`patient_details` (P_ID,P_Name,P_Age,P_PNo,P_Add,P_Email) VALUES('%s','%s',%s,%s,'%s','%s')"
    #         val = (P_ID, name, age, phoneno, adress, email)
    #         cursor.execute(sql % val)
    #         project.commit()
    #         print(" ___________________________________ ")
    #         print("| PATIENT REGISTRATION COMPLETED:...|")
    #         print("| USER ID:... ", P_ID)
    #         print("| PLEASE PROCEED WITH LOGIN WINDOW..")
    #         sql = "INSERT INTO `project`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
    #         val = (P_ID, password1, email)
    #         cursor.execute(sql % val)
    #         project.commit()

    def registerpatient(self):
        do = 1
        while do:
            try:
                name = input("| NAME:.. ")
                if name == '':
                    raise Exception
                else:
                    break
            except:
                print(".....THIS FIELD CANNOT BE LEFT EMPTY.....")
        d = 1
        while do:
            try:
                email = input("| EMAIL ID:.. ")
                if email == '':
                    raise Exception
                else:
                    break
            except:
                print(".....THIS FIELD CANNOT BE LEFT EMPTY.....")
        d = 1
        while do:
            try:
                phoneno = int(input("| PHONE NUMBER:....."))
                if phoneno == '':
                    raise Exception
                else:
                    break
            except:
                exceptValueError: print("Please enter a valid format of age")
            age = int(input("| AGE:....."))
            adress = input("| ADDRESS:")
            do = 1
        d = 1
        while do:
            try:
                password1 = input("| PASSWORD:..... ")
                if password1 == '':
                    raise Exception
                else:
                    break
            except:
                print("Please enter a valid password")
        password2 = input("| RE-TYPE PASSWORD:......")  ##### also rechecks the password
        if password1 == password2:
            ######### need to be changed according to table
            cursor.execute("SELECT SUBSTRING(P_ID,3,5) FROM `myproject`.`patient_details` ORDER BY P_ID DESC LIMIT 1")
            p1 = cursor.fetchone()
            y = str(int(p1[0]) + 1)
            x = 'P_'
            P_ID = x + y
            sql = "INSERT INTO `myproject`.`patient_details` (P_ID,P_Name,P_Age,P_PNo,P_Add,P_Email) VALUES('%s','%s',%s,%s,'%s','%s')"
            val = (P_ID, name, age, phoneno, adress, email)
            cursor.execute(sql % val)
            db.commit()
            print(" ___________________________________ ")
            print("| PATIENT REGISTRATION COMPLETED:...|")
            print("| USER ID:... ", P_ID)
            print("| PLEASE PROCEED WITH LOGIN WINDOW..")
            sql = "INSERT INTO `myproject`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
            val = (P_ID, password1, email)
            cursor.execute(sql % val)
            db.commit()
        else:
            print("WRONG PASSWORD")


        # do = 1
        # while do:
        #     try:
        #         age = int(input("| AGE:....."))
        #         if age <= 5:
        #             raise Exception
        #         else:
        #             do = 0
        #     except ValueError:
        #         print("Please enter a valid format of age")
        #     except:
        #         print("INVALID AGE")
        # adress = input("| ADDRESS:")
        # #               gender = input("enter the gender:.....")
        # #               pateint_type = input("OPD or Location:..............")
        #
        # do = 1
        # while do:
        #     try:
        #         password1 = input("| PASSWORD:..... ")
        #         if password1 == '':
        #             raise Exception
        #         else:
        #             do = 0
        #     except:
        #         print("Please enter a valid password")
        # password2 = input("| RE-TYPE PASSWORD:......")  ##### also rechecks the password
        # if password1 == password2:
        #     ######### need to be changed according to table
        #     cursor.execute("SELECT SUBSTRING(P_ID,3,5) FROM `project`.`patient_details` ORDER BY P_ID DESC LIMIT 1")
        #     p1 = cursor.fetchone()
        #     y = str(int(p1[0]) + 1)
        #     x = 'P_'
        #     P_ID = x + y
        #     sql = "INSERT INTO `project`.`patient_details` (P_ID,P_Name,P_Age,P_PNo,P_Add,P_Email) VALUES('%s','%s',%s,%s,'%s','%s')"
        #     val = (P_ID, name, age, phoneno, adress, email)
        #     cursor.execute(sql % val)
        #     project.commit()
        #     print(" ___________________________________ ")
        #     print("| PATIENT REGISTRATION COMPLETED:...|")
        #     print("| USER ID:... ", P_ID)
        #     print("| PLEASE PROCEED WITH LOGIN WINDOW..")
        #     sql = "INSERT INTO `project`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
        #     val = (P_ID, password1, email)
        #     cursor.execute(sql % val)
        #     project.commit()

    #################################################################################################################################################################
    def pateintlogin(self, u_id, password):
        cursor.execute(
            "SELECT count(*) FROM `project`.`admin` where BINARY ID='" + u_id + "' AND BINARY Password='" + password + "';")
        p1 = cursor.fetchone()
        return p1

    #################################################################################################################################################################

    def getpatientname(self, val):
        #        sql =
        # cursor.execute("select * from project.patient_details where P_ID="+P_ID+";")
        #        cursor.execute("select * from project.patient_details where P_ID='"+val+"';")
        #        m1=cursor.fetchone()
        #        print(m1)
        pass

    # print(self.name)
    #################################################################################################################################################################
    def getpatientall(self, pid):
        self.id=pid
        if cursor.execute("SELECT * FROM `project`.`patient_details` WHERE P_ID='" + self.id + "';"):
            print(cursor.fetchall())
            return 0
        else:
            return 1

    #################################################################################################################################################################
    def getpatientemail(self, pid):
        self.id=pid
        if cursor.execute("SELECT * FROM `project`.`patient_details` WHERE P_ID='" + self.id + "';"):
            print(cursor.fetchall())
            return 0
        else:
            return 1

    #################################################################################################################################################################
    def getpatientpswrd(self, pid):
        self.id=pid
        cursor.execute("SELECT Password FROM `project`.`admin` WHERE ID='" + self.id + "';")
        x = cursor.fetchone()
        return x[0]

    #################################################################################################################################################################
    def getpatientphone(self, pid):
        self.id=pid
        if cursor.execute("SELECT P_Pno FROM `project`.`patient_details` WHERE P_ID='" + self.id + "';"):
            print(cursor.fetchall())
            return 0
        else:
            return 1
    #################################################################################################################################################################
    def getpatientaddress(self, pid):
        self.id=pid
        if cursor.execute("SELECT P_Add FROM `project`.`patient_details` WHERE P_ID='" + self.id + "';"):
            print(cursor.fetchall())
            return 0
        else:
            return 1

    #    def getpatientid(self,self.id):
    #        cursor.execute("SELECT * FROM `project`.`patient_details` WHERE P_ID='" +self.id+ "';")
    #        print(cursor.fetchall())
    #
    def getpatientage(self, pid):
        self.id=pid
        if cursor.execute("SELECT P_Age FROM `project`.`patient_details` WHERE P_ID='" + self.id + "';"):
            print(cursor.fetchall())
            return 0
        else:
            return 1
    def searchdoctor(self,h1,u_id):
        print(" __________________________________________________________________________ ")
        print("|---------------------------DOCTOR SEARCH WINDOW---------------------------|")
        print("|                                                                          |")
        print("|                           1. SEARCH BY DOCTOR'S NAME                     |")
        print("|                           2. SEARCH BY DOCTOR'S ID                       |")  #### WRITE LOGIC FOR EACH AND EVERY ONE
        print("|                           3. SEARCH BY DEPARTMENT                        |")  #### show available departments
        print("|                           4. EXIT                                        |")
        print("|__________________________________________________________________________|")
        x = int(input("| ENTER YOUR CHOICE:..."))
        if x == 1:
            print(" __________________________________________________________________________ ")
            print("|-----------------------------SEARCH WINDOW--------------------------------|")
            print("|                                                                          |")
            ch = input("| ENTER THE DOCTOR'S NAME TO BE SEARCHED:... ")
            print("| DOCTOR'S LIST")
            h1.getdoctorsname(ch)
            print("| 1. WANT TO MAKE AN APPOINTMENT:...")
            print("| 2. RETURN TO PREVIOUS WINDOW:... ")
            x = int(input("| PLEASE MAKE A SELECTION:... "))
            if x == 1:
                y = input("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                print(h1.getappointmentid(y, u_id))
                # print("Are you want a specific department or general appointment")
                # print("1. Enter Department")
                # print("2. general patient")
                # ch = input("enter your choice:..........")
                # if ch == 1:
                #     h1.getdepartments()
                #     dep = input("enter the department from the given department:")
                #     print(h1.getappointmentid(y, u_id))
                #     print("please wait when  appointment  finalised")
                #     i = 1000000
                #     while (i >= 0):
                #         i = i - 1
                #     print("your appoinmnet has been fixed ")
                #     print("your id and details are:")
                #
                #
                # elif ch == 2:
                #     dep = 'General'
                #     h1.getappointment(dep, u_id)
                #     print("please wait when  appointmnet  finalised")
                #     i = 1000000
                #     while (i >= 0):
                #         i = i - 1
                #     print("your appoinmnet has been fixed ")
                #     print("your id and details are:")
                # else:
                #     print("wrong choice")
                #     #continue
                # pass
            else:
                pass
        elif x == 2:
            ch = input("| ENTER THE DEPARTMENT TO BE SEARCHED:... ")
            print("| DOCTOR'S LIST:... ")
            h1.getdoctorsdept(ch)
            print("| 1. WANT TO MAKE AN APPOINTMENT:...")
            print("| 2. RETURN TO PREVIOUS WINDOW:... ")
            x = int(input("| PLEASE MAKE A SELECTION:... "))
            if x == 1:
                ##### random exception handling sholud be used
                y = input("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                ######### apointment table should be used
                print(h1.getappointmentid(y, u_id))
            else:
                pass
            print("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
        elif x == 3:
            print("| LIST OF DEPARTMENTS:...")
            cursor.execute("SELECT Dep_Name FROM project.department")
            print(cursor.fetchall())
            cha = input("| ENTER THE DEPARTMENT TO BE SEARCHED:... ")
            print("| DOCTOR'S LIST:... ")
            cursor.execute("SELECT * FROM project.doctor_details WHERE BINARY D_ID IN (SELECT D_DID FROM project.doctor_professional_details WHERE BINARY D_Department ='" + cha + "');")
            print(cursor.fetchall())
            print("| 1. WANT TO MAKE AN APPOINTMENT:...")
            print("| 2. RETURN TO PREVIOUS WINDOW:... ")
            x = int(input("| PLEASE MAKE A SELECTION:... "))
            if x == 1:
                ##### random exception handling sholud be used
                y = input("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                ######### apointment table should be used
                print(h1.getappointmentid(y, u_id))
            else:
                pass
            print("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
        else:
            return False


    # def registerpatient(self):
    #     name = input("| NAME:.. ")
    #     email = input("| EMAIL ID:.. ")
    #     phoneno = int(input("| PHONE NUMBER:....."))
    #     age = int(input("| AGE:....."))
    #     adress = input("| ADDRESS:")
    #     #               gender = input("enter the gender:.....")
    #     #               pateint_type = input("OPD or Location:..............")
    #     password1 = input("| PASSWORD:..... ")
    #     password2 = input("| RE-TYPE PASSWORD:......")  ##### also rechecks the password
    #     if password1 == password2:
    #         ######### need to be changed according to table
    #         cursor.execute("SELECT SUBSTRING(P_ID,3,5) FROM `project`.`patient_details` ORDER BY P_ID DESC LIMIT 1")
    #         p1 = cursor.fetchone()
    #         y = str(int(p1[0]) + 1)
    #         x = 'P_'
    #         P_ID = x + y
    #         sql = "INSERT INTO `project`.`patient_details` (P_ID,P_Name,P_Age,P_PNo,P_Add,P_Email) VALUES('%s','%s',%s,%s,'%s','%s')"
    #         val = (P_ID, name, age, phoneno, adress, email)
    #         cursor.execute(sql % val)
    #         project.commit()
    #         print(" ___________________________________ ")
    #         print("| PATIENT REGISTRATION COMPLETED:...|")
    #         print("| USER ID:... ", P_ID)
    #         print("| PLEASE PROCEED WITH LOGIN WINDOW..")
    #         sql = "INSERT INTO `project`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
    #         val = (P_ID, password1, email)
    #         cursor.execute(sql % val)
    #         project.commit()

    def appointment(self,u_id,h1):
        print(" __________________________________________________________________________ ")
        print("|----------------------------OPD/LOCAL BOOKING WINDOW----------------------|")
        print("|                            1. OPD                                        |")
        print("|                            2. LOCAL                                      |")
        print("|                            3. EXIT                                       |")
        print("|__________________________________________________________________________|")
        innn = int(input("| PLEASE MAKE A SELECTION:..."))
        if innn == 1:
            print(" __________________________________________________________________________ ")
            print("|-------------------PATIENT'S APPOINTMENT BOOKING WINDOW-------------------|")
            print("|                            1. AUTOMATIC APPOINTMENT                      |")
            print("|                            2. MANUAL APPOINTMENT                         |")
            print("|                            3. EXIT                                       |")
            print("|__________________________________________________________________________|")
            inn=int(input("| PLEASE MAKE A SELECTION:..."))
            if inn==1:
                cursor.execute("SELECT DISTINCT Dep_Name FROM `project`.`department`")
                print(cursor.fetchall())
                ch = input("| ENTER THE DEPARTMENT FOR WHICH APPOINTMENT IS NEEDED:... ")
                if(int(cursor.execute("SELECT count(Dep_Name) FROM `project`.`department` where Dep_Name='" + ch + "';"))==1):
                    sql = "INSERT INTO `project`.`unassigned_patient` (`UP_ID`, `UP_PROB_DEP`, `UP_E_TYPE`)VALUES('%s','%s','%s')"
                    val = (u_id,ch,"")
                    cursor.execute(sql % val)
                    db.commit()
                    cursor.execute("SELECT Dep_sym FROM `project`.`department` where Dep_Name='" + ch + "';")
                    aaa=cursor.fetchone()
                    bbb=aaa[0]
                    now = datetime.datetime.now()
                    ccc=u_id+'_'+bbb+'_OPD_'+str(now)
                    print("TOKEN NUMBER OF THE PATIENT IS:",ccc)
                    sql = "INSERT INTO `project`.`patient_medical_history` (`Ref_ID`,`Pat_ID`,`Prescription`,`Past_Reports`) VALUES ('%s','%s','%s','%s')"
                    val = (ccc,u_id,'','')
                    cursor.execute(sql % val)
                    db.commit()
                else:
                    print("WRONG SELECTION..PLEASE ENTER THE CORRECT DEPARTMENT")
                    #continue
            elif inn==2:
                self.searchdoctor(h1,u_id)
            elif inn==3:
                pass
        elif innn == 2:
            print(" __________________________________________________________________________ ")
            print("|---------------------PATIENT'S LOCAL BOOKING WINDOW-----------------------|")
            print("|                            1. LOCAL  APPOINTMENT                         |")
            print("|                            2. EXIT                                       |")
            print("|__________________________________________________________________________|")
            inn = int(input("| PLEASE MAKE A SELECTION:..."))
            if inn == 1:
                cursor.execute("SELECT DISTINCT Dep_Name FROM `project`.`department`")
                print(cursor.fetchall())
                ch = input("| ENTER THE DEPARTMENT FOR WHICH PATIENT NEEDS TO BE ADMITTED:... ")
                if (int(cursor.execute("SELECT count(Dep_Name) FROM `project`.`department` where Dep_Name='" + ch + "';")) == 1):
                    sql = "INSERT INTO `project`.`unassigned_patient` (`UP_ID`, `UP_PROB_DEP`, `UP_E_TYPE`)VALUES('%s','%s','%s')"
                    val = (u_id, ch, "")
                    cursor.execute(sql % val)
                    db.commit()
                    cursor.execute("SELECT Dep_sym FROM `project`.`department` where Dep_Name='" + ch + "';")
                    aaa = cursor.fetchone()
                    if (aaa==None):
                        xx = 0
                    else:
                        xx = aaa[0]
                    bbb=xx
                    now = datetime.datetime.now()
                    ccc = u_id + '_' + bbb + '_LOCAL_' + str(now)
                    print("TOKEN NUMBER OF THE PATIENT IS:", ccc)
                    sql = "INSERT INTO `project`.`patient_medical_history` (`Ref_ID`,`Pat_ID`,`Prescription`,`Past_Reports`) VALUES ('%s','%s','%s','%s')"
                    val = (ccc, u_id, '', '')
                    cursor.execute(sql % val)
                    db.commit()
                    if (cursor.execute("SELECT count(Status) FROM `project`.`local` where DEP='" + ch + "';")==0):
                        sql = "INSERT INTO `project`.`local` (`RoomNo`,`Dep`,`Status`,`P_ID`) VALUES (%s,'%s','%s','%s')"
                        val = (1, ch,'Y',u_id)
                        cursor.execute(sql % val)
                        db.commit()
                    else:
                        if(cursor.execute("SELECT count(RoomNo) FROM `project`.`local` where DEP='" + ch + "';")==0):
                            cursor.execute("SELECT RoomNo FROM `project`.`local` where DEP='" + ch + "' ORDER BY RoomNo DESC LIMIT 1;")
                            aaa = cursor.fetchone()
                            if (aaa == 'None'):
                                xx = 0
                            else:
                                xx = aaa[0]
                            bbb = xx
                            sql = "INSERT INTO `project`.`local` (`RoomNo`,`Dep`,`Status`,`P_ID`) VALUES (%s,'%s','%s','%s')"
                            val = (bbb+1, ch, 'Y', u_id)
                            cursor.execute(sql % val)
                            db.commit()
                        else:
                            cursor.execute("SELECT RoomNo FROM `project`.`local` where DEP='" + ch + "' AND Status='N' ORDER BY RoomNo ASC LIMIT 1;")
                            aaa = cursor.fetchone()
                            if (aaa!=None):
                                xx = aaa[0]
                            else:
                                xx = 0
                            bbb = xx
                            sql = "INSERT INTO `project`.`local` (`RoomNo`,`Dep`,`Status`,`P_ID`) VALUES (%s,'%s','%s','%s')"
                            val = (bbb, ch, 'Y', u_id)
                            cursor.execute(sql % val)
                            db.commit()

                else:
                    print("WRONG SELECTION..PLEASE ENTER THE CORRECT DEPARTMENT")
                    # continue
            elif inn == 2:
                pass
        else:
            pass
# def getpatientgender(self,self.id):
#        cursor.execute("SELECT * FROM `project`.`patient_details` WHERE P_ID='" +self.id+ "';")
#        print(cursor.fetchall())

#
# p = patient()
# val = 'P_109'
# p.appointment('P_129','a')
# y = p.getpatientpswrd(val)
# print(y[0])
# project.close()