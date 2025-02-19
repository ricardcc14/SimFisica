import numpy as np
import matplotlib.pyplot as plt
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


    def show_graph_grades(self):
        all_grades = []
        for id in self.students.keys():
            for grade in self.students[id].grades.values():
                all_grades.append(grade)
        plt.hist(all_grades, bins=20, histtype="bar")
        plt.title('Grade Distribution')
        plt.xlabel('Grade')
        plt.xlim(0, 10)
        plt.ylabel('Frequency')
        plt.show()

    def show_correlation(self):
        maths_grades = []
        prog_grades = []
        for id in self.students.keys():
            maths_grades.append(self.students[id].grades["Maths"])
            prog_grades.append(self.students[id].grades["Programming"])

        plt.scatter(maths_grades, prog_grades)
        plt.title('Grade Distribution')
        plt.xlabel('Math')
        plt.xlim(0, 10)
        plt.ylabel('Programming')
        plt.ylim(0, 10)
        plt.show()
       






