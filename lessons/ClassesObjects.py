//Classes are code templates for creating objects. They set the basic variables and functions that its objects have.

class Person:
  def __init__(self,firstname, lastname, age, job):
    self.firstname = firstname
    self.lastname = lastname
    self.age = int(age)
    self.job = job
  
  def name(self):
    return ""+self.firstname+", "+ self.lastname


aperson = Person("John", "Smith", 9, "Teacher")
print(aperson.name())
print(aperson.job)


