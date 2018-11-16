import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user="root",
    passwd="",
    db="db"
)
# print(db)
cursor = db.cursor()


class doctorpersonaldetails:
    def __init__(self):
        pass

    def setdoctorname(self, name, did):
        cursor.execute("UPDATE `db`.`doctor_details` SET D_Name = '" + name + "' WHERE D_ID = '" + did + "';")
        db.commit()

    def setdoctorage(self, ageee, did):
        cursor.execute("UPDATE `db`.`doctor_details` SET D_Age = '" + ageee + "' WHERE D_ID = '" + did + "';")
        db.commit()

    def setdoctorpno(self, pno, did):
        cursor.execute("UPDATE `db`.`patient_details` SET D_PNo = '" + pno + "' WHERE D_ID = '" + did + "';")
        db.commit()

    def setdoctoremail(self, emaii, did):
        cursor.execute("UPDATE `db`.`doctor_details` SET D_Email = '" + emaii + "' WHERE D_ID = '" + did + "';")
        db.commit()

    def setdoctoraddr(self, addr, did):
        cursor.execute("UPDATE `db`.`doctor_details` SET D_PNo = '" + addr + "' WHERE D_ID = '" + did + "';")
        db.commit()

    def getdocdetail(self, did):
        cursor.execute("SELECT * FROM `db`.`doctor_details` WHERE D_ID='" + did + "';")
        print(cursor.fetchall())

    def getdocname(self, did):
        cursor.execute("SELECT D_Name FROM `db`.`doctor_details` WHERE D_ID='" + did + "';")
        print(cursor.fetchone())

    def getdocemail(self, did):
        cursor.execute("SELECT D_Email FROM `db`.`doctor_details` WHERE D_ID='" + did + "';")
        print(cursor.fetchall())

    def getdocphone(self,did):
        cursor.execute("SELECT D_PNo FROM `db`.`doctor_details` WHERE D_ID='" + did + "';")
        print(cursor.fetchall())

    def getdocaddress(self,did):
        cursor.execute("SELECT D_Add FROM `db`.`doctor_details` WHERE D_ID='" + did + "';")
        print(cursor.fetchall())