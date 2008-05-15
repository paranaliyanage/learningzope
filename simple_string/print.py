#print.py - Prints out the sttring in the database

from testzodb import TestZODB
db = TestZODB('./StoreData.fs')
dbroot = db.dbroot
print len(dbroot.keys())
for key in dbroot.keys():
    print key + ':', dbroot[key]
db.close()

