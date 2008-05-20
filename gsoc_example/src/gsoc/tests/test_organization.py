import unittest
from zope.testing.doctestunit import DocTestSuite
from zope.app.container.tests.test_icontainer import TestSampleContainer

from gsoc.organization import Organization

class Test(TestSampleContainer):

    def makeTestObject(self):
        return Organization()

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('gsoc.organization'),
        unittest.makeSuite(Test),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest = 'test_suite')

