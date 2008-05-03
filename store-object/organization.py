#organization.py - Class represents GSoC Organization 

from persistent import Persistent

class Organization(Persistent):
    def __init__(self, name):
        self.name = name;
        self.projects = []
        self.otherMentors = []
        
    def addProject(self, project):
        self.projects.append(project)
        self._p_changed = True
        
    def addMentor(self,mentor):
        self.otherMentors.append(mentor)
        #need to handle self._p_changed = True