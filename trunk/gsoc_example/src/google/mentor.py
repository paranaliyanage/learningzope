# -*- coding: UTF-8 -*-
from zope.interface import implements
from zope.interface import Interface

from google.interfaces import IMentor

class Mentor(Interface):
    """A simple implementation of the gsoc mentor
    Make sure that the ‘‘Mentor‘‘ implements the ‘‘IMentor‘‘ interface:
    
    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IMentor, Mentor)
    True
    
    Here is an example of changing the name of the gsoc mentor:
    >>> mentor = Mentor()
    >>> mentor.name
    u''
    
    >>> mentor.name = u'Mentor Name'
    >>> mentor.name
    u'Mentor Name'
    """

    implements(IMentor)

    name = u''



