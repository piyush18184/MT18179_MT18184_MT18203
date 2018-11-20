from doctor import doctor as doc
import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user="root",
    passwd="",
    db="db"
)
# print(db)
cursor = db.cursor()





class HOD:
    def __init__(self,hid='',resp=''):
        self.hid=hid
        self.resp=resp

    def sethod(self):

        hid = input("| HOD ID:.. ")
        cursor.execute("SELECT * FROM `db`.`hod` WHERE BINARY H_ID='" + hid + "';")
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
            xxxx = int(input("PLEASE CONFIRM..?"))
            if xxxx == 1:
                cursor.execute(
                    "UPDATE `db`.`hod` SET H_ASSIGNMENT_DEP = '" + hdep + "' WHERE H_ID = '" + hid + "';")
                db.commit()
                print(" ___________________________________ ")
                print("| HOD ASSIGNED SUCCESSFULLY TO A DEPARTMENT:...|")
                cursor.execute("SELECT * FROM `db`.`hod` WHERE BINARY H_ID = '" + hid + "';")
                print(cursor.fetchall())
            elif xxxx == 2:
                print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
                for i in range(1, 30000000):
                    pass
                #continue
            else:
                print("WRONG OPTION SELECTED...PLEASE TRY AGAIN")
                #continue
        elif xxx == 2:
            print("RETURNING TO PREVIOUS PAGE...PLEASE WAIT..")
            for i in range(1, 30000000):
                pass
            #continue
    def gethodall(self):
        print(
            " __________________________________________________________________________ ")
        print(
            "|--------------------------------HOD LIST----------------------------------|")
        cursor.execute("SELECT * FROM `db`.`hod`")
        print(cursor.fetchall())

    def getopdall(self):
        print(" __________________________________________________________________________ ")
        print("|---------------------------OPD DOCTOR LIST--------------------------------|")
        cursor.execute("SELECT * FROM `db`.`opd`")
        print(cursor.fetchall())

    def getdocdetails(self,did):
        print(" __________________________________________________________________________ ")
        print("|---------------------------OPD DOCTOR LIST--------------------------------|")
        cursor.execute("SELECT * FROM `db`.`doctor_details`,`db`.`doctor_professional_details` WHERE `db`.`doctor_details`.`D_ID`='"+did+"' AND `db`.`doctor_details`.`D_ID`=`db`.`doctor_professional_details`.`D_DID`;")
        print(cursor.fetchall())

    def assigndocopd(self,dpd):
        docid = input("| PLEASE ENTER THE DOCTOR's ID WHOSE INFROMATION NEEDS TO BE MODIFIED:...")
        dpd.assigndoctoropd(docid)
        print("DOCTOR DETAILS UPDATED SUCCESSFULLY")

    def setopdstarttiming(self,dpd):
        docid = input("| PLEASE ENTER THE DOCTOR's ID WHOSE INFROMATION NEEDS TO BE MODIFIED:...")
        opdst = input("| PLEASE ENTER THE END TIME FOR OPD(24 HOUR FORMAT(hh:mm:ss)):...")
        dpd.setopdstarttime(opdst,docid)
        print("DOCTOR DETAILS UPDATED SUCCESSFULLY")

    def setopdendtiming(self,dpd):
        docid = input("| PLEASE ENTER THE DOCTOR's ID WHOSE INFROMATION NEEDS TO BE MODIFIED:...")
        opdent = input("| PLEASE ENTER THE END TIME FOR OPD(24 HOUR FORMAT(hh:mm:ss)):...")
        dpd.setopdsendtime(opdent, docid)
        print("DOCTOR DETAILS UPDATED SUCCESSFULLY")
    def setdocroomno(self,dpd):
        docid = input("| PLEASE ENTER THE DOCTOR's ID WHOSE INFROMATION NEEDS TO BE MODIFIED:...")
        rno = input("| PLEASE ENTER THE ROOM NUMBER(24 HOUR FORMAT(hh:mm:ss)):...")
        dpd.setroomno(rno,docid)
        print("DOCTOR DETAILS UPDATED SUCCESSFULLY")
    def setdocextensionno(self,dpd):
        docid = input("| PLEASE ENTER THE DOCTOR's ID WHOSE INFROMATION NEEDS TO BE MODIFIED:...")
        dcon = input("| PLEASE ENTER THE ROOM NUMBER(24 HOUR FORMAT(hh:mm:ss)):...")
        dpd.setextensionno(dcon,docid)
        print("DOCTOR DETAILS UPDATED SUCCESSFULLY")
    def gethodroom(self):
        pass

    def gethodcontact(self):
        pass

    def gethodqualification(self):
        pass

    def sethoddep(self):
        pass

    def sethodroom(self):
        pass

    def sethodcontact(self):
        pass

    def sethodqualification(self):
        pass

