import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user="root",
    passwd="",
    db="db"
)
# print(db)
cursor = db.cursor()


class department:
    doctor_list=[];
    def __init__(self,name='',id=''):
        self.name=name
        self.id=id


    def setdephod(self, dep_id, hod):
        cursor.execute("UPDATE `db`.`department` SET Dep_HOD = '" + hod + "' WHERE Dep_ID = '" + dep_id + "';")
        db.commit()

    def setdep_building(self, dep_id, building):
        cursor.execute(
            "UPDATE `db`.`department` SET Dep_Building = '" + building + "' WHERE Dep_ID = '" + dep_id + "';")
        db.commit()

    def setdepcontact(self, dep_id, contact):
        cursor.execute(
            "UPDATE `db`.`department` SET Dep_Contact = '" + contact + "' WHERE Dep_ID = '" + dep_id + "';")
        db.commit()

    def setdeprooms(self, dep_id, room):
        cursor.execute("UPDATE `db`.`department` SET Dep_Room = '" + room + "' WHERE Dep_ID = '" + dep_id + "';")
        db.commit()

    def setdepopd(self, dep_id, opd):
        cursor.execute("UPDATE `db`.`department` SET Dep_OPD = '" + opd + "' WHERE Dep_ID = '" + dep_id + "';")
        db.commit()

    def setdepname(self, dep_id, name):
        cursor.execute("UPDATE `db`.`department` SET Dep_Name = '" + name + "' WHERE Dep_ID = '" + dep_id + "';")
        db.commit()

    def getalldep(self, dep_id):
        cursor.execute("SELECT Dep_Name FROM db.department")
        print(cursor.fetchall())

    def getdepinfo(self, dep_id):
        cursor.execute("SELECT * FROM `db.department` WHERE Dep_ID='" + dep_id + "';")
        print(cursor.fetchall())

    def getdepbuilding(self, dep_id):
        cursor.execute("SELECT Dep_Building Dep_Room FROM `db.department` WHERE Dep_ID='" + dep_id + "';")
        print(cursor.fetchall())

    def getdepcontact(self, dep_id):
        cursor.execute("SELECT Dep_Contact FROM `db.department` WHERE Dep_ID='" + dep_id + "';")
        print(cursor.fetchall())

    def getdeprooms(self, dep_id):
        cursor.execute("SELECT Dep_Room Dep_Building FROM `db.department` WHERE Dep_ID='" + dep_id + "';")
        print(cursor.fetchall())

    def getdephod(self, dep_id):
        cursor.execute("SELECT Dep_HOD FROM `db.department` WHERE Dep_ID='" + dep_id + "';")
        print(cursor.fetchall())

    def getdepid(self, dep_id):
        cursor.execute("SELECT Dep_ID FROM `db.department` WHERE Dep_ID='" + dep_id + "';")
        print(cursor.fetchall())