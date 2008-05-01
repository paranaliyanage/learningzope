#store.py - stores objects in the database

from testzodb import TestZODB, transaction
db = TestZODB("./StoreData.fs")
dbroot = db.dbroot

from student import Student
from organization import Organization

organization1 = Organization('Zope Foundation')
student1 = Student('Charith',organization1)
dbroot['student1'] = student1
org2 = Organization('Plone Foundation')
student2 = Student('TestStudent', org2)
dbroot['student2'] = student2

transaction.commit()
db.close()

