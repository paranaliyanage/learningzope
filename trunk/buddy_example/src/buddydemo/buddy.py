import persistent

class Buddy(persistent.Persistent):
    """Buddy information"""
    
    def __init__(self, first='', second='', email='', address='', pc=''):
        self.first = first
        self.second = second
	self.email = email
	self.address = address
	self.postal_code = pc

    def name(self):
	return "%s %s" % (self.first, self.last)

