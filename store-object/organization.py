#organization.py - Class represents GSoC Organization 

from persistent import Persistent
from persistent.list import PersistentList

class Organization(Persistent):
    def __init__(self, name):
        self.name = name;
        self.projects = PersistentList()
        self.otherMentors = []
        
    def addProject(self, project):
        self.projects.append(project)
        
    def addMentor(self,mentor):
        self.otherMentors.append(mentor)
        #self._p_changed = True
        
    def printYourself(self):
        print 'Organization name: '+ self.name
        print '    Projects:'
        for proj in self.projects:
            proj.printYourself()
            print ''
        if(self.otherMentors):
            print '    Other members: '
            for mentor in self.otherMentors:
                print '\t' + mentor.name
            