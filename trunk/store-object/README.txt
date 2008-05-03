
student.py, organization.py mentor.py, project.py represent simple class of Student, Organization, 
Mentor and Project.

google.py creates students, mentors, projects and set them to the organizations. It holds organizations.

retrieve.py stores a new project in the database and it will be stores in the database because it explicitly 
changed the dirty bit. (more details: http://www.zope.org/Wikis/ZODB/guide/node3.html)

But when it adds an additional mentor to the organization it won’t reflect in the database because I 
manually do not mark the dirty bit. 


print.py prints all objects in the database
