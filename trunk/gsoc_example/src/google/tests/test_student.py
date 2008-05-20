import unittest
from zope.testing.doctestunit import DocTestSuite
from google.student import Student

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('google.student'),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest = 'test_suite')

