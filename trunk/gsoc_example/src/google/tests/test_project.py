import unittest
from zope.testing.doctestunit import DocTestSuite
from google.project import Project

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('google.project'),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest = 'test_suite')

