import datetime
import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user="root",
    passwd="",
    db="db"
)
print(db)
cursor = db.cursor()
print(cursor)



class Hospital:
    list_of_patients = [];
    list_of_doctors = [];
    list_of_departments = [];

    def __init__(self):
        pass

    ##################################################################################################
    def getdoctorsname(self, name):
        cursor.execute("SELECT * FROM `db`.`doctor_details` where D_Name = '" + name + "';")
        print(cursor.fetchall())

    ########################################################################################
    def getdoctorsid(self, id):
        cursor.execute("SELECT * FROM `db`.`doctor_details` where D_DID = '" + id + "';")
        print(cursor.fetchall())

    ###############################################################################################
    def getdoctorsdept(self, dep):
        cursor.execute("SELECT * FROM `db`.`doctor_details` where D_Department = '" + dep + "';")
        print(cursor.fetchall())

    ###############################################################################################
    def getappointmentdept(self, dep, u_id):
        now = datetime.datetime.now()
        cursor.execute("SELECT Dep_sym FROM `db`.`department` where D_Name = '" + dep + "';")
        x = cursor.fetchone()
        cursor.execute("SELECT SUBSTRING(P_Appointment_ID,5,7) FROM `db`.`appointments` ORDER BY D_ID DESC LIMIT 1")
        p1 = cursor.fetchone()
        y = str(int(p1[0]) + 1)
        a = x + y  ####genearted pateint id
        #############################################################################
        ###### NEED TO ENSURE THAT DOCTOR ID ALLOCATED BY SYSTEM SHOULD BE OF SAME DEPARTMENT
        sql = "INSERT INTO `db`.`appointments` (`P_Appointment_ID`, `Appointed_D_ID`, `P_Appointment_Date`, `P_Appointment_Time`, `P_ID`)VALUES('%s','%s','%s','%s','%s','%s')"
        val = (a, 'D_112', now.date(), now.time(), u_id)
        cursor.execute(sql % val)
        db.commit()

    ###############################################################################################
    def getappointmentid(self, dep, u_id):
        now = datetime.datetime.now()
        cursor.execute("SELECT D_Department FROM `db`.`doctor_professional_details` where D_DID = '" + dep + "';")
        x = cursor.fetchone()
        z = x[0]
        cursor.execute("SELECT Dep_sym FROM `db`.`department` where Dep_Name = '" + z + "';")
        b = cursor.fetchone()
        c=b[0]
        y = u_id+'_'+c+'_'+str(now)
        # a = b + y  ####genearted pateint id
        #############################################################################
        ###### NEED TO ENSURE THAT DOCTOR ID ALLOCATED BY SYSTEM SHOULD BE OF SAME DEPARTMENT
        sql = "INSERT INTO `db`.`patient_medical_history` (`Ref_ID`,`Pat_ID`,`Prescription`,`Past_Reports`) VALUES ('%s','%s','%s','%s')"
        val = (y,u_id,'', '')
        cursor.execute(sql % val)
        db.commit()
        return y

    ###############################################################################################
    def checkavailability(self, id):
        ### write sql query for searching the no of p[ateimts assigned to a doctor id]
        ### for no of pateintsas well as for for timings
        pass

    ###############################################################################################
    def gettiming(self, did):
        cursor.execute(
            "SELECT D_OPD_TIME_START, D_OPD_TIME_END FROM `db`.`doctor_professional_details` where D_DID = '" + did + "';")
        print(cursor.fetchall())

    ###############################################################################################
    def getdepartments(self):
        cursor.execute("SELECT `department`.`Dep_Name` FROM `db`.`department`")
        print(cursor.fetchall())

    ###############################################################################################
    def getdoctordetail(self, did):
        cursor.execute("SELECT * FROM `db`.`doctor_details` where D_ID = '" + did + "';")
        print(cursor.fetchall())

    ###############################################################################################
    def getpateinthistory(self, pid):
        cursor.execute("SELECT * FROM `db`.`patient_medical_history` where Pat_ID = '" + pid + "';")
        print(cursor.fetchall())

    ###############################################################################################

    def getpatientsallocated(self, did):
        cursor.execute("SELECT * FROM `db`.`doctor_assignment` where Appointed_D_ID = '" + did + "';")
        print(cursor.fetchall())

    def setdoctors(self):
        pass

    def setdepartments(self):
        pass

    def setpatients(self):
        pass