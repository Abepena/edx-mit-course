import datetime

class Person:
    def __init__(self,name):
        self.name = name
        self.birthday = None
        self.last_name = name.split(' ')[-1] #assumes name will be a string of first and last name 
    def get_last_name(self):
        """ return self's last name"""
        return self.last_name
    def set_birthday(self,month,day,year):
        self.birthday = datetime.date(year,month,day)
    def get_age(self):
        """returns self's current age in date"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday.days)
    def __lt__(self,other):
        """
        returns True of self's name is lexigraphically
        less than other's last name and False otherwise
        """
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name
    def __str__(self):
        """return self's name"""
        return self.name
    

class MITPerson(Person):
    next_id_num = 0 #next id number to assign
    
    def __init__(self,name):
        Person.__init__(self,name) #initializing Person attributes
        self.id_num = MITPerson.next_id_num #MITPerson attr, unique id
        MITPerson.next_id_num += 1
        
    def get_id_num(self):
        return str(self.id_num).zfill(3)
    
    #sorting MIT people by id number
    def __lt__(self,other):
        return self.id_num < other.id_num
    
    def speak(self,utterance):
          return ("{} says {}".format(self.name, utterance))

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self,name,class_year):
        MITPerson.__init__(self,name)
        self.year = class_year
        
    def get_class(self):
        return self.year
    
    def speak(self, utterance):
        new = MITPerson.speak(self,"Dude {}".format(utterance))
        return new

        return(MITPerson.speak(self,new))
class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def is_student(obj):
    return isinstance(obj,Student)

class Professor(MITPerson):
    def __init__(self,name,department):
        MITPerson.__init__(self,name)
        self.department = department
    
    def speak(self):
        new = "In course {} we say".format(self.department)
        return MITPerson.speak(new + utterance)
    
    def lecture(self,topic):
        return self.speak('it is obvious that' + topic)
        

class Grades:
    """
    A mapping from students to a list of grades
    """
    
    def __init__(self):
        """
        Create an empty gradebook
        """
        self.students = [] # list of Student objects
        self.grades = {} # maps idNum --> list of grades
        self.is_sorted = True
    
    def add_student(self, student):
        """
        Assumes: student is of type Student
        Add student to the gradebook
        """
        
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.get_id_num()] = []
        self.is_sorted = False
    
    def add_grade(self, student, grade):
        """
        Assumes grade is a float
        Add grade to the list of grades for student
        """
        try:
            self.grades[student.get_id_num()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
        
    def get_grades(self,student):
        """Return a list of grades for a student"""
        try:
            return self.grades[student.get_id_num()][:] #returns a copy of student grades
        except KeyError:
            raise ValueError('Student not in grade book')
    
    def all_students(self):
        """Return a list of all students in grade book"""
        if not self.is_sorted:
            self.students.sort()
            self.is_sorted = True
        return self.students[:]
        #returning a copy of students so we dont accidentally
        # destroy the underlying list stored inside of the instance
        

def grade_report(course):
    """Assumes: course is of type Grades"""
    report = []
    for s in course.all_students():
        tot = 0.0
        num_grades = 0
        for g in course.get_grades(s):
            tot += g
            num_grades += 1
        try:
            average = tot/num_grades
            report.append(f"{str(s)}'s mean grade is {average}")
        except ZeroDivisionError:
            report.append(f"{str(s)} has no grades")
        
    return "\n".join(report)

ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

six00 = Grades()
six00.add_student(g1)
six00.add_student(ug2)
six00.add_student(ug1)
six00.add_student(g2)
six00.add_student(ug4)
six00.add_student(ug3)

print(grade_report(six00))

