# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:40:24 2018

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


class Testdoctor(unittest.TestCase):
    
     def testgetdocdetail(self):
        res=dpd.getdocdetail(self,'D_101')
        self.assertEqual(res,0)
        
     def testgetdocname(self):
        res1=dpd.getdocname(self,'D_123')
        self.assertEqual(res1,0)
        
     def testgetdocphone(self):
        res2=dpd.getdocphone(self,'D_102')
        self.assertEqual(res2,0)
    
     def testgetdocaddress(self):
        res3=dpd.getdocaddress(self,'D_102')
        self.assertEqual(res3,0)
        
     def testgetdocemail(self):
        res4=dpd.getdocemail(self,'D_102')
        self.assertEqual(res4,0)
        
if '__name__' == '__main__':
    unittest.main(defaultTest='Testdoctor')

    
    