
student.py, organization.py mentor.py, project.py represent simple class of Student, Organization, 
Mentor and Project.

google.py creates students, mentors, projects and set them to the organizations. It holds organizations.

retrieve.py stores a new project in the database and it will be stores in the database because it uses a PersistentList. 
But for the other mentors I use a simple list. To store this you need to set the dirty bit. I have commented it.
Uncomment it and see the different. On the other hand you can still get the same results by making the otherMentors as 
a PersistentList.
(more details: http://www.zope.org/Wikis/ZODB/guide/node3.html)

But when it adds an additional mentor to the organization it won’t reflect in the database because I 
manually do not mark the dirty bit. 


print.py prints all objects in the database
