import sys
from patient import patient as p
from patientmedicalreport import *
from admin import *
from doctorpersonaldetails import *
from doctorproffessionaldetails import *
import pymysql

db= pymysql.connect(
    host='127.0.0.1',
    user="root",
    passwd="up32ee9964",
    db="oopd"
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
                        if ch == 1:
                            cursor.execute("select * from oopd.doctor_details")
                            for x in cursor:
                                print(x)
                        elif ch == 2:
                            cursor.execute("select * from oopd.patient_details")
                            for x in cursor:
                                print(x)
                        elif ch == 3:
                            pass
                        elif ch == 4:
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
                                cursor.execute(
                                    "SELECT SUBSTRING(D_ID,3,5) FROM `oopd`.`doctor_details` ORDER BY D_ID DESC LIMIT 1")
                                p1 = cursor.fetchone()
                                y = str(int(p1[0]) + 1)
                                x = 'D_'
                                D_ID = x + y
                                sql = "INSERT INTO `oopd`.`doctor_details` (D_ID,D_Name,D_Age,D_PNo,D_Add,D_Email) VALUES('%s','%s',%s,%s,'%s','%s')"
                                val = (D_ID, name, age, phoneno, adress, email)
                                cursor.execute(sql % val)
                                db.commit()
                                print(" ___________________________________ ")
                                print("| DOCTOR DETAILS ADDED SUCCESSFULLY:...|")
                                print("| USER ID:... ", D_ID)
                                sql = "INSERT INTO `oopd`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
                                val = (D_ID, password1, email)
                                cursor.execute(sql % val)
                                db.commit()
                        elif ch == 5:
                            print(" __________________________________________________________________________ ")
                            print("|-------------------------DATABASE MANAGEMENT WINDOW-----------------------|")
                            print("|                                                                          |")
                            print("|                        1. PATIENT'S PERSONAL DETAILS                     |")
                            print("|                        2. PATIENT'S MEDICAL HISTORY                      |")
                            print("|                        3. DOCTOR'S PERSONAL DETAILS                      |")
                            print("|                        4. DOCTOR'S PROFESSIONAL DETAILS                  |")
                            print("|                        5. HOD MANAGEMENT                                 |")
                            print("|                        6. AUTOMATIC PATIENT ASSIGNMENT                   |")
                            print("|                        7. DOCTOR'S REFERRAL MANAGEMENT                   |")
                            print("|                        8. RETURN TO PREVIOUS PAGE                        |")
                            print("|                        9. LOGOUT                                         |")
                            print("|__________________________________________________________________________|")
                            x = int(input("Enter your choice:....."))
                            if x==1:
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
                                    cursor.execute("SELECT * FROM `oopd`.`patient_details` WHERE P_ID='" +pid+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                        1. YES                                            |")
                                    print("|                        2. NO                                             |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        nm = input("| PATIENT NAME:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                        1. YES                                            |")
                                        print("|                        2. NO                                             |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`patient_details` SET P_Name = '" +nm+ "' WHERE P_ID = '" +pid+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| PATIENT NAME UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`patient_details` WHERE `P_ID` = '" +pid+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 2:
                                    pid = input("| PATIENT ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`patient_details` WHERE P_ID='" +pid+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                        1. YES                                            |")
                                    print("|                        2. NO                                             |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        agee = input("| PATIENT AGE:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                        1. YES                                            |")
                                        print("|                        2. NO                                             |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`patient_details` SET P_Age = '" +agee+ "' WHERE P_ID = '" +pid+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| PATIENT AGE UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`patient_details` WHERE `P_ID` = '" +pid+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 3:
                                    pid = input("| PATIENT ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`patient_details` WHERE P_ID='" +pid+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                        1. YES                                            |")
                                    print("|                        2. NO                                             |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        phno = input("| PATIENT PHONE NUMBER:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                        1. YES                                            |")
                                        print("|                        2. NO                                             |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`patient_details` SET P_PNo = '" +phno+ "' WHERE P_ID = '" +pid+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| PATIENT PHONE NUMBER UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`patient_details` WHERE `P_ID` = '" +pid+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 4:
                                    pid = input("| PATIENT ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`patient_details` WHERE P_ID='" +pid+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                        1. YES                                            |")
                                    print("|                        2. NO                                             |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        emai = input("| PATIENT EMAIL:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                        1. YES                                            |")
                                        print("|                        2. NO                                             |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`patient_details` SET P_Email = '" +emai+ "' WHERE P_ID = '" +pid+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| PATIENT EMAIL UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`patient_details` WHERE `P_ID` = '" +pid+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 5:
                                    pid = input("| PATIENT ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`patient_details` WHERE P_ID='" +pid+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                        1. YES                                            |")
                                    print("|                        2. NO                                             |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        addr = input("| PATIENT ADDRESS:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                        1. YES                                            |")
                                        print("|                        2. NO                                             |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`patient_details` SET P_PNo = '" +addr+ "' WHERE P_ID = '" +pid+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| PATIENT ADDRESS UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`patient_details` WHERE `P_ID` = '" +pid+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
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
                            elif x==2:
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
                            elif x==3:
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
                                    cursor.execute("SELECT * FROM `oopd`.`doctor_details` WHERE D_ID='" +did+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                1. YES                                    |")
                                    print("|                                2. NO                                     |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        nme = input("| DOCTOR NAME:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                               1. YES                                     |")
                                        print("|                               2. NO                                      |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`doctor_details` SET D_Name = '" +nme+ "' WHERE D_ID = '" +did+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| DOCTOR NAME UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`doctor_details` WHERE `D_ID` = '" +did+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 2:
                                    did = input("| DOCTOR ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`doctor_details` WHERE D_ID='" +did+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                1. YES                                    |")
                                    print("|                                2. NO                                     |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        ageee = input("| DOCTOR AGE:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                              1. YES                                      |")
                                        print("|                              2. NO                                       |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`doctor_details` SET D_Age = '" +ageee+ "' WHERE D_ID = '" +did+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| DOCTOR AGE UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`doctor_details` WHERE `D_ID` = '" +did+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 3:
                                    did = input("| DOCTOR ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`doctor_details` WHERE D_ID='" +did+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                 1. YES                                   |")
                                    print("|                                 2. NO                                    |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        phnu = input("| DOCTOR PHONE NUMBER:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                              1. YES                                      |")
                                        print("|                              2. NO                                       |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`patient_details` SET D_PNo = '" +phnu+ "' WHERE D_ID = '" +did+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| DOCTOR PHONE NUMBER UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`doctor_details` WHERE `D_ID` = '" +did+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 4:
                                    did = input("| DOCTOR ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`doctor_details` WHERE D_ID='" +did+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                 1. YES                                   |")
                                    print("|                                 2. NO                                     |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        emaii = input("| DOCTOR EMAIL:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                              1. YES                                      |")
                                        print("|                              2. NO                                       |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`doctor_details` SET D_Email = '" +emaii+ "' WHERE D_ID = '" +did+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| DOCTOR EMAIL UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`doctor_details` WHERE `D_ID` = '" +did+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 5:
                                    did = input("| DOCTOR ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`doctor_details` WHERE D_ID='" +did+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                 1. YES                                   |")
                                    print("|                                 2. NO                                     |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        addre = input("| DOCTOR ADDRESS:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                              1. YES                                      |")
                                        print("|                              2. NO                                       |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`doctor_details` SET D_PNo = '" +addre+ "' WHERE D_ID = '" +did+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| DOCTOR ADDRESS UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`doctor_details` WHERE `D_ID` = '" +did+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
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
                            elif x==4:
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
                                    cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE D_ID='" +did+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                1. YES                                    |")
                                    print("|                                2. NO                                     |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        dep = input("| DOCTOR DEPARTMENT:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                               1. YES                                     |")
                                        print("|                               2. NO                                      |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`doctor_professional_details` SET D_Department = '" +dep+ "' WHERE D_ID = '" +did+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| DOCTOR DEPARTMENT UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE `D_ID` = '" +did+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 2:
                                    did = input("| DOCTOR ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE D_ID='" +did+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                1. YES                                    |")
                                    print("|                                2. NO                                     |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        opdst = input("| DOCTOR OPD START TIME:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                              1. YES                                      |")
                                        print("|                              2. NO                                       |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`doctor_professional_details` SET D_OPD_TIME_START = '" +opdst+ "' WHERE D_ID = '" +did+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| DOCTOR OPD START TIME UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE `D_ID` = '" +did+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 3:
                                    did = input("| DOCTOR ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE D_ID='" +did+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                 1. YES                                   |")
                                    print("|                                 2. NO                                    |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        opden = input("| DOCTOR OPD END TIME:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                              1. YES                                      |")
                                        print("|                              2. NO                                       |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`patient_details` SET D_OPD_TIME_END = '" +opden+ "' WHERE D_ID = '" +did+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| DOCTOR OPD END TIME UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE `D_ID` = '" +did+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 4:
                                    did = input("| DOCTOR ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE D_ID='" +did+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                 1. YES                                   |")
                                    print("|                                 2. NO                                     |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        dtyp = input("| DOCTOR TYPE:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                              1. YES                                      |")
                                        print("|                              2. NO                                       |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`doctor_professional_details` SET D_Type = '" +dtyp+ "' WHERE D_ID = '" +did+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| DOCTOR TYPE UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE `D_ID` = '" +did+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 5:
                                    did = input("| DOCTOR ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE D_ID='" +did+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                 1. YES                                   |")
                                    print("|                                 2. NO                                     |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        spec = input("| DOCTOR SPECIALIZATION:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                              1. YES                                      |")
                                        print("|                              2. NO                                       |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`doctor_professional_details` SET D_Specialization = '" +spec+ "' WHERE D_ID = '" +did+ "';")
                                            oopd.commit()
                                            print(" ___________________________________ ")
                                            print("| DOCTOR SPECIALIZATION UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE `D_ID` = '" +did+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 6:
                                    did = input("| DOCTOR ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE D_ID='" +did+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                 1. YES                                   |")
                                    print("|                                 2. NO                                     |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        extno = input("| DOCTOR EXTENSION NUMBER:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                              1. YES                                      |")
                                        print("|                              2. NO                                       |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`doctor_professional_details` SET D_ExtensionNo = '" +extno+ "' WHERE D_ID = '" +did+ "';")
                                            oopd.commit()
                                            print(" ___________________________________ ")
                                            print("| DOCTOR EXTENSION NUMBER UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE `D_ID` = '" +did+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 7:
                                    did = input("| DOCTOR ID:.. ")
                                    cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE D_ID='" +did+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                 1. YES                                   |")
                                    print("|                                 2. NO                                     |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        rmno = input("| DOCTOR ROOM NUMBER:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                              1. YES                                      |")
                                        print("|                              2. NO                                       |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`doctor_professional_details` SET D_RoomNo = '" +rmno+ "' WHERE D_ID = '" +did+ "';")
                                            db.commit()
                                            print(" ___________________________________ ")
                                            print("| DOCTOR ROOM NUMBER UPDATED SUCCESSFULLY:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`doctor_professional_details` WHERE `D_ID` = '" +did+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
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
                            elif x==5:
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
                                    cursor.execute("SELECT * FROM `oopd`.`hod` WHERE H_ID='" +hid+ "';")
                                    print(cursor.fetchall())
                                    print(" __________________________________________________________________________ ")
                                    print("|------------------------IS THE INFORMATION CORRECT------------------------|")
                                    print("|                                                                          |")
                                    print("|                                1. YES                                    |")
                                    print("|                                2. NO                                     |")
                                    print("|__________________________________________________________________________|")
                                    xxx=int(input("PLEASE SELECT THE OPTION:..."))
                                    if xxx==1:
                                        hdep = input("| HOD DEPARTMENT:.. ")
                                        print(" __________________________________________________________________________ ")
                                        print("|------------------------------CONFIRM-------------------------------------|")
                                        print("|                                                                          |")
                                        print("|                               1. YES                                     |")
                                        print("|                               2. NO                                      |")
                                        print("|__________________________________________________________________________|")
                                        xxx=int(input("PLEASE CONFIRM..?"))
                                        if xxx==1:
                                            cursor.execute("UPDATE `oopd`.`hod` SET H_ASSIGNMENT_DEP = '" +hdep+ "' WHERE H_ID = '" +hid+ "';")
                                            oopd.commit()
                                            print(" ___________________________________ ")
                                            print("| HOD ASSIGNED SUCCESSFULLY TO A DEPARTMENT:...|")
                                            cursor.execute("SELECT * FROM `oopd`.`hod` WHERE H_ID = '" +hid+ "';")
                                            print(cursor.fetchall())
                                        elif xxx==2:
                                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                            for i in range(1, 30000000):
                                                pass
                                            continue
                                        else:
                                            print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                                            continue
                                    elif xx==2:
                                        print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                        for i in range(1, 30000000):
                                            pass
                                        continue
                                elif xx == 2:
                                    print(" __________________________________________________________________________ ")
                                    print("|--------------------------------HOD LIST----------------------------------|")
                                    cursor.execute("SELECT * FROM `oopd`.`hod`")
                                    print(cursor.fetchall())
                                elif xx == 3:
                                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                    for i in range(1, 30000000):
                                        pass
                                    continue
                                else:
                                    print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                    continue
                            elif x==6:
                                pass
                            elif x==7:
                                pass
                            elif x==8:
                                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                for i in range(1,30000000):
                                    pass
                                continue
                            elif x==9:
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
                    if aa!=3:
                        print("| ERROR:...TRY AGAIN...!")
                        print(3 - aa, "CHANCES LEFT")
                        aa = aa + 1
                    else:
                        print("LIMIT EXCEEDED")
                        aaa=input("PRESS ANY KEY TO EXIT")
                        sys.exit()
        elif x == 2:
            aa = 1
            while aa <= 3:
                print(" __________________________________________________________________________ ")
                print("|------------------------------DOCTOR's LOGIN WINDOW-----------------------|")
                name = input("| USER ID:..")
                pswrd = input("| PASSWORD:..")
                cursor.execute("SELECT count(*) FROM `oopd`.`admin` where ID='" + name + "' AND Password='" + pswrd + "';")
                p1 = cursor.fetchone()
                y = int(p1[0])
                if y==0:
                # if(cursor.execute("SELECT ID FROM `oopd`.`admin` where ID='" + d_id + "' AND Password='" + pswrd + "';") != None):
                    if aa!=3:
                        print("| ERROR:...TRY AGAIN...!")
                        print(3 - aa, "CHANCES LEFT")
                        aa = aa + 1
                    else:
                        print("LIMIT EXCEEDED")
                        aaa = input("PRESS ANY KEY TO EXIT")
                        sys.exit()
                else:
                    while True:
                    ##############  Doctor functionality
                        print(" __________________________________________________________________________ ")
                        print("|----------------------------WELCOME TO HOMEPAGE---------------------------|")
                        print("|                                                                          |")
                        print("|                        1. SEE PATIENT ALLOCATED                          |")
                        print("|                        2. EDIT PROFILE                                   |")
                        print("|                        3. SORT PATIENT LIST                              |")
                        print("|                        4. LEAVE MANAGEMENT                               |")
                        print("|                        5. VIEW PROFILE                                   |")
                        print("|                        6. REFERRAL                                       |")
                        print("|                        7. LOGOUT                                         |")
                        print("|__________________________________________________________________________|")
                        x = int(input("Enter your choice:....."))
                        if x == 1:
                            ###  view list of pateints allocated to him
                            pass
                            print()
                        elif x == 2:
                            diid = input("| D_ID:.. ")
                            #cursor.execute("SELECT * FROM `oopd`.`doctor_details` WHERE D_ID = '" +diid+ "';")
                            name=input("|NAME:..")
                            age=input("|AGE:..")
                            phone=input("|PHONE:..")
                            email=input("|EMAIL:..")
                            address=input("|ADDR:..")
                            cursor.execute("UPDATE `oopd`.`doctor_details` SET D_Name = '" +name+ "',D_PNo='"+phone+"',D_Add='"+address+"',D_Age='"+age+"',D_Email='"+email+"'   WHERE D_ID = '" +diid+ "';") 
                            db.commit()
                            #### edit doctor profile
                            pass
                        elif x == 3:

                            ### sort of pateint depending upon department, id
                            pass
                        elif x == 4:
                            #### leave of doctors
                            pass
                        elif x == 5:
                             diid = input("| D_ID:.. ")
                             cursor.execute("SELECT * FROM `oopd`.`doctor_details` WHERE D_ID = '" +diid+ "';")
                             print(cursor.fetchall())
                            
                            ######  view profile
                            
                        elif x == 6:
                            #### refereral if required
                            pass
                        elif x == 7:
                            print("| LOGGING OUT...PRESS ANY KEY TO CONTINUE..!")
                            a = input("")
                            sys.exit()
                        else:
                            print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                            continue
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
                cursor.execute("SELECT SUBSTRING(P_ID,3,5) FROM `oopd`.`patient_details` ORDER BY P_ID DESC LIMIT 1")
                p1 = cursor.fetchone()
                y = str(int(p1[0]) + 1)
                x = 'P_'
                P_ID = x + y
                sql = "INSERT INTO `oopd`.`patient_details` (P_ID,P_Name,P_Age,P_PNo,P_Add,P_Email) VALUES('%s','%s',%s,%s,'%s','%s')"
                val = (P_ID, name, age, phoneno, adress, email)
                cursor.execute(sql % val)
                db.commit()
                print(" ___________________________________ ")
                print("| PATIENT REGISTRATION COMPLETED:...|")
                print("| USER ID:... ", P_ID)
                print("| PLEASE PROCEED WITH LOGIN WINDOW..")
                sql = "INSERT INTO `oopd`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
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
                    "SELECT count(*) FROM `oopd`.`admin` where ID='" + u_id + "' AND Password='" + password + "';")
                p1 = cursor.fetchone()
                y = int(p1[0])
                if y == 0:
                    # if(cursor.execute("SELECT ID FROM `oopd`.`admin` where ID='" + d_id + "' AND Password='" + pswrd + "';") != None):
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
                        print(" __________________________________________________________________________ ")
                        print("|----------------------------WELCOME TO HOMEPAGE---------------------------|")
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
                            print(
                                "|                           2. SEARCH BY DOCTOR'S ID                       |")  #### WRITE LOGIC FOR EACH AND EVERY ONE
                            print(
                                "|                           3. SEARCH BY DEPARTMENT                        |")  #### show available departments
                            print("|                           4. EXIT                                        |")
                            print("|__________________________________________________________________________|")
                            x = int(input("| ENTER YOUR CHOICE:..."))
                            if x == 1:
                                print(" __________________________________________________________________________ ")
                                print("|-----------------------------SEARCH WINDOW--------------------------------|")
                                print("|                                                                          |")
                                ch = input("| ENTER THE DOCTOR'S NAME TO BE SEARCHED:... ")
                                print("| DOCTOR'S LIST")
                                cursor.execute("SELECT * FROM `oopd`.`doctor_details` where D_Name = '" + ch + "';")
                                print(cursor.fetchall())
                                print("| 1. WANT TO MAKE AN APPOINTMENT:...")
                                print("| 2. RETURN TO PREVIOUS WINDOW:... ")
                                x = int(input("| PLEASE MAKE A SELECTION:... "))
                                if x == 1:
                                    ##### random exception handling sholud be used
                                    y = input("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                                    ######### apointment table should be used
                                    pass
                                else:
                                    pass
                            elif x == 2:
                                ch = input("| ENTER THE DEPARTMENT TO BE SEARCHED:... ")
                                print("| DOCTOR'S LIST:... ")
                                cursor.execute("SELECT * FROM `oopd`.`doctor_details` where D_ID = '" + ch + "';")
                                print(cursor.fetchall())
                                print("| 1. WANT TO MAKE AN APPOINTMENT:...")
                                print("| 2. RETURN TO PREVIOUS WINDOW:... ")
                                x = int(input("| PLEASE MAKE A SELECTION:... "))
                                if x == 1:
                                    ##### random exception handling sholud be used
                                    y = input("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                                    ######### apointment table should be used
                                    pass
                                else:
                                    pass
                                print("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                            elif x == 3:
                                ch = input("| ENTER THE DEPARTMENT TO BE SEARCHED:... ")
                                print("| DOCTOR'S LIST:... ")
                                # cursor.execute("SELECT * FROM `oopd`.`doctor_details` where D_Name = '" + ch + "';")
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
                        elif x == 2:
                            print(" __________________________________________________________________________ ")
                            print("|-------------------DOCTOR'S OPD TIMING SEARCH WINDOW----------------------|")
                            print("|                                                                          |")
                            ##### search doctor id and show to pateint
                            ### pateint can able to selct the coctor also
                            d_id = input("| PLEASE ENTER THE DOCTOR'S ID:... ")
                        elif x == 3:
                            print(" __________________________________________________________________________ ")
                            print("|--------------------DOCTOR'S PROFILE SEARCH WINDOW------------------------|")
                            print("|                                                                          |")
                            #### show doctor profile to pateint
                            d_id = input("| PLEASE ENTER THE DOCTOR'S ID:... ")
                            pass
                        elif x == 4:
                            print(" __________________________________________________________________________ ")
                            print("|----------------------------PAST HISTORY----------------------------------|")
                            print("|                                                                          |")
                            #### show pateint his history
                            pass
                        elif x == 5:
                            print(" __________________________________________________________________________ ")
                            print("|----------------------------SELF PROFILE----------------------------------|")
                            print("|                                                                          |")
                            #### pateints profile
                            pass
                        elif x == 6:
                            print(" __________________________________________________________________________ ")
                            print("|---------------------------NEW APPOINTMENT--------------------------------|")
                            print("|                                                                          |")

                            ### assignment automatic
                            pass
                        elif x == 7:
                            print(" __________________________________________________________________________ ")
                            print("|----------------------------EDIT PROFILE----------------------------------|")
                            print("|                                                                          |")
                            print("|                            1. MANUAL APPOINTMENT:                        |")
                            print("|                            2. AUTOMATIC APPOINTMENT:                     |")
                            print("|                            3. RETURN TO PREVIOUS PAGE:                   |")
                            print("|__________________________________________________________________________|")
                            ### edit pateints id
                            x = int(input("| ENTER YOUR CHOICE:..."))
                            if x == 1:
                                pass
                            elif x == 2:
                                pass
                            elif x == 3:
                                break
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
            print("|                                                                          |")
            #### forgot password
            pass
        elif x == 6:
            print(" __________________________________________________________________________ ")
            print("|--------------------PATIENT'S EMERGENCY REGISTRATION----------------------|")
            name = input("| NAME:.. ")
            types = input("| TYPE:.. ")
            age = input("| AGE:..")
            em = input("| EMAIL ID:..")
            cursor.execute("SELECT SUBSTRING(P_ID,3,5) FROM `oopd`.`patient_details` ORDER BY P_ID DESC LIMIT 1")
            p1 = cursor.fetchone()
            y = str(int(p1[0]) + 1)
            x = 'P_'
            E_ID = x + y
            sql = "INSERT INTO `oopd`.`patient_details` (P_ID,P_Name,P_AGE,P_EMAIL) VALUES('%s','%s',%s,'%s')"
            val = (E_ID, name, age, em)
            cursor.execute(sql % val)
            db.commit()
            psw='xyz'
            sql = "INSERT INTO `oopd`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
            val = (E_ID, psw, em)
            cursor.execute(sql % val)
            db.commit()
            print("| PATIENT ID:...",E_ID)
            print("| PATIENT PASSWORD:...", psw)
            print("| PLEASE KEEP A NOTE FOR FURTHER REFERENCE")
            sql = "INSERT INTO `oopd`.`patient_assignment` (E_NAME,E_ID,E_TYPE,E_AGE) VALUEs('%s','%s','%s',%s)"
            val = (name, E_ID, types, age)
            cursor.execute(sql % val)
            db.commit()
            print("| PATIENT'S DETAILS SAVED SUCCESSFULLY")
            cursor.execute("SELECT * FROM `oopd`.`patient_assignment` WHERE E_ID='" + E_ID + "';")
            print(cursor.fetchall())
            inpu=input("| PRESS ANY KEY TO CONTINUE")
            print("PLEASE WAIT....EXITING")
            for i in range(1, 30000000):
                pass
        elif x == 7:
            sys.exit()
    else:
        print("| ERROR:... ")


if __name__ == "__main__":
    main()

oopd.close()