#student.py - Class represents a GSoC student

from persistent import Persistent

class Student(Persistent):
    def __init__(self,name,organization):
        self.name = name
        self.organization = organization

