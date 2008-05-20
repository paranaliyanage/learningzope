from zope.interface import Interface
from zope.schema import Text, TextLine, Field

from zope.app.container.constraints import ContainerTypesConstraint, ItemTypePrecondition
from zope.app.container.interfaces import IContainer, IContained
from zope.app.file.interfaces import IFile

#may need this to be container
class IOrganization(Interface):
    """An Organization object. This contains projects, mentors and students"""
    
#    def __setitem__(name, object):
#        """Add students mentors and projects"""

    name=TextLine(
        title=u"Organization Name",
        description=u"Name of the organization",
        default=u"",
        required=True)

class IGsoc(IContainer):
    """This is the root object of this project. It can only caontain IOrganization objects"""

    def __setitem__(name, object):
        """Add a IOrganization object"""

    __setitem__.precondition = ItemTypePrecondition(IOrganization)

    description = Text(
        title=u"Description",
        description=u"A detailed description about the content on the Gsoc",
        default=u"",
        required=False)

class IOrganizationContained(IContained):
    """Interface that specifies type of objects that can contain in an organization"""
    
    __parent__ = Field(
        constraint = ContainerTypesConstraint(IGsoc))


class IOrganizationContainer(IContainer):
    """Organization is also a container for projects, students and mentors"""
    
    def __setitem__(name,object):
        """Add an ISudent, IProject and IMentor object"""

    __setitem__.precondition = ItemTypePrecondition(IFile)



