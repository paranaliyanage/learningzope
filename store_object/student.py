#student.py - Class represents a GSoC student

from persistent import Persistent

class Student(Persistent):
    def __init__(self,id,name):
        self.id = id
        self.name = name