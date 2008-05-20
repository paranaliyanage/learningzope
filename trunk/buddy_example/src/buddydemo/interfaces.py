import re, zope.interface
from zope.schema import Text, TextLine
from zope.i18nmessageid import MessageFactory
_ = MessageFactory("buddydemo")

class IBuddy(zope.interface.Interface):
    """Provides access to basic buddy information"""

    first = TextLine(title=_("First name"))
    last = TextLine(title=_("Last name"))
    email = TextLine(title=_("Electronic mail address"))
    address = Text(title=_("Postal address"))
    postal_code = TextLine(title=_("Postal code"),
       constraint=re.compile("\d{5,5}(-\d{4,4})?$").match)

    def name():
        """Gets the buddy name.

        The buddy name is the first and last name"""



class IPostalInfo(zope.interface.Interface):
    """Provide information for postal codes"""

    city=TextLine(title=u"City")
    state=TextLine(title=u"State")
    

class IPostalLookup(zope.interface.Interface):
    """Provides postal code lookups"""

    def lookup(postal_code):
	"""Lookup information for a postal code.
	An IPostalInfo is returned if the postal
	code is known. None is returned otherwise.
	"""

