import sys
from patient import patient as p
from patientmedicalreport import patientmedicalreport as pmr

from admin import admin
from doctorpersonaldetails import doctorpersonaldetails as dpd
from doctorproffessionaldetails import doctorprofessionaldetails as ddd
from Hospital import Hospital as h
import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user="root",
    passwd="",
    db="db"
)
print(db)
cursor = db.cursor()
print(cursor)

def main():
    while True:
        print(" ______________________________________________________________________ ")
        print("|-------------------------SMART HEALTH CARE SYSTEM---------------------|")
        print("|                                                                      |")
        print("|                            1. ADMIN LOGIN                            |")
        print("|                            2. DOCTOR LOGIN                           |")
        print("|                            3. PATIENT REGISTRATION WINDOW            |")
        print("|                            4. EXISTING USER                          |")
        print("|                            5. RESET PASSWORD                         |")
        print("|                            6. EMERGENCY                              |")
        print("|                            7. Exit                                   |")
        print("|______________________________________________________________________|")
        print("| PLEASE MAKE A SELECTION:... ")
        x = int(input())
        if x == 1:
            aa = 1
            while aa <= 3:
                pswrd = input("Enter password: ")
                if pswrd == '1234':
                    while True:
                        print(" __________________________________________________________________________ ")
                        print("|--------------------WELCOME TO ADMINISTRATIVE MODE------------------------|")
                        print("|                                                                          |")
                        print("|                       1. VIEW ALL DOCTORS                                |")
                        print("|                       2. VIEW ALL PATIENTS                               |")
                        print("|                       3. ASSIGN DOCTORS                                  |")
                        print("|                       4. ADD DOCTORS                                     |")
                        print("|                       5. DATABASE MANAGEMENT                             |")
                        print("|                       6. LOGOUT                                          |")
                        print("|__________________________________________________________________________|")
                        ch = int(input("Enter your choice:"))
                        a1 = admin()
                        if ch == 1:
                            a1.getdoctors()
                        elif ch == 2:
                            a1.getpatients()
                        elif ch == 3:
                            cursor.execute("SELECT COUNT(UP_ID) FROM `db`.`unassigned_patient`")
                            p1 = cursor.fetchone()
                            y = p1[0]
                            for i in range (1,y):
                                cursor.execute("SELECT UP_ID FROM `db`.`unassigned_patient` ORDER BY UP_ID ASC LIMIT 1")
                                p2=cursor.fetchone()
                                y2=p2[0]
                                # print(y2)
                                cursor.execute("SELECT D_DID FROM `db`.`doctor_professional_details` WHERE D_Department=(SELECT UP_PROB_DEP FROM `db`.`unassigned_patient` WHERE UP_ID=(SELECT UP_ID FROM `db`.`unassigned_patient` ORDER BY UP_ID ASC LIMIT 1));")
                                p3=cursor.fetchone()
                                y3=p3[0]
                                # print(y3)
                                sql = "INSERT INTO `db`.`doctor_assignment` (`DOC_ID`, `PAT_ID`, `DOC_MAX_LMT`, `REF_DOC_ID`) VALUES('%s','%s',%s,'%s')"
                                val = (y3,y2,20,'')
                                cursor.execute(sql % val)
                                db.commit()
                                cursor.execute("DELETE FROM `db`.`unassigned_patient` WHERE UP_ID='"+ y2 +"';")
                                db.commit()
                            print("AUTOMATIC ASSIGNMENT SUCCESSFUL")
                        elif ch == 4:
                            a1.adddoctor()
                        elif ch == 5:
                            print(" __________________________________________________________________________ ")
                            print("|-------------------------DATABASE MANAGEMENT WINDOW-----------------------|")
                            print("|                                                                          |")
                            print("|                        1. PATIENT'S PERSONAL DETAILS                     |")
                            print("|                        2. PATIENT'S MEDICAL HISTORY                      |")
                            print("|                        3. DOCTOR'S PERSONAL DETAILS                      |")
                            print("|                        4. DOCTOR'S PROFESSIONAL DETAILS                  |")
                            print("|                        5. HOD MANAGEMENT                                 |")
                            print("|                        6. RETURN TO PREVIOUS PAGE                        |")
                            print("|                        7. LOGOUT                                         |")
                            print("|__________________________________________________________________________|")
                            x = int(input("Enter your choice:....."))
                            if x == 1:
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
                                p1 = p()
                                if xx == 1:
                                    pid = input("| PATIENT ID:.. ")
                                    p1.getpatientall(pid)  ###### getting all details of
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
                                            p1.setpateintname(nm, pid)
                                            print(" ___________________________________ ")
                                            print("| PATIENT NAME UPDATED SUCCESSFULLY:...|")
                                            p1.getpatientall(pid)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 2:
                                    pid = input("| PATIENT ID:.. ")
                                    p1.getpatientall(pid)
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
                                            p1.setpateintage(agee, pid)
                                            print(" ___________________________________ ")
                                            print("| PATIENT AGE UPDATED SUCCESSFULLY:...|")
                                            p1.getpatientall(pid)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 3:
                                    pid = input("| PATIENT ID:.. ")
                                    p1.getpatientall(pid)
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
                                            p1.setpatientphone(pid, phno)
                                            print(" ___________________________________ ")
                                            print("| PATIENT PHONE NUMBER UPDATED SUCCESSFULLY:...|")
                                            p1.getpatientall(pid)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 4:
                                    pid = input("| PATIENT ID:.. ")
                                    p1.getpatientall(pid)
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
                                            p1.setpatientemail(pid, emai)
                                            print(" ___________________________________ ")
                                            print("| PATIENT EMAIL UPDATED SUCCESSFULLY:...|")
                                            p1.getpatientall(pid)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 5:
                                    pid = input("| PATIENT ID:.. ")
                                    p1.getpatientall(pid)
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
                                            p1.setpatientaddress(pid, addr)
                                            print(" ___________________________________ ")
                                            print("| PATIENT ADDRESS UPDATED SUCCESSFULLY:...|")
                                            p1.getpatientall(pid)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 6:
                                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                    for i in range(1, 30000000):
                                        pass
                                    continue
                                else:
                                    print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                    continue
                            elif x == 2:
                                print(" __________________________________________________________________________ ")
                                print("|----------------PATIENT'S MEDICAL HISTORY EDIT WINDOW---------------------|")
                                print("|                                                                          |")
                                print("|                        1. EDIT PATIENT'S PRESCRIPTION                    |")
                                print("|                        2. EDIT PATIENT'S PAST REPORTS                    |")
                                print("|                        3. RETURN TO PREVIOUS PAGE                        |")
                                print("|__________________________________________________________________________|")
                                xx = int(input("Enter your choice:....."))
                                if xx == 1:
                                    pass
                                elif xx == 2:
                                    pass
                                elif xx == 3:
                                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                    for i in range(1, 30000000):
                                        pass
                                    continue
                                else:
                                    print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                    continue
                            elif x == 3:
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
                                xx = int(input("Enter your choice:....."))
                                if xx == 1:
                                    did = input("| DOCTOR ID:.. ")
                                    d1 = dpd()
                                    d1.getdocdetail(did)
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
                                        xxx = int(input("PLEASE CONFIRM..?"))
                                        if xxx == 1:
                                            d1.setdoctorname(nme, did)

                                            print(" ___________________________________ ")
                                            print("| DOCTOR NAME UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 2:
                                    did = input("| DOCTOR ID:.. ")
                                    d1.getdocdetail(did)
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
                                        ageee = input("| DOCTOR AGE:.. ")
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
                                            d1.setdoctorage(ageee, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR AGE UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 3:
                                    did = input("| DOCTOR ID:.. ")
                                    d1.getdocdetail(did)
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
                                        phnu = input("| DOCTOR PHONE NUMBER:.. ")
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
                                            d1.setdoctorpno(phnu, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR PHONE NUMBER UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 4:
                                    did = input("| DOCTOR ID:.. ")
                                    d1.getdocdetail(did)
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
                                            d1.setdoctoremail(emaii, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR EMAIL UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 5:
                                    did = input("| DOCTOR ID:.. ")
                                    d1.getdocdetail(did)
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
                                            d1.setdoctoraddr(addre, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR ADDRESS UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 6:
                                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                    for i in range(1, 30000000):
                                        pass
                                    continue
                                else:
                                    print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                    continue
                            elif x == 4:
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
                                d2 = ddd()
                                if xx == 1:
                                    did = input("| DOCTOR ID:.. ")
                                    d2.getdocprofessinalall(did)
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
                                            d2.setdoctordepartment(dep, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR DEPARTMENT UPDATED SUCCESSFULLY:...|")
                                            d2.getdocprofessinalall(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 2:
                                    did = input("| DOCTOR ID:.. ")
                                    d2.getdocprofessinalall(did)
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
                                            d2.setopdstarttime(opdst, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR OPD START TIME UPDATED SUCCESSFULLY:...|")
                                            d2.getdocprofessinalall(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 3:
                                    did = input("| DOCTOR ID:.. ")
                                    d2.getdocprofessinalall(did)
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
                                            d2.setopdendttime(opden, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR OPD END TIME UPDATED SUCCESSFULLY:...|")
                                            d2.getdocprofessinalall(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 4:
                                    did = input("| DOCTOR ID:.. ")
                                    d2.getdocprofessinalall(did)
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
                                            d2.setdoctype(dtyp, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR TYPE UPDATED SUCCESSFULLY:...|")
                                            d2.getdocprofessinalall(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 5:
                                    did = input("| DOCTOR ID:.. ")
                                    d2.getdocprofessinalall(did)
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
                                            d2.setdocspecialisation(spec, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR SPECIALIZATION UPDATED SUCCESSFULLY:...|")
                                            d2.getdocprofessinalall(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 6:
                                    did = input("| DOCTOR ID:.. ")
                                    d2.getdocprofessinalall(did)
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
                                            d2.setextensionno(extno, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR EXTENSION NUMBER UPDATED SUCCESSFULLY:...|")
                                            d2.getdocprofessinalall(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 7:
                                    did = input("| DOCTOR ID:.. ")
                                    d2.getdocprofessinalall(did)
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
                                            d2.setroomno(rmno, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR ROOM NUMBER UPDATED SUCCESSFULLY:...|")
                                            d2.getdocprofessinalall(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 8:
                                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                    for i in range(1, 30000000):
                                        pass
                                    continue
                                else:
                                    print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                    continue
                            elif x == 5:
                                print(" __________________________________________________________________________ ")
                                print("|----------------------HOD MANAGEMENT EDIT WINDOW--------------------------|")
                                print("|                                                                          |")
                                print("|                        1. HOD ASSIGNMENT                                 |")
                                print("|                        2. VIEW HOD LIST                                  |")
                                print("|                        3. RETURN TO PREVIOUS PAGE                        |")
                                print("|__________________________________________________________________________|")
                                xx = int(input("Enter your choice:....."))
                                if xx == 1:
                                    hid = input("| HOD ID:.. ")
                                    cursor.execute("SELECT * FROM `db`.`hod` WHERE H_ID='" + hid + "';")
                                    print(cursor.fetchall())
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
                                        hdep = input("| HOD DEPARTMENT:.. ")
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
                                            cursor.execute(
                                                "UPDATE `db`.`hod` SET H_ASSIGNMENT_DEP = '" + hdep + "' WHERE H_ID = '" + hid + "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| HOD ASSIGNED SUCCESSFULLY TO A DEPARTMENT:...|")
                                            cursor.execute("SELECT * FROM `db`.`hod` WHERE H_ID = '" + hid + "';")
                                            print(cursor.fetchall())
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 2:
                                    print(
                                        " __________________________________________________________________________ ")
                                    print(
                                        "|--------------------------------HOD LIST----------------------------------|")
                                    cursor.execute("SELECT * FROM `db`.`hod`")
                                    print(cursor.fetchall())
                                elif xx == 3:
                                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                    for i in range(1, 30000000):
                                        pass
                                    continue
                                else:
                                    print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                    continue
                            elif x == 7:
                                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                for i in range(1, 30000000):
                                    pass
                                continue
                            elif x == 8:
                                print("| LOGGING OUT...PRESS ANY KEY TO CONTINUE..!")
                                a = input("")
                                sys.exit()
                            else:
                                print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                continue
                        elif ch == 6:
                            print("| LOGGING OUT...PRESS ANY KEY TO CONTINUE..!")
                            a = input("")
                            sys.exit()
                        else:
                            print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                            continue
                else:
                    if aa != 3:
                        print("| ERROR:...TRY AGAIN...!")
                        print(3 - aa, "CHANCES LEFT")
                        aa = aa + 1
                    else:
                        print("LIMIT EXCEEDED")
                        aaa = input("PRESS ANY KEY TO EXIT")
                        sys.exit()
        elif x == 2:
            aa = 1
            while aa <= 3:
                print(" __________________________________________________________________________ ")
                print("|------------------------------DOCTOR's LOGIN WINDOW-----------------------|")
                a1 = admin()
                name = input("| USER ID:..")
                pswrd = input("| PASSWORD:..")

                y = a1.doctorlogin(name, pswrd)
                if y == 0:
                    # if(cursor.execute("SELECT ID FROM `db`.`admin` where ID='" + d_id + "' AND Password='" + pswrd + "';") != None):
                    if aa != 3:
                        print("| ERROR:...TRY AGAIN...!")
                        print(3 - aa, "CHANCES LEFT")
                        aa = aa + 1
                    else:
                        print("LIMIT EXCEEDED")
                        aaa = input("PRESS ANY KEY TO EXIT")
                        sys.exit()
                else:
                    cursor.execute("SELECT count(D_DID) FROM `db`.`doctor_professional_details` where D_DID='" + name + "' and D_Type='HOD';");
                    yyy=cursor.fetchone()
                    ppp=int(yyy[0])
                    print(ppp)
                    if (ppp>0):
                        while True:
                            print(" __________________________________________________________________________ ")
                            print("|----------------------------WELCOME TO HOMEPAGE---------------------------|")
                            print("|                                                                          |")
                            print("|                        1. SEE PATIENT ALLOCATED                          |")
                            print("|                        2. EDIT PROFILE                                   |")
                            print("|                        3. VIEW PROFILE                                   |")
                            print("|                        4. REFERRAL                                       |")
                            print("|                        5. HOD TASKS                                      |")
                            print("|                        6. LOGOUT                                         |")
                            print("|__________________________________________________________________________|")
                            x = int(input("Enter your choice:....."))
                            if x == 1:
                                h1.getpatientsallocated(name)
                            elif x == 2:
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
                                xx = int(input("Enter your choice:....."))
                                if xx == 1:
                                    did = input("| DOCTOR ID:.. ")
                                    d1 = dpd()
                                    d1.getdocdetail(did)
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
                                        xxx = int(input("PLEASE CONFIRM..?"))
                                        if xxx == 1:
                                            d1.setdoctorname(nme, did)

                                            print(" ___________________________________ ")
                                            print("| DOCTOR NAME UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 2:
                                    did = input("| DOCTOR ID:.. ")
                                    d1.getdocdetail(did)
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
                                        ageee = input("| DOCTOR AGE:.. ")
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
                                            d1.setdoctorage(ageee, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR AGE UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 3:
                                    did = input("| DOCTOR ID:.. ")
                                    d1.getdocdetail(did)
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
                                        phnu = input("| DOCTOR PHONE NUMBER:.. ")
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
                                            d1.setdoctorpno(phnu, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR PHONE NUMBER UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 4:
                                    did = input("| DOCTOR ID:.. ")
                                    d1.getdocdetail(did)
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
                                            d1.setdoctoremail(emaii, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR EMAIL UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 5:
                                    did = input("| DOCTOR ID:.. ")
                                    d1.getdocdetail(did)
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
                                            d1.setdoctoraddr(addre, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR ADDRESS UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 6:
                                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                    for i in range(1, 30000000):
                                        pass
                                    continue
                                else:
                                    print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                    continue
                            elif x == 3:
                                h1.getdoctordetail(name)
                            elif x == 4:
                                print(" __________________________________________________________________________ ")
                                print("|------------------------DOCTOR'S REFERRAL WINDOW--------------------------|")
                                cursor.execute("SELECT PAT_ID FROM `db`.`doctor_assignment` WHERE DOC_ID='"+name+"';")
                                print(cursor.fetchall())
                                y1=input("ENTER THE PATIENT'S ID TO BE REFFERED:")
                                cursor.execute("SELECT COUNT(PAT_ID) FROM `db`.`doctor_assignment` WHERE PAT_ID='" + y1 + "' AND DOC_ID='" + name + "';")
                                y2=cursor.fetchone()
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
                                        cursor.execute("DELETE FROM `db`.`doctor_assignment` WHERE PAT_ID='"+y1+"';")
                                        db.commit()
                                        sql = "INSERT INTO `db`.`doctor_assignment` (`DOC_ID`, `PAT_ID`, `DOC_MAX_LMT`, `REF_DOC_ID`) VALUES('%s','%s',%s,'%s')"
                                        val = (d2, y1, 20,name)
                                        cursor.execute(sql % val)
                                        db.commit()
                            elif x == 5:
                                print(" __________________________________________________________________________ ")
                                print("|---------------------------HOD'S TASK WINDOW------------------------------|")
                                print("|                                                                          |")
                                print("|                        1. SET DOCTOR'S OPD TIMINGS                       |")
                                print("|                        2. ROOM ALLOTMENT                                 |")
                                print("|                        3. DEPARTMENT CONTACT                             |")
                                print("|                        4. RETURN                                         |")
                                print("|__________________________________________________________________________|")
                                xxxx = int(input("Enter your choice:....."))
                                if xxxx == 1:
                                    print(" __________________________________________________________________________ ")
                                    print("|-----------------------HOD's OPD TIMING UPDATE----------------------------|")
                                    print("|                                                                          |")
                                    print("|                        1. OPD START TIMINGS                              |")
                                    print("|                        2. OPD END TIMINGS                                |")
                                    print("|                        3. RETURN                                         |")
                                    print("|__________________________________________________________________________|")
                                    xxxxx = int(input("Enter your choice:....."))
                                    if xxxxx == 1:
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                        print("|                                                                          |")
                                        print("|                                1. YES                                    |")
                                        print("|                                2. NO                                     |")
                                        print("|__________________________________________________________________________|")
                                        xxxxxx = int(input("Enter your choice:....."))
                                        if xxxxxx==1:
                                            docid=input("| PLEASE ENTER THE DOCTOR's ID WHOSE INFROMATION NEEDS TO BE MODIFIED:...")
                                            opdst=input("| PLEASE ENTER THE START TIME FOR OPD(24 HOUR FORMAT(hh:mm:ss)):...")
                                            cursor.execute("UPDATE `db`.`doctor_professional_details` SET D_OPD_TIME_START = '" + opdst + "' WHERE D_DID = '" + docid + "';")
                                            db.commit()
                                            print("DOCTOR DETAILS UPDATED SUCCESSFULLY")
                                        else:
                                            print("RETURNING BACK...")
                                            break
                                    elif xxxxx == 2:
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                        print("|                                                                          |")
                                        print("|                                1. YES                                    |")
                                        print("|                                2. NO                                     |")
                                        print("|__________________________________________________________________________|")
                                        xxxxxx = int(input("Enter your choice:....."))
                                        if xxxxxx==1:
                                            docid=input("| PLEASE ENTER THE DOCTOR's ID WHOSE INFROMATION NEEDS TO BE MODIFIED:...")
                                            opdent=input("| PLEASE ENTER THE END TIME FOR OPD(24 HOUR FORMAT(hh:mm:ss)):...")
                                            cursor.execute("UPDATE `db`.`doctor_professional_details` SET D_OPD_TIME_END = '" + opdent + "' WHERE D_DID = '" + docid + "';")
                                            db.commit()
                                            print("DOCTOR DETAILS UPDATED SUCCESSFULLY")
                                        else:
                                            print("RETURNING BACK...")
                                            break
                                    elif xxxxx == 3:
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                        print("|                                                                          |")
                                        print("|                                1. YES                                    |")
                                        print("|                                2. NO                                     |")
                                        print("|__________________________________________________________________________|")
                                        xxxxxx = int(input("Enter your choice:....."))
                                        if xxxxxx==1:
                                            docid=input("| PLEASE ENTER THE DOCTOR's ID WHOSE INFROMATION NEEDS TO BE MODIFIED:...")
                                            rno=input("| PLEASE ENTER THE ROOM NUMBER(24 HOUR FORMAT(hh:mm:ss)):...")
                                            cursor.execute("UPDATE `db`.`doctor_professional_details` SET D_RoomNo = '" + rno + "' WHERE D_DID = '" + docid + "';")
                                            db.commit()
                                            print("DOCTOR DETAILS UPDATED SUCCESSFULLY")
                                        else:
                                            print("RETURNING BACK...")
                                            break
                                    else:
                                        break
                            elif x == 6:
                                print("| LOGGING OUT...PRESS ANY KEY TO CONTINUE..!")
                                a = input("")
                                sys.exit()
                            else:
                                print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                continue
                            h1 = h()
                    else:
                        while True:
                            print(" __________________________________________________________________________ ")
                            print("|----------------------------WELCOME TO HOMEPAGE---------------------------|")
                            print("|                                                                          |")
                            print("|                        1. SEE PATIENT ALLOCATED                          |")
                            print("|                        2. EDIT PROFILE                                   |")
                            print("|                        3. VIEW PROFILE                                   |")
                            print("|                        4. REFERRAL                                       |")
                            print("|                        6. LOGOUT                                         |")
                            print("|__________________________________________________________________________|")
                            x = int(input("Enter your choice:....."))
                            if x == 1:
                                h1.getpatientsallocated(name)
                            elif x == 2:
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
                                xx = int(input("Enter your choice:....."))
                                if xx == 1:
                                    did = input("| DOCTOR ID:.. ")
                                    d1 = dpd()
                                    d1.getdocdetail(did)
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
                                        xxx = int(input("PLEASE CONFIRM..?"))
                                        if xxx == 1:
                                            d1.setdoctorname(nme, did)

                                            print(" ___________________________________ ")
                                            print("| DOCTOR NAME UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 2:
                                    did = input("| DOCTOR ID:.. ")
                                    d1.getdocdetail(did)
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
                                        ageee = input("| DOCTOR AGE:.. ")
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
                                            d1.setdoctorage(ageee, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR AGE UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 3:
                                    did = input("| DOCTOR ID:.. ")
                                    d1.getdocdetail(did)
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
                                        phnu = input("| DOCTOR PHONE NUMBER:.. ")
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
                                            d1.setdoctorpno(phnu, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR PHONE NUMBER UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 4:
                                    did = input("| DOCTOR ID:.. ")
                                    d1.getdocdetail(did)
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
                                            d1.setdoctoremail(emaii, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR EMAIL UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 5:
                                    did = input("| DOCTOR ID:.. ")
                                    d1.getdocdetail(did)
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
                                            d1.setdoctoraddr(addre, did)
                                            print(" ___________________________________ ")
                                            print("| DOCTOR ADDRESS UPDATED SUCCESSFULLY:...|")
                                            d1.getdocdetail(did)
                                        elif xxx == 2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx == 2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 6:
                                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                    for i in range(1, 30000000):
                                        pass
                                    continue
                                else:
                                    print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                    continue
                            elif x == 3:
                                h1.getdoctordetail(name)
                            elif x == 4:  ### we have to assign all doctors a level a junior level dr can only reffere someone
                                #### and also other departmental refferal only oh the consent of hod
                                #### refereral if required
                                print(" __________________________________________________________________________ ")
                                print("|------------------------DOCTOR'S REFERRAL WINDOW--------------------------|")
                                cursor.execute(
                                    "SELECT PAT_ID FROM `db`.`doctor_assignment` WHERE DOC_ID='" + name + "';")
                                print(cursor.fetchall())
                                y1 = input("ENTER THE PATIENT'S ID TO BE REFFERED:")
                                cursor.execute(
                                    "SELECT COUNT(PAT_ID) FROM `db`.`doctor_assignment` WHERE PAT_ID='" + y1 + "' AND DOC_ID='" + name + "';")
                                y2 = cursor.fetchone()
                                p2 = y2[0]
                                if (p2 > 0):
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
                                        d2 = input("ENTER THE DOCTOR's ID TO BE REFERRED TO:")
                                        cursor.execute(
                                            "DELETE FROM `db`.`doctor_assignment` WHERE PAT_ID='" + y1 + "';")
                                        db.commit()
                                        sql = "INSERT INTO `db`.`doctor_assignment` (`DOC_ID`, `PAT_ID`, `DOC_MAX_LMT`, `REF_DOC_ID`) VALUES('%s','%s',%s,'%s')"
                                        val = (d2, y1, 20, name)
                                        cursor.execute(sql % val)
                                        db.commit()

                            elif x == 5:
                                print("| LOGGING OUT...PRESS ANY KEY TO CONTINUE..!")
                                a = input("")
                                sys.exit()
                            else:
                                print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                continue
                            h1 = h()
        elif x == 3:
            print(" __________________________________________________________________________ ")
            print("|-----------------------PATIENT'S REGISTRATION WINDOW----------------------|")
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
                cursor.execute("SELECT SUBSTRING(P_ID,3,5) FROM `db`.`patient_details` ORDER BY P_ID DESC LIMIT 1")
                p1 = cursor.fetchone()
                y = str(int(p1[0]) + 1)
                x = 'P_'
                P_ID = x + y
                sql = "INSERT INTO `db`.`patient_details` (P_ID,P_Name,P_Age,P_PNo,P_Add,P_Email) VALUES('%s','%s',%s,%s,'%s','%s')"
                val = (P_ID, name, age, phoneno, adress, email)
                cursor.execute(sql % val)
                db.commit()
                print(" ___________________________________ ")
                print("| PATIENT REGISTRATION COMPLETED:...|")
                print("| USER ID:... ", P_ID)
                print("| PLEASE PROCEED WITH LOGIN WINDOW..")
                sql = "INSERT INTO `db`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
                val = (P_ID, password1, email)
                cursor.execute(sql % val)
                db.commit()
        elif x == 4:
            aa = 1
            while aa <= 3:
                print(" __________________________________________________________________________ ")
                print("|-------------------------PATIENT's LOGIN WINDOW---------------------------|")
                u_id = input("| USERID:.. ")
                password = input("| PASSWORD:.. ")
                cursor.execute(
                    "SELECT count(*) FROM `db`.`admin` where ID='" + u_id + "' AND Password='" + password + "';")
                p1 = cursor.fetchone()
                y = int(p1[0])
                if y == 0:
                    # if(cursor.execute("SELECT ID FROM `db`.`admin` where ID='" + d_id + "' AND Password='" + pswrd + "';") != None):
                    if aa != 3:
                        print("| ERROR:...TRY AGAIN...!")
                        print(3 - aa, "CHANCES LEFT")
                        aa = aa + 1
                    else:
                        print("LIMIT EXCEEDED")
                        aaa = input("PRESS ANY KEY TO EXIT")
                        sys.exit()
                else:
                    while True:
                        h1 = h()
                        print(" __________________________________________________________________________ ")
                        print("|----------------------------WELCOME TO HOSPITAL---------------------------|")
                        print("|                                                                          |")
                        print("|                            1. SEARCH DOCTOR                              |")  #### ON THE BASIS OF DEPARTMENT OR DOCTOR NAME ## INSIDE OOF DEPARTMENT 10 DOCTOR AYE
                        print("|                            2. VIEW DOCTOR'S OPD TIMING                   |")
                        print("|                            3. VIEW DOCTOR'S PROFILE                      |")
                        print("|                            4. VIEW PAST HISTORY                          |")
                        print("|                            5. VIEW PROFILE                               |")
                        print("|                            6. NEW APPOINTMENT                            |")
                        print("|                            7. EDIT PROFILE                               |")
                        print("|                            8. EXIT                                       |")
                        print("|__________________________________________________________________________|")
                        x = int(input("Enter your choice:"))
                        if x == 1:
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
                                    ##### random exception handling sholud be used
                                    y = input("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                                    ######### apointment table should be used
                                    ##### also check for availability of doctors
                                    ## count for no of patients assigned to any doctor if no is greator thasn 20 than
                                    ##an appoint is not possible
                                    print("Are you want a specific department or general appointment")
                                    print("1. Enter Department")
                                    print("2. general patient")
                                    ch = input("enter your choice:..........")
                                    if ch == 1:
                                        h1.getdepartments()
                                        dep = input("enter the department from the given department:")
                                        h1.getappointment(dep, u_id)
                                        print("please wait when  appointment  finalised")
                                        i = 1000000
                                        while (i >= 0):
                                            i = i - 1
                                        print("your appoinmnet has been fixed ")
                                        print("your id and details are:")


                                    elif ch == 2:
                                        dep = 'General'
                                        h1.getappointment(dep, u_id)
                                        print("please wait when  appointmnet  finalised")
                                        i = 1000000
                                        while (i >= 0):
                                            i = i - 1
                                        print("your appoinmnet has been fixed ")
                                        print("your id and details are:")
                                    else:
                                        print("wrong choice")
                                        continue
                                    pass
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
                                    h1.getappointmentid(y, u_id)
                                else:
                                    pass
                                print("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                            elif x == 3:
                                print("| LIST OF DEPARTMENTS:...")
                                cursor.execute("SELECT Dep_Name FROM db.department")
                                print(cursor.fetchall())
                                cha = input("| ENTER THE DEPARTMENT TO BE SEARCHED:... ")
                                print("| DOCTOR'S LIST:... ")
                                cursor.execute("SELECT * FROM db.doctor_details WHERE D_ID IN (SELECT D_DID FROM db.doctor_professional_details WHERE D_Department ='" + cha + "');")
                                print(cursor.fetchall())
                            else:
                                return False
                        elif x == 2:
                            print(" __________________________________________________________________________ ")
                            print("|-------------------DOCTOR'S OPD TIMING SEARCH WINDOW----------------------|")
                            print("|                                                                          |")
                            d_id = input("| PLEASE ENTER THE DOCTOR'S ID:... ")
                            h1.gettiming(d_id)
                        elif x == 3:
                            print(" __________________________________________________________________________ ")
                            print("|--------------------DOCTOR'S PROFILE SEARCH WINDOW------------------------|")
                            print("|                                                                          |")
                            d_id = input("| PLEASE ENTER THE DOCTOR'S ID:... ")
                            h1.getdoctordetail(d_id)
                        elif x == 4:
                            print(" __________________________________________________________________________ ")
                            print("|----------------------------PAST HISTORY----------------------------------|")
                            print("|                                                                          |")
                            h1.getpateinthistory(u_id)
                        elif x == 5:
                            print(" __________________________________________________________________________ ")
                            print("|----------------------------SELF PROFILE----------------------------------|")
                            print("|                                                                          |")
                            p1 = p()
                            p1.getpatientall(u_id)
                        elif x == 6:
                            print(" __________________________________________________________________________ ")
                            print("|-------------------PATIENT'S APPOINTMENT BOOKING WINDOW-------------------|")
                            print("|                            1. AUTOMATIC APPOINTMENT                      |")
                            print("|                            2. MANUAL APPOINTMENT                         |")
                            print("|                            3. EXIT                                       |")
                            print("|__________________________________________________________________________|")
                            inn=int(input("| PLEASE MAKE A SELECTION:..."))
                            if inn==1:
                                cursor.execute("SELECT DISTINCT Dep_sym FROM `db`.`department`")
                                print(cursor.fetchall())
                                ch = input("| ENTER THE DEPARTMENT FOR WHICH APPOINTMENT IS NEEDED:... ")
                                if(int(cursor.execute("SELECT Dep_sym FROM `db`.`department` where D_Name LIKE ('%'" + ch + "'%');"))==1):
                                    sql = "INSERT INTO `db`.`unassigned_patient` (`UP_ID`, `UP_PROB_DEP`, `UP_E_TYPE`)VALUES('%s','%s','%s')"
                                    val = (u_id,ch,"")
                                    cursor.execute(sql % val)
                                    db.commit()
                                else:
                                    print("WRONG SELECTION..PLEASE ENTER THE CORRECT DEPARTMENT")
                                    continue
                            elif inn==2:
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
                                        ##### random exception handling sholud be used
                                        y = input("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                                        ######### apointment table should be used
                                        ##### also check for availability of doctors
                                        ## count for no of patients assigned to any doctor if no is greator thasn 20 than
                                        ##an appoint is not possible
                                        print("Are you want a specific department or general appointment")
                                        print("1. Enter Department")
                                        print("2. general pateint")
                                        ch = input("enter your choice:..........")
                                        if ch == 1:
                                            h1.getdepartments()
                                            dep = input("enter the department from the given department:")
                                            h1.getappointment(dep, u_id)
                                            print("please wait when  appointmnet  finalised")
                                            i = 1000000
                                            while (i >= 0):
                                                i = i - 1
                                            print("your appoinmnet has been fixed ")
                                            print("your id and details are:")


                                        elif ch == 2:
                                            dep = 'General'
                                            h1.getappointment(dep, u_id)
                                            print("please wait when  appointmnet  finalised")
                                            i = 1000000
                                            while (i >= 0):
                                                i = i - 1
                                            print("your appoinmnet has been fixed ")
                                            print("your id and details are:")
                                        else:
                                            print("wrong choice")
                                            continue
                                        pass
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
                                        h1.getappointmentid(y, u_id)
                                    else:
                                        pass
                                    print("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                                elif x == 3:
                                    ch = input("| ENTER THE DEPARTMENT TO BE SEARCHED:... ")
                                    print("| DOCTOR'S LIST:... ")
                                    # cursor.execute("SELECT * FROM `db`.`doctor_details` where D_Name = '" + ch + "';")
                                    # print(cursor.fetchall())
                                    # print("| 1. WANT TO MAKE AN APPOINTMENT:...")
                                    # print("| 2. RETURN TO PREVIOUS WINDOW:... ")
                                    # x = int(input("| PLEASE MAKE A SELECTION:... "))
                                    # if x == 1:
                                    #     ##### random exception handling sholud be used
                                    #     y = input("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                                    #     ######### apointment table should be used
                                    #     pass
                                    # else:
                                    #     pass
                                    # print("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                                else:
                                    return False
                            elif inn==3:
                                break
                        elif x == 7:
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
                            p2 = p()
                            p2.getpatientall(y)
                            if x == 1:
                                ######### name ########
                                print("| 1. Confirm")
                                print("| 2. RETURN TO PREVIOUS WINDOW:... ")
                                choice = int(input("| ENTER YOUR CHOICE:..."))
                                if choice == 1:
                                    paswrd = input("enter your password please")

                                    if paswrd == p2.getpatientpswrd(y):
                                        name = input("enter name to be changed")
                                        p2.setpateintname(name, y)
                                        print("pleas wait .............")
                                        i = 1000000
                                        while i >= 0:
                                            i = i - 1
                                        print("your name has been changed")
                                        p2.getpatientall(y)
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

                                    if paswrd == p2.getpatientpswrd(y):
                                        email = input("enter email to be changed")
                                        p2.setpatientemail(email, y)
                                        print("pleas wait .............")
                                        i = 1000000
                                        while i >= 0:
                                            i = i - 1
                                        print("your email has been changed")
                                        p2.getpatientall(y)
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

                                    if paswrd == p2.getpatientpswrd(y):
                                        addr = input("enter address to be changed")
                                        p2.setpatientaddress(addr, y)
                                        print("pleas wait .............")
                                        i = 1000000
                                        while i >= 0:
                                            i = i - 1
                                        print("your email has been changed")
                                        p2.getpatientall(y)
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

                                    if paswrd == p2.getpatientpswrd(y):
                                        phno = input("enter address to be changed")
                                        p2.setpatientphone(phno, y)
                                        print("pleas wait .............")
                                        i = 1000000
                                        while i >= 0:
                                            i = i - 1
                                        print("your email has been changed")
                                        p2.getpatientall(y)
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

                                    if paswrd == p2.getpatientpswrd(y):
                                        age = input("enter age to be changed")
                                        p2.setpatientaddress(age, y)
                                        print("pleas wait .............")
                                        i = 1000000
                                        while i >= 0:
                                            i = i - 1
                                        print("your age has been updated")
                                        p2.getpatientall(y)
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
                                input("PRESS ANY KEY TO CONTINUE:..")
                                break
                        elif x == 8:
                            print("| LOGGING OUT...PRESS ANY KEY TO CONTINUE..!")
                            a = input("")
                            sys.exit()
                        else:
                            print("WRONG CHOICE...TRY AGAIN")
                            continue
        elif x == 5:
            print(" __________________________________________________________________________ ")
            print("|----------------------------PASSWORD RESET PAGE---------------------------|")
            print("| 1. FORGOT ID                                                             |")
            print("| 2. FORGOT PASSWORD                                                             |")
            choice = int(input("Please enyer your choice:......."))
            p1 = p()
            if choice == 1:
                pno = input("Please enter a phone no associated with your account:...")

                print("YOUR ID IS GIVEN BELOW. USE THIS TO RESER YOUR PASSWORD")
                print(p1.getidpno(pno))
            elif choice == 2:
                print("Please enter you id:....")
                x1 = input()
                print("Are you sure you want to reset your password")
                print("1. CONFIRM")
                print("2. RETURN BACK")
                ch = int(input("your choice::...."))
                if ch == 1:
                    pswrd1 = input("please enter your password....")
                    pswrd2 = input("please enter your password again....")
                    if (pswrd1 == pswrd2):
                        print("please wait while updating...............")

                        p1.setpassword(pswrd1, x1)
                        i = 100000000
                        while i >= 0:
                            i = i - 1

                        print(" your password has changed ")
                        print(" please move forward with login ")
                    else:
                        print("PASSWORDS DONOT MATCH")
                        print("PLEASE TRY AGAIN")
            else:
                print("wrong choice")
                pass
        elif x == 6:
            print(" __________________________________________________________________________ ")
            print("|--------------------PATIENT'S EMERGENCY REGISTRATION----------------------|")
            name = input("| NAME:.. ")
            types = input("| TYPE:.. ")
            age = input("| AGE:..")
            em = input("| EMAIL ID:..")
            cursor.execute("SELECT SUBSTRING(P_ID,3,5) FROM `db`.`patient_details` ORDER BY P_ID DESC LIMIT 1")
            p1 = cursor.fetchone()
            y = str(int(p1[0]) + 1)
            x = 'P_'
            E_ID = x + y
            sql = "INSERT INTO `db`.`patient_details` (P_ID,P_Name,P_AGE,P_EMAIL) VALUES('%s','%s',%s,'%s')"
            val = (E_ID, name, age, em)
            cursor.execute(sql % val)
            db.commit()
            psw = 'xyz'
            sql = "INSERT INTO `db`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
            val = (E_ID, psw, em)
            cursor.execute(sql % val)
            db.commit()
            print("| PATIENT ID:...", E_ID)
            print("| PATIENT PASSWORD:...", psw)
            print("| PLEASE KEEP A NOTE FOR FURTHER REFERENCE")
            sql = "INSERT INTO `db`.`patient_assignment` (E_NAME,E_ID,E_TYPE,E_AGE) VALUES('%s','%s','%s',%s)"
            val = (name, E_ID, types, age)
            cursor.execute(sql % val)
            db.commit()
            print("| PATIENT'S DETAILS SAVED SUCCESSFULLY")
            cursor.execute("SELECT * FROM `db`.`patient_assignment` WHERE E_ID='" + E_ID + "';")
            print(cursor.fetchall())
            inpu = input("| PRESS ANY KEY TO CONTINUE")
            print("PLEASE WAIT....EXITING")
            for i in range(1, 30000000):
                pass
        elif x == 7:
            sys.exit()
    else:
        print("| ERROR:... ")


if __name__ == "__main__":
    main()

db.close()