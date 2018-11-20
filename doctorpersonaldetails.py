import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user="root",
    passwd="6%w<RPl4",
    db="mydb"
)
# print(mydb)
cursor = db.cursor()


class doctorpersonaldetails:
    def __init__(self,name = '',age = '',pno = '',did = '',email = '',addr = ''):
        self.name = name
        self.age = age
        self.did = did
        self.email = email
        self.pno = pno
        self.addr = addr
        

    def setdoctorname(self, name, did):
        self.name = name
        self.did = did
        cursor.execute("UPDATE `mydb`.`doctor_details` SET D_Name = '" + self.name + "' WHERE D_ID = '" + self.did + "';")
        db.commit()

    def setdoctorage(self, ageee, did):
        self.age = ageee
        self.did = did
        cursor.execute("UPDATE `mydb`.`doctor_details` SET D_Age = '" + self.age + "' WHERE D_ID = '" + self.did + "';")
        db.commit()

    def setdoctorpno(self, pno, did):
        self.did = did
        self.pno = pno
        cursor.execute("UPDATE `mydb`.`doctor_details` SET D_PNo = '" + self.pno + "' WHERE D_ID = '" + self.did + "';")
        db.commit()

    def setdoctoremail(self, emaii, did):
        self.did = did
        self.email = emaii
        cursor.execute("UPDATE `mydb`.`doctor_details` SET D_Email = '" + self.email + "' WHERE D_ID = '" + self.did + "';")
        db.commit()

    def setdoctoraddr(self, addr, did):
        self.addr = addr
        self.did = did
        cursor.execute("UPDATE `mydb`.`doctor_details` SET D_Add = '" + self.addr + "' WHERE D_ID = '" + self.did + "';")
        db.commit()

    def getdocdetail(self, did):
        self.did =did
        cursor.execute("SELECT * FROM `mydb`.`doctor_details` WHERE D_ID='" + self.did + "';")
        print(cursor.fetchall())

    def getdocname(self, did):
        self.did = did
        cursor.execute("SELECT D_Name FROM `mydb`.`doctor_details` WHERE D_ID='" + self.did + "';")
        print(cursor.fetchone())

    def getdocemail(self, did):
        self.did = did
        cursor.execute("SELECT D_Email FROM `mydb`.`doctor_details` WHERE D_ID='" + self.did + "';")
        print(cursor.fetchall())

    def getdocphone(self,did):
        self.did = did
        cursor.execute("SELECT D_PNo FROM `mydb`.`doctor_details` WHERE D_ID='" + self.did + "';")
        print(cursor.fetchall())

    def getdocaddress(self,did):
        self.did = did
        cursor.execute("SELECT D_Add FROM `mydb`.`doctor_details` WHERE D_ID='" + self.did + "';")
        print(cursor.fetchall())


# a = doctorpersonaldetails()
# a.getdocaddress('D_105')
# a.getdocdetail('D_105')
# a.getdocname('D_105')
# a.getdocphone('D_105')
# a.getdocemail('D_105')
