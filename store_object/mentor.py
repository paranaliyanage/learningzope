#mentor.py - Class represnts a GSoC mentor

from persistent import Persistent

class Mentor(Persistent):
    def __init__(self,id,name):
        self.id = id
        self.name = name