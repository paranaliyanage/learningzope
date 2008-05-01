#print.py - prints out stored objects in the database

from testzodb import TestZODB
db = TestZODB('./StoreData.fs')
dbroot = db.dbroot

from student import Student
for key in dbroot.keys():
    object = dbroot[key]
    if isinstance(object,Student):
        print 'name:' + object.name , '\t organization:' + object.organization.name

db.close()
