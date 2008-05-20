import zope.interface
from buddydemo.interfaces import IPostalInfo, IPostalLookup

class Info:
    zope.interface.implements(IPostalInfo)
    def __init__(self,city,state):
	self.city, self.state = city, state


class Lookup:
    zope.interface.implements(IPostalLookup)
    _data = {
	'12345': ('Piliyandala', 'Western'),
        '12356': ('Galle', 'Southern'),
	'12367': ('Baticalo', 'Estern'),
	}
    def lookup(self,postal_code):
	data = self._data.get(postal_code)
	if(data):
	    return Info(*data)
