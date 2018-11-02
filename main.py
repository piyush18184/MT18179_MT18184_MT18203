import sys
from patient import patient as p
from patientmedicalreport import *
from admin import *
from doctorpersonaldetails import *
from doctorproffessionaldetails import *
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
                        if ch == 1:
                            cursor.execute("select * from db.doctor_details")
                            for x in cursor:
                                print(x)
                        elif ch == 2:
                            cursor.execute("select * from db.patient_details")
                            for x in cursor:
                                print(x)
                        elif ch == 3:
                            pass
                        elif ch == 4:
                            pass
                        elif ch == 5:
                            pass
                        elif ch == 6:
                            print("| LOGGING OUT...PRESS ANY KEY TO CONTINUE..!")
                            a = input("")
                            break
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
                cursor.execute("SELECT count(*) FROM `db`.`admin` where ID='" + name + "' AND Password='" + pswrd + "';")
                p1 = cursor.fetchone()
                y = int(p1[0])
                if y==0:
                # if(cursor.execute("SELECT ID FROM `db`.`admin` where ID='" + d_id + "' AND Password='" + pswrd + "';") != None):
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
                            #### edit doctor profile
                            pass
                        elif x == 3:

                            ### sort of pateint depending upon department, id
                            pass
                        elif x == 4:
                            #### leave of doctors
                            pass
                        elif x == 5:
                            ######  view profile
                            pass
                        elif x == 6:
                            #### refereral if required
                            pass
                        elif x == 7:
                            print("| LOGGING OUT...PRESS ANY KEY TO CONTINUE..!")
                            a = input("")
                            break
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
                                cursor.execute("SELECT * FROM `mydb`.'doctor_details` where D_Name = '" + ch + "';")
                                cursor.fetchall()
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
                                print("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
                            elif x == 3:
                                ch = input("| ENTER THE DOCTOR'S ID TO BE SEARCHED:... ")
                                print("| DOCTOR'S LIST:... ")
                                print("| ENTER THE DOCTOR'S ID FOR APPOINTMENT:... ")
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
                        else:
                            return False

        elif x == 5:
            print(" __________________________________________________________________________ ")
            print("|----------------------------PASSWORD RESET PAGE---------------------------|")
            print("|                                                                          |")
            #### forgot password
            pass

        elif x == 6:
            print(" __________________________________________________________________________ ")
            print("|------------------------------EMERGENCY PAGE------------------------------|")
            print("|                                                                          |")
            #### critical pateint
            pass
        elif x == 7:
            sys.exit()
    else:
        print("| ERROR:... ")


if __name__ == "__main__":
    main()

db.close()
