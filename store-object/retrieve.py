#retrieve.py - Retrieve a object and change attributes
from testzodb import TestZODB, transaction
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
retrieveorg.addMentor('Sidnei da Silva')

transaction.commit()
db.close()