import unittest
from zope.testing.doctestunit import DocTestSuite
from zope.app.container.tests.test_icontainer import TestSampleContainer
from gsoc.gsoc import Gsoc

class Test(TestSampleContainer):

    def makeTestObject(self):
        return Gsoc()

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('gsoc.gsoc'),
        unittest.makeSuite(Test),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest = 'test_suite')

