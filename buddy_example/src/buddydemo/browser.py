import zope.interface
from buddydemo.interfaces import IBuddy, IPostalInfo

class BuddyInfo:
    """Provides as interface for viewing a Buddy"""

    zope.interface.implements(IPostalInfo)
    __used_for__ = IBuddy

    def __init__(self, context, request):
	self.context = context
	self.request = request
	
	info = IPostalInfo(context)
	self.city, self.state = info.city, info.state
