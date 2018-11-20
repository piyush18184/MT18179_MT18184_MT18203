import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user="root",
    passwd="6%w<RPl4",
    db="db"
)
print(db)
cursor = db.cursor()
print(cursor)




class doctorprofessionaldetails:
    def __init__(self,did = '',opdst = '',opdet = '',dtyp = '',spec = '',extno = '',rmno = '',dep = '',name = ''):
        self.opdst = opdst
        self.opdet = opdet
        self.spec = spec
        self.dtyp = dtyp
        self.extno = extno
        self.rmno = rmno
        self.did = did
        self.dep = dep
        self.name = name
    def getdocprofessinalall(self, did):
        self.did = did
        cursor.execute("SELECT * FROM `db`.`doctor_professional_details` WHERE D_ID='" + self.did + "';")
        print(cursor.fetchall())

    def setdoctordepartment(self, dep, did):
        self.dep = dep
        self.did = did
        cursor.execute(
            "UPDATE `db`.`doctor_professional_details` SET D_Department = '" + self.dep + "' WHERE D_ID = '" + self.did + "';")
        db.commit()

    def assigndoctoropd(self, did):
        self.did = did
        cursor.execute("SELECT D_Department FROM `db`.`doctor_professional_details` WHERE D_DID = '" + self.did + "';")
        aa=cursor.fetchone()
        bb=aa[0]
        self.dep = bb
        cursor.execute("SELECT D_Name FROM `db`.`doctor_details` WHERE D_ID = '" + self.did + "';")
        cc = cursor.fetchone()
        dd = cc[0]
        self.name = dd
        cursor.execute("SELECT count(D_ID) FROM `db`.`opd` WHERE D_dep='"+self.dep+"';")
        xxx =cursor.fetchone()
        yyy=int(xxx[0])
        if (yyy==0):
            sql="INSERT INTO `db`.`opd` (`D_ID`,`D_dep`,`D_name`) VALUES('%s','%s','%s')"
            val=(self.did,self.dep,self.name)
            cursor.execute(sql % val)
            db.commit()
        else:
            cursor.execute("UPDATE `db`.`opd` SET D_ID = '" + self.did + "' , D_dep='" + self.dep + "' , D_name='" + self.name + "' WHERE D_dep = '" + bb + "';")
            db.commit()

    def setopdstarttime(self, opdst, did):
        self.opdst = opdst
        self.did = did
        cursor.execute(
            "UPDATE `db`.`doctor_professional_details` SET D_OPD_TIME_START = '" + self.opdst + "' WHERE D_DID = '" + self.did + "';")
        db.commit()

    def setopdendttime(self, opdet, did):
        self.opdet = opdet
        self.did = did
        cursor.execute(
            "UPDATE `db`.`doctor_professional_details` SET D_OPD_TIME_END = '" + self.opdet + "' WHERE D_DID = '" + self.did + "';")
        db.commit()

    def setdoctype(self, dtyp, did):
        self.dtyp = dtyp
        self.did = did
        cursor.execute(
            "UPDATE `db`.`doctor_professional_details` SET D_Type = '" + self.dtyp + "' WHERE D_DID = '" + self.did + "';")
        db.commit()
    def getdoctype(self, did):
        self.did = did
        cursor.execute(
            "SELECT D_Type FROM `db`.`doctor_professional_details` WHERE D_DID = '" + self.did + "';")
        print(cursor.fetchone())
    def setdocspecialisation(self, spec, did):
        self.spec = spec
        self.did = did
        cursor.execute(
            "UPDATE `db`.`doctor_professional_details` SET D_Specialization = '" + self.spec + "' WHERE D_ID = '" + self.did + "';")
        db.commit()
    def getdocspecialisation(self,did):
        self.did = did
        cursor.execute(
            "SELECT D_Specialization FROM `db`.`doctor_professional_details` WHERE D_ID = '" + self.did + "';")
        print(cursor.fetchone())
    def setextensionno(self, ext, did):
        self.extno = ext
        self.did = did
        cursor.execute(
            "UPDATE `db`.`doctor_professional_details` SET D_ExtensionNo = '" + self.extno + "' WHERE D_ID = '" + self.did + "';")
        db.commit()

    def setroomno(self, rmno, did):
        self.rmno = rmno
        self.did = did
        cursor.execute(
            "UPDATE `db`.`doctor_professional_details` SET D_RoomNo = '" + self.rmno + "' WHERE D_ID = '" + self.did + "';")
        db.commit()
    def getdoctype(self, did):
        self.did = did
        cursor.execute(
            "SELECT D_Type FROM `db`.`doctor_professional_details` WHERE D_DID = '" + self.did + "';")
        print(cursor.fetchone())
    def getopdstarttime(self, did):
         self.did = did
         cursor.execute(
            "SELECT D_OPD_TIME_START FROM `db`.`doctor_professional_details` WHERE D_DID = '" + self.did + "';")
         print(cursor.fetchone())
    def getopdendtime(self, did):
         self.did = did
         cursor.execute(
            "SELECT D_OPD_TIME_END FROM `db`.`doctor_professional_details` WHERE D_DID = '" + self.did + "';")
         print(cursor.fetchone())
    def getroomno(self,did):
        self.did = did
        cursor.execute(
            "SELECT D_RoomNo FROM `db`.`doctor_professional_details` WHERE D_ID = '" + self.did + "';")
        print(cursor.fetchone())
    def getextensionno(self,did):
        self.did = did
        cursor.execute(
            "SELECT D_ExtensionNo FROM `db`.`doctor_professional_details` WHERE D_ID = '" + self.did + "';")
        print(cursor.fetchone())

    def getdoctordepartment(self,did):

        self.did = did
        cursor.execute(
            "SELECT D_Department FROM `db`.`doctor_professional_details` WHERE D_ID = '" + self.did + "';")
        print(cursor.fetchone())





a = doctorprofessionaldetails()
a.getdocprofessinalall('D_101')
