#print.py - prints out stored objects in the database

import sys
sys.path.append("D:\GSOC\code\google") #change according to your path
from simple_string.testzodb import TestZODB
db = TestZODB('./StoreData.fs')
dbroot = db.dbroot

from organization import Organization

for key in dbroot.keys():
    object = dbroot[key]
    object.printYourself()    
    print ''

db.close()