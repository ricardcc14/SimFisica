# EXERCICI 1: Simulació Física
from Student import Student
from GraduateStudent import GraduateStudent

alice = Student("Alice", 9)
alice.add_grade("Maths", 9)
alice.add_grade("Programming", 8.5)

bob = GraduateStudent("Bob", 2)
bob.set_thesis_title("AI in physics simulation")
bob.add_grade("Maths", 9.5)
bob.add_grade("Programming", 9)

def print_student_average(student):
    print(student.name + " average grades are: " + str(student.average_grade())) 
    if (hasattr(student, "thesis")):
        print(student.name + " thesis title: " + student.thesis) 
    print()

print_student_average(alice)
print_student_average(bob)





    
        
  

