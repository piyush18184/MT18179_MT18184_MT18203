import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user="root",
    passwd="",
    db="db"
)
# print(db)
cursor = db.cursor()


class patientmedicalreport:
    def __init__(self):
        pass

    def setpateientpres(self):
        print(" Enter the Pateint ID whose prescriton needs to be edited::")
        x1 = input()
        y1 = input("Enter prescription::")
        cursor.execute(
            "UPDATE `db`.`patient_medical_history` SET Prescription = '" + y1 + "' WHERE Pat_ID = '" + x1 + "';")
        db.commit()

    def setpatienthistory(self):
        print(" Enter the Pateint ID whose Reports needs to be edited::")
        x1 = input()
        y1 = input("Enter Reports for updation::")
        cursor.execute(
            "UPDATE `db`.`patient_medical_history` SET Prescription = '" + y1 + "' WHERE Pat_ID = '" + x1 + "';")
        db.commit()

    def viewhistory(self, did):
        print(" Enter the Patient ID whose Reports needs to be edited::")
        x1 = input()
        cursor.execute(
            "SELECT count(DOC_ID) FROM `db`.`doctor_assignment` WHERE Pat_ID ='" + x1 + "' AND DOC_ID='" + did + "';")
        aaa = cursor.fetchone()
        bbb = aaa[0]
        if bbb == 0:
            print("Sorry..No Such Patient Assigned to you")
            pass
        else:
            cursor.execute("SELECT * FROM `db`.`patient_medical_history` WHERE Pat_ID ='" + x1 + "';")
            print(cursor.fetchall())
