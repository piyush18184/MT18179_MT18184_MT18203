from doctor import doctor as doc
import sys
from patient import patient as p
from patientmedicalreport import patientmedicalreport as pmr
import datetime
from admin import admin
from doctorpersonaldetails import doctorpersonaldetails as dpd
from doctorproffessionaldetails import doctorprofessionaldetails as ddd
from Hospital import Hospital as h
from HOD import HOD as hod
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
                            a1.assigndoctor()
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
                                p1=p()
                                p1.editpatient()
                            elif x == 2:
                                print(" __________________________________________________________________________ ")
                                print("|----------------PATIENT'S MEDICAL HISTORY EDIT WINDOW---------------------|")
                                print("|                                                                          |")
                                print("|                        1. EDIT PATIENT'S PRESCRIPTION                    |")
                                print("|                        2. EDIT PATIENT'S PAST REPORTS                    |")
                                print("|                        3. RETURN TO PREVIOUS PAGE                        |")
                                print("|__________________________________________________________________________|")
                                xx = int(input("Enter your choice:....."))
                                pmr1 = pmr()
                                if xx == 1:
                                    pmr1.setpateientpres()
                                elif xx == 2:
                                    pmr1.setpatienthistory()
                                elif xx == 3:
                                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                    for i in range(1, 30000000):
                                        pass
                                    continue
                                else:
                                    print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                    continue
                            elif x == 3:
                                doc2=doc()
                                d1 = dpd()
                                doc2.editdetail(d1)
                            elif x == 4:
                                doc3 = doc()
                                d2 = ddd()
                                doc3.editdocprofdetail(d2)
                            elif x == 5:
                                print(" __________________________________________________________________________ ")
                                print("|----------------------HOD MANAGEMENT EDIT WINDOW--------------------------|")
                                print("|                                                                          |")
                                print("|                        1. HOD ASSIGNMENT                                 |")
                                print("|                        2. VIEW HOD LIST                                  |")
                                print("|                        3. RETURN TO PREVIOUS PAGE                        |")
                                print("|__________________________________________________________________________|")
                                hod1 = hod()
                                xx = int(input("Enter your choice:....."))
                                if xx == 1:
                                    hod1.sethod()
                                elif xx == 2:
                                    hod1.gethodall()
                                elif xx == 3:
                                    print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                    for i in range(1, 30000000):
                                        pass
                                    continue
                                else:
                                    print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                                    continue
                            elif x == 6:
                                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                                for i in range(1, 30000000):
                                    pass
                                continue
                            elif x == 7:
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
                    cursor.execute("SELECT count(D_DID) FROM `db`.`doctor_professional_details` where BINARY D_DID='" + name + "' and BINARY D_Type='HOD';");
                    yyy=cursor.fetchone()
                    ppp=int(yyy[0])
                    print(ppp)
                    if (ppp>0):
                        while True:
                            h1 = h()
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
                                doc4 = doc()
                                d1 = dpd()
                                doc4.editdetail(d1)
                            elif x == 3:
                                h1.getdoctordetail(name)
                            elif x == 4:
                                print(" __________________________________________________________________________ ")
                                print("|------------------------DOCTOR'S REFERRAL WINDOW--------------------------|")
                                h1 = h()
                                p1 = p()
                                h1.referpatients(name,p1)
                            elif x == 5:
                                print(" __________________________________________________________________________ ")
                                print("|---------------------------HOD'S TASK WINDOW------------------------------|")
                                print("|                                                                          |")
                                print("|                        1. SET DOCTOR'S OPD TIMINGS                       |")
                                print("|                        2. ROOM ALLOTMENT                                 |")
                                print("|                        3. DEPARTMENT CONTACT                             |")
                                print("|                        4. ASSIGN DOCTOR TO OPD                           |")
                                print("|                        5. VIEW DOCTORS ASSIGNED TO OPD                   |")
                                print("|                        6. VIEW DOCTOR DETAILS ASSIGNED TO OPD            |")
                                print("|                        7. RETURN                                         |")
                                print("|__________________________________________________________________________|")
                                xxxx = int(input("Enter your choice:....."))
                                hod2 = hod()
                                dprd = ddd()
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
                                        hod2.setopdstarttiming(dprd)
                                    elif xxxxx == 2:
                                        hod2.setopdendtiming(dprd)
                                elif xxxx == 2:
                                    hod2.setdocroomno(dprd)
                                elif xxxx == 3:
                                    hod2.setdocextensionno(dprd)
                                elif xxxx == 4:
                                    hod2.assigndocopd(dprd)
                                elif xxxx == 5:
                                    hod2.getopdall()
                                elif xxxx == 6:
                                    docid = input("| PLEASE ENTER THE DOCTOR's ID WHOSE INFROMATION NEEDS TO BE VIEWED:...")
                                    hod2.getdocdetails(docid)
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
                            h1 = h()
                            print(" __________________________________________________________________________ ")
                            print("|----------------------------WELCOME TO HOMEPAGE---------------------------|")
                            print("|                                                                          |")
                            print("|                        1. SEE PATIENT ALLOCATED                          |")
                            print("|                        2. EDIT PROFILE                                   |")
                            print("|                        3. VIEW PROFILE                                   |")
                            print("|                        4. REFERRAL                                       |")
                            print("|                        5. LOGOUT                                         |")
                            print("|__________________________________________________________________________|")
                            x = int(input("Enter your choice:....."))
                            if x == 1:
                                h1.getpatientsallocated(name)
                            elif x == 2:
                                doc4 = doc()
                                d1 = dpd()
                                doc4.editdetail(d1)
                            elif x == 3:
                                h1.getdoctordetail(name)
                            elif x == 4:  ### we have to assign all doctors a level a junior level dr can only reffere someone
                                #### and also other departmental refferal only oh the consent of hod
                                #### refereral if required
                                print(" __________________________________________________________________________ ")
                                print("|------------------------DOCTOR'S REFERRAL WINDOW--------------------------|")
                                h2 = h()
                                p2 = p()
                                h2.referpatients(name,p2)
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
            p5 = p()
            p5.registerpatient()
        elif x == 4:
            aa = 1
            while aa <= 3:
                print(" __________________________________________________________________________ ")
                print("|-------------------------PATIENT's LOGIN WINDOW---------------------------|")
                u_id = input("| USERID:.. ")
                password = input("| PASSWORD:.. ")
                cursor.execute(
                    "SELECT count(*) FROM `db`.`admin` where BINARY ID='" + u_id + "' AND BINARY Password='" + password + "';")
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
                            p4 = p()
                            p4.searchdoctor(h1,u_id)
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
                            p6 = p()
                            hx = h()
                            p6.appointment(u_id,hx)
                        elif x == 7:
                            p3 = p()
                            p3.editpatientself()
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
            h3 = h()
            h3.emergency()
        elif x == 7:
            sys.exit()
    else:
        print("| ERROR:... ")


if __name__ == "__main__":
    main()

db.close()