#store.py - Store a simple string in the database

from testzodb import TestZODB, transaction
db = TestZODB('./StoreData.fs')
dbroot = db.dbroot
dbroot['store_string'] = 'Charith is doing coding for learning ZODB'
dbroot['store_message'] = 'First example with ZODB!!'
transaction.commit()
db.close()
