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
            "UPDATE `mydb`.`patient_medical_history` SET Prescription = '" + y1 + "' WHERE P_ID = '" + x1 + "';")
        db.commit()

    def setpatienthistory(self):
        print(" Enter the Pateint ID whose Reports needs to be edited::")
        x1 = input()
        y1 = input("Enter Reports for updation::")
        cursor.execute(
            "UPDATE `mydb`.`patient_medical_history` SET Prescription = '" + y1 + "' WHERE P_ID = '" + x1 + "';")
        db.commit()