# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:15:21 2018"

@author: Jeet"""

from doctorpersonaldetails import doctorpersonaldetails as dpd
from doctorproffessionaldetails import doctorprofessionaldetails as ddd
import datetime
import pymysql
db = pymysql.connect(
                    host='127.0.0.1',
                    user="root",
                    passwd="6%w<RPl4",
                    db="mydb"
                    )
#rint(db)
cursor = db.cursor()

class doctor(dpd,ddd):
    def __init__(self):
        pass

    def editdetail(self):
        print(" __________________________________________________________________________ ")
        print("|-------------------DOCTOR'S PERSONAL DETAILS EDIT WINDOW------------------|")
        print("|                                                                          |")
        print("|                        1. EDIT DOCTOR'S NAME                             |")
        print("|                        2. EDIT DOCTOR'S AGE                              |")
        print("|                        3. EDIT DOCTOR'S PHONE NUMBER                     |")
        print("|                        4. EDIT DOCTOR'S EMAIL                            |")
        print("|                        5. EDIT DOCTOR'S ADDRESS                          |")
        print("|                        6. RETURN TO PREVIOUS PAGE                        |")
        print("|__________________________________________________________________________|")
        do = 1
        while(do):
            try:
                xx = int(input("Enter your choice:....."))
                do = 0
            except ValueError:print("You Entered a string when a integer is required. PLease try again.....")
        if xx == 1:
            did = input("| DOCTOR ID:.. ")

            super().getdocdetail(did)
            print(
                " __________________________________________________________________________ ")
            print(
                "|------------------------IS THE INFORMATION CORRECT------------------------|")
            print(
                "|                                                                          |")
            print(
                "|                                1. YES                                    |")
            print(
                "|                                2. NO                                     |")
            print(
                "|__________________________________________________________________________|")
            do = 1
            while(do):
                try:
                    xxx = int(input("PLEASE SELECT THE OPTION:..."))
                    do = 0
                except ValueError:print("You Entered a string when a integer is required. PLease try again.....")

            if xxx == 1:
                nme = input("| DOCTOR NAME:.. ")
                print(
                    " __________________________________________________________________________ ")
                print(
                    "|------------------------------CONFIRM-------------------------------------|")
                print(
                    "|                                                                          |")
                print(
                    "|                               1. YES                                     |")
                print(
                    "|                               2. NO                                      |")
                print(
                    "|__________________________________________________________________________|")
                do = 1
                while(do):
                    try:
                        xxx = int(input("PLEASE CONFIRM..?"))
                        do = 0
                    except ValueError:print("You Entered a string when a integer is required. PLease try again.....")

                if xxx == 1:
                    super().setdoctorname(nme, did)

                    print(" ___________________________________ ")
                    print("| DOCTOR NAME UPDATED SUCCESSFULLY:...|")
                    super().getdocdetail(did)
                elif xxx == 2:
                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                    for i in range(1, 30000000):
                        pass

                else:
                    print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")

            elif xx == 2:
                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                for i in range(1, 30000000):
                    pass

        elif xx == 2:
            did = input("| DOCTOR ID:.. ")
            super().getdocdetail(did)
            print(
                " __________________________________________________________________________ ")
            print(
                "|------------------------IS THE INFORMATION CORRECT------------------------|")
            print(
                "|                                                                          |")
            print(
                "|                                1. YES                                    |")
            print(
                "|                                2. NO                                     |")
            print(
                "|__________________________________________________________________________|")
            do = 1
            while(do):
                try:
                    xxx = int(input("PLEASE SELECT THE OPTION:..."))
                    do = 0
                except ValueError:print("You Entered a string when a integer is required. PLease try again.....")

            if xxx == 1:
                do = 1
                while(do):
                    try:
                        ageee = int(input("| DOCTOR AGE:.. "))
                        if (ageee <= 25):
                            raise Exception("Only positive values are allowed")
                        do = 0
                    except ValueError:print("You Entered a string when a integer is required. PLease try again.....")
                    except: print("only positive values gretor than 25 are allowed")

                print(
                    " __________________________________________________________________________ ")
                print(
                    "|------------------------------CONFIRM-------------------------------------|")
                print(
                    "|                                                                          |")
                print(
                    "|                              1. YES                                      |")
                print(
                    "|                              2. NO                                       |")
                print(
                    "|__________________________________________________________________________|")
                while(do):
                    try:
                        xxx = int(input("PLEASE CONFIRM..?"))
                        do = 0
                    except ValueError:print("You Entered a string when a integer is required. PLease try again.....")



                if xxx == 1:
                    super().setdoctorage(ageee, did)
                    print(" ___________________________________ ")
                    print("| DOCTOR AGE UPDATED SUCCESSFULLY:...|")
                    super().getdocdetail(did)
                elif xxx == 2:
                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                    for i in range(1, 30000000):
                        pass
                #  continue
                else:
                    print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                #   continue
            elif xx == 2:
                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                for i in range(1, 30000000):
                    pass
                #continue
        elif xx == 3:
            did = input("| DOCTOR ID:.. ")
            super().getdocdetail(did)
            print(
                " __________________________________________________________________________ ")
            print(
                "|------------------------IS THE INFORMATION CORRECT------------------------|")
            print(
                "|                                                                          |")
            print(
                "|                                 1. YES                                   |")
            print(
                "|                                 2. NO                                    |")
            print(
                "|__________________________________________________________________________|")
            xxx = int(input("PLEASE SELECT THE OPTION:..."))
            if xxx == 1:
                do = 1
                while(do):
                    try:
                        phnu = input("| DOCTOR PHONE NUMBER:.. ")
                        if (phnu >= 100000):
                            raise Exception("phone no has to be at least of 6 digits")
                        do = 0
                    except ValueError:print("You Entered a string when a integer is required. PLease try again.....")
                    except: print("only positive values gretor than 25 are allowed")


                print(
                    " __________________________________________________________________________ ")
                print(
                    "|------------------------------CONFIRM-------------------------------------|")
                print(
                    "|                                                                          |")
                print(
                    "|                              1. YES                                      |")
                print(
                    "|                              2. NO                                       |")
                print(
                    "|__________________________________________________________________________|")
                xxx = int(input("PLEASE CONFIRM..?"))
                if xxx == 1:
                    super().setdoctorpno(phnu, did)
                    print(" ___________________________________ ")
                    print("| DOCTOR PHONE NUMBER UPDATED SUCCESSFULLY:...|")
                    super().getdocdetail(did)
                elif xxx == 2:
                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                    for i in range(1, 30000000):
                        pass
                    #
                else:
                    print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                    #continue
            elif xx == 2:
                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                for i in range(1, 30000000):
                    pass
                #continue
        elif xx == 4:
            did = input("| DOCTOR ID:.. ")
            super().getdocdetail(did)
            print(
                " __________________________________________________________________________ ")
            print(
                "|------------------------IS THE INFORMATION CORRECT------------------------|")
            print(
                "|                                                                          |")
            print(
                "|                                 1. YES                                   |")
            print(
                "|                                 2. NO                                     |")
            print(
                "|__________________________________________________________________________|")
            xxx = int(input("PLEASE SELECT THE OPTION:..."))
            if xxx == 1:
                emaii = input("| DOCTOR EMAIL:.. ")
                print(
                    " __________________________________________________________________________ ")
                print(
                    "|------------------------------CONFIRM-------------------------------------|")
                print(
                    "|                                                                          |")
                print(
                    "|                              1. YES                                      |")
                print(
                    "|                              2. NO                                       |")
                print(
                    "|__________________________________________________________________________|")
                xxx = int(input("PLEASE CONFIRM..?"))
                if xxx == 1:
                    super().setdoctoremail(emaii, did)
                    print(" ___________________________________ ")
                    print("| DOCTOR EMAIL UPDATED SUCCESSFULLY:...|")
                    super().getdocdetail(did)
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
            did = input("| DOCTOR ID:.. ")
            super().getdocdetail(did)
            print(
                " __________________________________________________________________________ ")
            print(
                "|------------------------IS THE INFORMATION CORRECT------------------------|")
            print(
                "|                                                                          |")
            print(
                "|                                 1. YES                                   |")
            print(
                "|                                 2. NO                                     |")
            print(
                "|__________________________________________________________________________|")
            xxx = int(input("PLEASE SELECT THE OPTION:..."))
            if xxx == 1:
                addre = input("| DOCTOR ADDRESS:.. ")
                print(
                    " __________________________________________________________________________ ")
                print(
                    "|------------------------------CONFIRM-------------------------------------|")
                print(
                    "|                                                                          |")
                print(
                    "|                              1. YES                                      |")
                print(
                    "|                              2. NO                                       |")
                print(
                    "|__________________________________________________________________________|")
                xxx = int(input("PLEASE CONFIRM..?"))
                if xxx == 1:
                    super().setdoctoraddr(addre, did)
                    print(" ___________________________________ ")
                    print("| DOCTOR ADDRESS UPDATED SUCCESSFULLY:...|")
                    super().getdocdetail(did)
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
    ######################################################################################################################################
    ######################################################################################################################################
    def editdocprofdetail(self):
        print(" __________________________________________________________________________ ")
        print("|-----------------DOCTOR'S PROFESSIONAL DETAILS EDIT WINDOW----------------|")
        print("|                                                                          |")
        print("|                        1. EDIT DOCTOR'S DEPARTMENT                       |")
        print("|                        2. EDIT DOCTOR'S OPD START TIME                   |")
        print("|                        3. EDIT DOCTOR'S OPD END TIME                     |")
        print("|                        4. EDIT DOCTOR'S TYPE                             |")
        print("|                        5. EDIT DOCTOR'S SPECIALIZATION                   |")
        print("|                        6. EDIT DOCTOR'S EXTENSION NUMBER                 |")
        print("|                        7. EDIT DOCTOR'S ROOM NUMBER                      |")
        print("|                        8. RETURN TO PREVIOUS PAGE                        |")
        print("|__________________________________________________________________________|")
        xx = int(input("Enter your choice:....."))
        if xx == 1:
            did = input("| DOCTOR ID:.. ")
            super().getdocprofessinalall(did)
            print(
                " __________________________________________________________________________ ")
            print(
                "|------------------------IS THE INFORMATION CORRECT------------------------|")
            print(
                "|                                                                          |")
            print(
                "|                                1. YES                                    |")
            print(
                "|                                2. NO                                     |")
            print(
                "|__________________________________________________________________________|")
            xxx = int(input("PLEASE SELECT THE OPTION:..."))
            if xxx == 1:
                dep = input("| DOCTOR DEPARTMENT:.. ")
                print(
                    " __________________________________________________________________________ ")
                print(
                    "|------------------------------CONFIRM-------------------------------------|")
                print(
                    "|                                                                          |")
                print(
                    "|                               1. YES                                     |")
                print(
                    "|                               2. NO                                      |")
                print(
                    "|__________________________________________________________________________|")
                xxx = int(input("PLEASE CONFIRM..?"))
                if xxx == 1:
                    super().setdoctordepartment(dep, did)
                    print(" ___________________________________ ")
                    print("| DOCTOR DEPARTMENT UPDATED SUCCESSFULLY:...|")
                    super().getdocprofessinalall(did)
                elif xxx == 2:
                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                    for i in range(1, 30000000):
                        pass
                else:
                    print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
            elif xx == 2:
                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                for i in range(1, 30000000):
                    pass
        elif xx == 2:
            did = input("| DOCTOR ID:.. ")
            super().getdocprofessinalall(did)
            print(
                " __________________________________________________________________________ ")
            print(
                "|------------------------IS THE INFORMATION CORRECT------------------------|")
            print(
                "|                                                                          |")
            print(
                "|                                1. YES                                    |")
            print(
                "|                                2. NO                                     |")
            print(
                "|__________________________________________________________________________|")
            xxx = int(input("PLEASE SELECT THE OPTION:..."))
            if xxx == 1:
                opdst = input("| DOCTOR OPD START TIME:.. ")
                print(
                    " __________________________________________________________________________ ")
                print(
                    "|------------------------------CONFIRM-------------------------------------|")
                print(
                    "|                                                                          |")
                print(
                    "|                              1. YES                                      |")
                print(
                    "|                              2. NO                                       |")
                print(
                    "|__________________________________________________________________________|")
                xxx = int(input("PLEASE CONFIRM..?"))
                if xxx == 1:
                    super().setopdstarttime(opdst, did)
                    print(" ___________________________________ ")
                    print("| DOCTOR OPD START TIME UPDATED SUCCESSFULLY:...|")
                    super().getdocprofessinalall(did)
                elif xxx == 2:
                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                    for i in range(1, 30000000):
                        pass
                else:
                    print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
            elif xx == 2:
                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                for i in range(1, 30000000):
                    pass
        elif xx == 3:
            did = input("| DOCTOR ID:.. ")
            super().getdocprofessinalall(did)
            print(
                " __________________________________________________________________________ ")
            print(
                "|------------------------IS THE INFORMATION CORRECT------------------------|")
            print(
                "|                                                                          |")
            print(
                "|                                 1. YES                                   |")
            print(
                "|                                 2. NO                                    |")
            print(
                "|__________________________________________________________________________|")
            xxx = int(input("PLEASE SELECT THE OPTION:..."))
            if xxx == 1:
                opden = input("| DOCTOR OPD END TIME:.. ")
                print(
                    " __________________________________________________________________________ ")
                print(
                    "|------------------------------CONFIRM-------------------------------------|")
                print(
                    "|                                                                          |")
                print(
                    "|                              1. YES                                      |")
                print(
                    "|                              2. NO                                       |")
                print(
                    "|__________________________________________________________________________|")
                xxx = int(input("PLEASE CONFIRM..?"))
                if xxx == 1:
                    super().setopdendttime(opden, did)
                    print(" ___________________________________ ")
                    print("| DOCTOR OPD END TIME UPDATED SUCCESSFULLY:...|")
                    super().getdocprofessinalall(did)
                elif xxx == 2:
                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                    for i in range(1, 30000000):
                        pass
                else:
                    print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
            elif xx == 2:
                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                for i in range(1, 30000000):
                    pass
        elif xx == 4:
            did = input("| DOCTOR ID:.. ")
            super().getdocprofessinalall(did)
            print(
                " __________________________________________________________________________ ")
            print(
                "|------------------------IS THE INFORMATION CORRECT------------------------|")
            print(
                "|                                                                          |")
            print(
                "|                                 1. YES                                   |")
            print(
                "|                                 2. NO                                     |")
            print(
                "|__________________________________________________________________________|")
            xxx = int(input("PLEASE SELECT THE OPTION:..."))
            if xxx == 1:
                dtyp = input("| DOCTOR TYPE:.. ")
                print(
                    " __________________________________________________________________________ ")
                print(
                    "|------------------------------CONFIRM-------------------------------------|")
                print(
                    "|                                                                          |")
                print(
                    "|                              1. YES                                      |")
                print(
                    "|                              2. NO                                       |")
                print(
                    "|__________________________________________________________________________|")
                xxx = int(input("PLEASE CONFIRM..?"))
                if xxx == 1:
                    super().setdoctype(dtyp, did)
                    print(" ___________________________________ ")
                    print("| DOCTOR TYPE UPDATED SUCCESSFULLY:...|")
                    super().getdocprofessinalall(did)
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
            did = input("| DOCTOR ID:.. ")
            super().getdocprofessinalall(did)
            print(
                " __________________________________________________________________________ ")
            print(
                "|------------------------IS THE INFORMATION CORRECT------------------------|")
            print(
                "|                                                                          |")
            print(
                "|                                 1. YES                                   |")
            print(
                "|                                 2. NO                                     |")
            print(
                "|__________________________________________________________________________|")
            xxx = int(input("PLEASE SELECT THE OPTION:..."))
            if xxx == 1:
                spec = input("| DOCTOR SPECIALIZATION:.. ")
                print(
                    " __________________________________________________________________________ ")
                print(
                    "|------------------------------CONFIRM-------------------------------------|")
                print(
                    "|                                                                          |")
                print(
                    "|                              1. YES                                      |")
                print(
                    "|                              2. NO                                       |")
                print(
                    "|__________________________________________________________________________|")
                xxx = int(input("PLEASE CONFIRM..?"))
                if xxx == 1:
                    super().setdocspecialisation(spec, did)
                    print(" ___________________________________ ")
                    print("| DOCTOR SPECIALIZATION UPDATED SUCCESSFULLY:...|")
                    super().getdocprofessinalall(did)
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
            did = input("| DOCTOR ID:.. ")
            super().getdocprofessinalall(did)
            print(
                " __________________________________________________________________________ ")
            print(
                "|------------------------IS THE INFORMATION CORRECT------------------------|")
            print(
                "|                                                                          |")
            print(
                "|                                 1. YES                                   |")
            print(
                "|                                 2. NO                                     |")
            print(
                "|__________________________________________________________________________|")
            xxx = int(input("PLEASE SELECT THE OPTION:..."))
            if xxx == 1:
                extno = input("| DOCTOR EXTENSION NUMBER:.. ")
                print(
                    " __________________________________________________________________________ ")
                print(
                    "|------------------------------CONFIRM-------------------------------------|")
                print(
                    "|                                                                          |")
                print(
                    "|                              1. YES                                      |")
                print(
                    "|                              2. NO                                       |")
                print(
                    "|__________________________________________________________________________|")
                xxx = int(input("PLEASE CONFIRM..?"))
                if xxx == 1:
                    super().setextensionno(extno, did)
                    print(" ___________________________________ ")
                    print("| DOCTOR EXTENSION NUMBER UPDATED SUCCESSFULLY:...|")
                    super().getdocprofessinalall(did)
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
        elif xx == 7:
            did = input("| DOCTOR ID:.. ")
            super().getdocprofessinalall(did)
            print(
                " __________________________________________________________________________ ")
            print(
                "|------------------------IS THE INFORMATION CORRECT------------------------|")
            print(
                "|                                                                          |")
            print(
                "|                                 1. YES                                   |")
            print(
                "|                                 2. NO                                     |")
            print(
                "|__________________________________________________________________________|")
            xxx = int(input("PLEASE SELECT THE OPTION:..."))
            if xxx == 1:
                rmno = input("| DOCTOR ROOM NUMBER:.. ")
                print(
                    " __________________________________________________________________________ ")
                print(
                    "|------------------------------CONFIRM-------------------------------------|")
                print(
                    "|                                                                          |")
                print(
                    "|                              1. YES                                      |")
                print(
                    "|                              2. NO                                       |")
                print(
                    "|__________________________________________________________________________|")
                xxx = int(input("PLEASE CONFIRM..?"))
                if xxx == 1:
                    super().setroomno(rmno, did)
                    print(" ___________________________________ ")
                    print("| DOCTOR ROOM NUMBER UPDATED SUCCESSFULLY:...|")
                    super().getdocprofessinalall(did)
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
        elif xx == 8:
            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
            for i in range(1, 30000000):
                pass
        else:
            print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
    def patientviewed(self,did):
        x =  input(" ENTER THE PATEINT ID VIEWED")
        cursor.execute("DELETE FROM `mydb`.`doctor_assignment` WHERE PAT_ID = '"+x+"';")
        db.commit()
        cursor.execute("SELECT Ref_ID FROM `mydb`.`patient_medical_history` WHERE PAT_ID = '"+x+"' ORDER BY Ref_ID DESC LIMIT 1")
        aa=cursor.fetchone()
        rid=aa[0]
        cursor.execute("SELECT D_Department FROM `mydb`.`doctor_professional_details` WHERE D_DID = '"+did+"';" )
        aa=cursor.fetchone()
        dep = aa[0]
        pres=input("ENTER THE PRESCRIPTION")
        dis=input("ENTER THE DISEASE")
        dov=input("ENTER THE DAY OF VISIT")
        dod=input("ENTER THE DAY OF DISCHARGE")
        tov=input("ENTER THE TIME OF VISIT")
        tod=input("ENTER THE TIME OF DISCHARGE")
        test=input("ENTER  test")
        sql="INSERT INTO `mydb`.`patient_medical_history`(`Ref_ID`,`Pat_ID`,`Prescription`,`Past_Reports`,`dayofvisit`,`timeofvisit`,`dayofdischarge`,`dischargetime`,`department`,`d_id`,`disease`,`test`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        val = (rid,x,pres,'',dov,tov,dod,tod,dep,did,dis,test)
        cursor.execute(sql % val)
        db.commit()
    #
    #
# d1 = doctor()
# d1.editdetail()
