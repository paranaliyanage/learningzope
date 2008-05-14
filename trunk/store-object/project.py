#project.py - Class represnts a GSoC mentor

from persistent import Persistent

class Project(Persistent):
    def __init__(self,name,mentor,student):
        self.name = name
        self.mentor = mentor
        self.student = student
        
    def printYourself(self):
        print '\t Project name: ' + self.name
        print '\t Mentor name: ' + self.mentor.name
        print '\t Student name: ' + self.student.name
        
    