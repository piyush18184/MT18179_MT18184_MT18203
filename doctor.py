# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:15:21 2018

@author: Jeet
"""
class doctor:
    def __init__(self):
        pass

    def editdetail(sel,d1):
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
            
                else:
                    print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                    
            elif xx == 2:
                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                for i in range(1, 30000000):
                    pass
                
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
    def editdocprofdetail(self,d2):
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
                            else:
                                print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                        elif xx == 2:
                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                            for i in range(1, 30000000):
                                pass
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
                            else:
                                print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                        elif xx == 2:
                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                            for i in range(1, 30000000):
                                pass
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
                            else:
                                print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                        elif xx == 2:
                            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                            for i in range(1, 30000000):
                                pass
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
                        #continue
                    else:
                        print("| WRONG CHOICE ENTERED..PLEASE TRY AGAIN")
                        #continue
               
    def enterhod(self):
        pass

