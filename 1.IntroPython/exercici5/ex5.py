# EXERCICI 5: Simulació Física
import json
from Student import Student
from GraduateStudent import GraduateStudent
from Manager import Manager

students_manager = Manager()

with open('./exercici5/students.json', 'r') as file:
    data = json.load(file)
    for student_json in data:
        student = Student(student_json["name"], student_json["id"])
        for subject in student_json["subjects"]:
            student.add_grade(subject["class"], subject["grade"])
        students_manager.add_student(student)

alice = Student("Alice", len(students_manager.students) + 1)
alice.add_grade("Maths", 9)
alice.add_grade("Programming", 8.5)
students_manager.add_student(alice)

bob = GraduateStudent("Bob", len(students_manager.students) + 2)
bob.set_thesis_title("AI in physics simulation")
bob.add_grade("Maths", 9.5)
bob.add_grade("Programming", 9)
students_manager.add_student(bob)        

for id in students_manager.students.keys():
    if (students_manager.students[id].name == "Alice" or students_manager.students[id].name == "Bob"):
        print(students_manager.students[id].name + " average grades are: " + str(students_manager.students[id].average_grade())) 
        if (hasattr(students_manager.students[id], "thesis")):
            print(students_manager.students[id].name + " thesis title: " + students_manager.students[id].thesis) 

        print(students_manager.students[id].name + " best grades:")
        best_subjects = students_manager.students[id].best_grades()
        for subject in best_subjects:
            print("Subject: " + subject + ", Grade: " + str(students_manager.students[id].grades[subject]))
        print()

print("Students average grade: " + str(students_manager.average_student_grade()))       
            
students_manager.grades_statistics() 
students_manager.show_graph_grades()
students_manager.show_correlation()