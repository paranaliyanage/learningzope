#google.py - Select projects and stores them in the database
import sys
sys.path.append("D:\GSOC\code\google") #change according to your path
from simple_string.testzodb import TestZODB, transaction
#from testzodb import TestZODB, transaction
from organization import Organization
from mentor import Mentor
from student import Student
from project import Project

db = TestZODB("./StoreData.fs")
dbroot = db.dbroot

student11 = Student(4,'Charith')
mentor11 = Mentor(4,'Groszer')
organization1 = Organization('Zope Foundation')
project11 = Project('OCQL',mentor11,student11)
organization1.addProject(project11)

dbroot['org1'] = organization1

student12 = Student(5,'Ulrich Fouquet')
mentor12 = Mentor(1,'Martijn Faassen')
project12 = Project('Grok',mentor12,student12)
organization1.addProject(project12)


student21 = Student(1,'Martin Lundwall')
mentor21 = Mentor(4,'Lennart Regebro')
organization2 = Organization('Plone Foundation')
project21 = Project('Integration',mentor21,student21)
organization2.addProject(project21)

dbroot['org2'] = organization2

transaction.commit()
db.close()