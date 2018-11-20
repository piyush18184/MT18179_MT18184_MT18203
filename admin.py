import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user="root",
    passwd="",
    db="db"
)
# print(db)
cursor = db.cursor()


# print(cursor)

class admin:
    def __init__(self,name='',email='',phoneno='',age='',adress='',password1='',password2=''):
        self.name=name
        self.email=email
        self.phoneno=phoneno
        self.age=age
        self.adress=adress
        self.password1=password1
        self.password2=password2

    def getdoctors(self):
        cursor.execute("select * from db.doctor_details")
        for x in cursor:
            print(x)

    def getpatients(self):
        cursor.execute("select * from db.patient_details")
        for x in cursor:
            print(x)

    def adddoctor(self):
        self.name = input("| NAME:.. ")
        self.email = input("| EMAIL ID:.. ")
        self.phoneno = int(input("| PHONE NUMBER:....."))
        self.age = int(input("| AGE:....."))
        self.adress = input("| ADDRESS:")
        #               gender = input("enter the gender:.....")
        #               pateint_type = input("OPD or Location:..............")
        self.password1 = input("| PASSWORD:..... ")
        self.password2 = input("| RE-TYPE PASSWORD:......")  ##### also rechecks the password
        if self.password1 == self.password2:
            ######### need to be changed according to table
            cursor.execute(
                "SELECT SUBSTRING(D_ID,3,5) FROM `db`.`doctor_details` ORDER BY D_ID DESC LIMIT 1")
            p1 = cursor.fetchone()
            y = str(int(p1[0]) + 1)
            x = 'D_'
            D_ID = x + y
            sql = "INSERT INTO `db`.`doctor_details` (D_ID,D_Name,D_Age,D_PNo,D_Add,D_Email) VALUES('%s','%s',%s,%s,'%s','%s')"
            val = (D_ID, self.name, self.age, self.phoneno, self.adress, self.email)
            cursor.execute(sql % val)
            db.commit()
            for i in range(1, 30000000):
                pass
                continue
            print(" ___________________________________ ")
            print("| DOCTOR DETAILS ADDED SUCCESSFULLY:...|")
            print("| USER ID:... ", D_ID)
            sql = "INSERT INTO `db`.`admin` (ID,Password,Email) VALUES('%s','%s','%s')"
            val = (D_ID, self.password1, self.email)
            cursor.execute(sql % val)
            db.commit()

    def doctorlogin(self, name, pswrd):
        cursor.execute(
            "SELECT count(*) FROM `db`.`admin` where BINARY ID='" + name + "' AND BINARY Password='" + pswrd + "';")
        p1 = cursor.fetchone()
        return p1[0]

    def assigndoctor(self):
        cursor.execute("SELECT COUNT(UP_ID) FROM `db`.`unassigned_patient`")
        p1 = cursor.fetchone()
        y = p1[0]
        for i in range(1, y):
            cursor.execute("SELECT UP_ID FROM `db`.`unassigned_patient` ORDER BY UP_ID ASC LIMIT 1")
            p2 = cursor.fetchone()
            y2 = p2[0]
            # print(y2)
            cursor.execute(
                "SELECT D_DID FROM `db`.`doctor_professional_details` WHERE D_Department=(SELECT UP_PROB_DEP FROM `db`.`unassigned_patient` WHERE UP_ID=(SELECT UP_ID FROM `db`.`unassigned_patient` ORDER BY UP_ID ASC LIMIT 1));")
            p3 = cursor.fetchone()
            y3 = p3[0]
            # print(y3)
            sql = "INSERT INTO `db`.`doctor_assignment` (`DOC_ID`, `PAT_ID`, `DOC_MAX_LMT`, `REF_DOC_ID`) VALUES('%s','%s',%s,'%s')"
            val = (y3, y2, 20, '')
            cursor.execute(sql % val)
            db.commit()
            cursor.execute("DELETE FROM `db`.`unassigned_patient` WHERE UP_ID='" + y2 + "';")
            db.commit()

    def deletedoctor(self):
        x = input("ENTER THE DOCTOR ID TO BE DELETED ")
        cursor.execute(
            "UPDATE `db`.`doctor_assignment` SET DOC_ID=(SELECT D_ID FROM `db`.`opd`,`db`.`doctor_professional_details` "
            "WHERE D_dep=(SELECT D_Department FROM `db`.`doctor_professional_details` WHERE D_DID='" + x + "') "
            "AND `db`.`doctor_professional_details`.`D_DID`=`db`.`opd`.`D_ID` AND D_Type "
            "NOT IN (SELECT D_Type FROM `db`.`doctor_professional_details` WHERE D_DID='" + x + "')) WHERE DOC_ID='" + x + "';")
        db.commit()
        cursor.execute("DELETE FROM `db`.`doctor_details` WHERE D_ID = '" + x + "';")
        db.commit()
        cursor.execute("DELETE FROM `db`.`doctor_professional_details` WHERE D_DID = '" + x + "';")
        db.commit()
        cursor.execute("DELETE FROM `db`.`admin` WHERE ID = '" + x + "';")
        db.commit()
        print("DOCTOR DELETED SUCCESSFULLY ")

    def mangementwindow(self):
        pass