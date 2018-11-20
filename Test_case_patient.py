# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:21:01 2018

@author: lenovo
"""
from doctor import doctor as doc
import sys
from patient import patient as p
from patientmedicalreport import patientmedicalreport as pmr
import datetime
from admin import admin
from doctorpersonaldetails import doctorpersonaldetails as dpd
from doctorproffessionaldetails import doctorprofessionaldetails as ddd
from hosiptal import Hospital as h
from HOD import HOD as hod
import pymysql
import unittest

db = pymysql.connect(
    host='127.0.0.1',
    user="root",
    passwd="",
    db="project"
)
print(db)
cursor = db.cursor()
print(cursor)

class Testpatient(unittest.TestCase):
    
    def testgetpateintall(self):
        res=p.getpatientall(self,'P_107')
        self.assertEqual(res,0)
        
    def testgetpatientemail(self):
        res1=p.getpatientemail(self,'P_102')
        self.assertEqual(res1,0)
        
    def testgetpatientphone(self):
        res2=p.getpatientphone(self,'P_102')
        self.assertEqual(res2,0)
    
    def testgetpatientaddress(self):
        res3=p.getpatientaddress(self,'P_102')
        self.assertEqual(res3,0)
        
    def testgetpatientage(self):
        res4=p.getpatientage(self,'P_102')
        self.assertEqual(res4,0)
        
    def testgetpatientpasswrd(self):
        r=p.getpatientpswrd(self,'P_105')
        self.assertEqual(r,'xYz')
        
    def testsetpatientname(self):
        r5=p.setpateintname(self,'P_109')
        self.assertEqual(r5,0)

    
if '__name__' == '__main__':
    unittest.main(defaultTest='Testpatient')