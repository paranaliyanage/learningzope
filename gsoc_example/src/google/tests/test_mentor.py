import unittest
from zope.testing.doctestunit import DocTestSuite
from google.mentor import Mentor

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('google.mentor'),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest = 'test_suite')

