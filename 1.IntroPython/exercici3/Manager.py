import numpy as np
from Student import Student

class Manager:
    def __init__(self):   
        self.students = {}
    
    def add_student(self, student):
        self.students[student.id] = student
    
    def average_student_grade(self): 
        sum = 0
        for id in self.students.keys():
            sum += self.students[id].average_grade()
        average = sum / len(self.students)
        
        return average
    
    def grades_statistics(self):
        all_grades = []
        for id in self.students.keys():
            for grade in self.students[id].grades.values():
                all_grades.append(grade)
        print("Student statistics:")
        print("Median: " + str(np.median(all_grades)))
        print("Standard deviation: " + str(np.std(all_grades)))




