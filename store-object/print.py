#print.py - prints out stored objects in the database

from testzodb import TestZODB
db = TestZODB('./StoreData.fs')
dbroot = db.dbroot

from organization import Organization

for key in dbroot.keys():
    object = dbroot[key]
    if isinstance(object,Organization):
        print 'Organization name: ' + object.name
        if (object.projects):
            for i in range(0,len(object.projects)):
                print '\t Project name: ' + object.projects[i].name
                print '\t \t Mentor name: ' + object.projects[i].mentor.name
                print '\t \t Student: ' + object.projects[i].student.name
                
        if(object.otherMentors):
            for i in range(0,len(object.otherMentors)):
                print ""
                print '\t Other mentors: ' + object.otherMentors[i]
            

db.close()
