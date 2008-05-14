#retrieve.py - Retrieve a object and change attributes
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

student31 = Student(1,'Robert Schuppenies')
mentor31 = Mentor(4,'Martin v. Löwis')
organization3 = Organization(' Python Software Foundation')
project31 = Project(' Python Memory Profiler',mentor31,student31)
organization3.addProject(project31)

dbroot['org3'] = organization3

retrieveorg = dbroot['org1']
othermentor = Mentor(6,'Sidnei da Silva')
retrieveorg.addMentor(othermentor)

transaction.commit()
db.close()