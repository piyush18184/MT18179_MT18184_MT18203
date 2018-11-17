# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:59:33 2018

@author: lenovo
"""
import department as dp
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


class Testdepartment(unittest.TestCase):
    
    def testgetdepdetail(self):
        res=dp.getalldep(self,'D_101')
        self.assertEqual(res,0)
        
    def testgetdepinfo(self):
        res1=dp.getdepinfo(self,'D_123')
        self.assertEqual(res1,0)
        
    def testgetdepcontact(self):
        res2=dp.getdepcontact(self,'D_102')
        self.assertEqual(res2,0)
    
    def testgetdepbuilding(self):
        res3=dp.getdepbuilding(self,'D_102')
        self.assertEqual(res3,0)
        
    def testgetdeprooms(self):
        res4=dp.getdeprooms(self,'D_102')
        self.assertEqual(res4,0)
        
    def testgetdephod(self):
        res=dp.getdephod(self,'D_101')
        self.assertEqual(res,0)
        
    def testgetdepid(self):
        res1=dp.getdepid(self,'D_123')
        self.assertEqual(res1,0)
        

if '__name__' == '__main__':
    unittest.main(defaultTest='Testdepartment')
