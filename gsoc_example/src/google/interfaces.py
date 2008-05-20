from zope.interface import Interface
from zope.schema import Text, TextLine, Field
from zope.i18nmessageid import MessageFactory
from zope.app.container.constraints import ContainerTypesConstraint, ItemTypePrecondition
from zope.app.container.interfaces import IContainer, IContained
from zope.app.file.interfaces import IFile
_ = MessageFactory("google")

class IProject(Interface):
    """A Project object."""

    name = TextLine(title=_("Project Name"))
#    name=TextLine(
#        title=u"Project Name",
#        description=u"Name of the project",
#        default=u"",
#        required=True)
    
#    description=TextLine(
#        title=u"Project Description",
#        description=u"Detailed description about the project",
#        default=u"",
#        required=False)



class IStudent(Interface):
    """A Student object"""

    name = TextLine(title=_("Student Name"))

#    name=TextLine(
#        title=u"Student's Name",
#        description=u"Name of the student",
#        default=u"",
#        required=True)


class IMentor(Interface):
    """A Mentor object"""

    name = TextLine(title=_("Mentor Name"))

#    name=TextLine(
#        title=u"Mentor's Name",
#        description=u"Name of the student",
#        default=u"",
#        required=True)


class IOrganization(IContainer):
    """An Organization object. This contains projects, mentors and students"""
    
    def __setitem__(name, object):
        """Add students mentors and projects"""

    __setitem__.precondition = ItemTypePrecondition(IProject, IStudent, IMentor)

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
        """Add an IStudent, IProject and IMentor object"""

    __setitem__.precondition = ItemTypePrecondition(IProject,IStudent, IMentor)



