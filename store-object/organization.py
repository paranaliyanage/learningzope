#organization.py - Class represents GSoC Organization 

from persistent import Persistent

class Organization(Persistent):
    def __init__(self, name):
        self.name = name;
        