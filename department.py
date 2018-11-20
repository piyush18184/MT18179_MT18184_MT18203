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
    def __init__(self,name='', did = '',build = '',d_name = '',contact = '',room = '',opd = ''):
        self.name=name
        self.did= did
        self.build = build
        self.dname = d_name
        self.contact = contact
        self.room = room
        self.opd = opd

    def setdephod(self, dep_id, hod):
        self.did = dep_id
        self.name = hod
        cursor.execute("UPDATE `db`.`department` SET Dep_HOD = '" + self.name + "' WHERE Dep_ID = '" + self.did + "';")
        db.commit()

    def setdep_building(self, dep_id, building):
        self.did = dep_id
        self.build = building
        cursor.execute(
            "UPDATE `db`.`department` SET Dep_Building = '" + self.build + "' WHERE Dep_ID = '" + self.did + "';")
        db.commit()

    def setdepcontact(self, dep_id, contact):
        self.did = dep_id
        self.contact = contact
        cursor.execute(
            "UPDATE `db`.`department` SET Dep_Contact = '" + self.contact + "' WHERE Dep_ID = '" + self.did + "';")
        db.commit()

    def setdeprooms(self, dep_id, room):
        self.did = dep_id
        self.room = room
        cursor.execute("UPDATE `db`.`department` SET Dep_Room = '" + self.room + "' WHERE Dep_ID = '" + self.did + "';")
        db.commit()

    def setdepopd(self, dep_id, opd):
        self.did = dep_id
        self.opd = opd
        cursor.execute("UPDATE `db`.`department` SET Dep_OPD = '" + self.opd + "' WHERE Dep_ID = '" + self.did + "';")
        db.commit()

    def setdepname(self, dep_id, name):
        self.did = dep_id
        self.dname = name
        cursor.execute("UPDATE `db`.`department` SET Dep_Name = '" + self.dname + "' WHERE Dep_ID = '" + self.did + "';")
        db.commit()

    def getalldep(self, dep_id):
        self.did = dep_id
        cursor.execute("SELECT Dep_Name FROM db.department")
        print(cursor.fetchall())

    def getdepinfo(self, dep_id):
        self.did = dep_id
        cursor.execute("SELECT * FROM `db.department` WHERE Dep_ID='" + self.did + "';")
        print(cursor.fetchall())

    def getdepbuilding(self, dep_id):
        self.did = dep_id
        cursor.execute("SELECT Dep_Building Dep_Room FROM `db.department` WHERE Dep_ID='" + self.did + "';")
        print(cursor.fetchall())

    def getdepcontact(self, dep_id):
        self.did = dep_id
        cursor.execute("SELECT Dep_Contact FROM `db.department` WHERE Dep_ID='" + self.did + "';")
        print(cursor.fetchall())

    def getdeprooms(self, dep_id):
        self.did = dep_id
        cursor.execute("SELECT Dep_Room Dep_Building FROM `db.department` WHERE Dep_ID='" + self.did + "';")
        print(cursor.fetchall())

    def getdephod(self, dep_id):
        self.did = dep_id
        cursor.execute("SELECT Dep_HOD FROM `db.department` WHERE Dep_ID='" + self.did + "';")
        print(cursor.fetchall())

    def getdepid(self, dep_id):
        self.did = dep_id
        cursor.execute("SELECT Dep_ID FROM `db.department` WHERE Dep_ID='" + self.did + "';")
        print(cursor.fetchall())
