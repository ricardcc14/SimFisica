class Student:
    def __init__(self, name, id):   
        self.name = name
        self.id = id
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def average_grade(self):
        sum = 0
        for grade in self.grades.values():
            sum += grade
            average = sum / len(self.grades)
        return average

    def best_grades(self):
        best_indexs = [list(self.grades.keys())[i] for i, grade in enumerate(self.grades.values()) if grade >= 9]
        return best_indexs


    