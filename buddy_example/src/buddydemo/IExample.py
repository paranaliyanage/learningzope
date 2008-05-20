from zope.interface import Interface, Attribute

class IExample(Interface):
    """This interfase represents a generic example"""

    text = Attribute("The text of the example")

    def setAttribute(text):
	"set the test"

    def getAttribute():
	"get the value"
