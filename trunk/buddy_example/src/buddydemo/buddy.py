import zope.interface
import persistent
from buddydemo.interfaces import IBuddy

class Buddy(persistent.Persistent):
    """Buddy information"""
    
    zope.interface.implements(IBuddy)

    def __init__(self, first='', last='', second='', email='', address='', pc=''):
        self.first = first
	self.last = last
        self.second = second
	self.email = email
	self.address = address
	self.postal_code = pc

    def name(self):
	return "%s %s" % (self.first, self.last)


from buddydemo.interfaces import IPostalInfo, IPostalLookup
from zope.app import zapi

class BuddyCityState:
    
    zope.interface.implements(IPostalInfo)

    __used_for__ = IBuddy

    def __init__(self, buddy):
	lookup=zapi.getUtility(IPostalLookup)
	info = lookup.lookup(buddy.postal_code)
	if info is None:
	    self.city, self.state = '',''
	else:
	    self.city, self.state = info.city, info.state

