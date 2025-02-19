# EXERCICI 2: Simulació Física
from Student import Student
from GraduateStudent import GraduateStudent
from Manager import Manager

students_manager = Manager()

alice = Student("Alice", 9)
alice.add_grade("Maths", 9)
alice.add_grade("Programming", 8.5)
students_manager.add_student(alice)

bob = GraduateStudent("Bob", 2)
bob.set_thesis_title("AI in physics simulation")
bob.add_grade("Maths", 9.5)
bob.add_grade("Programming", 9)
students_manager.add_student(bob)

for id in students_manager.students.keys():
    print(students_manager.students[id].name + " average grades are: " + str(students_manager.students[id].average_grade())) 
    if (hasattr(students_manager.students[id], "thesis")):
        print(students_manager.students[id].name + " thesis title: " + students_manager.students[id].thesis) 

    print(students_manager.students[id].name + " best grades:")
    best_subjects = students_manager.students[id].best_grades()
    for subject in best_subjects:
        print("Subject: " + subject + ", Grade: " + str(students_manager.students[id].grades[subject]))
    print()

print("Students average grade: %.1f" % round(students_manager.average_student_grade(), 1))       
            



