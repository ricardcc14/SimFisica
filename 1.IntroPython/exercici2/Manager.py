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
    





