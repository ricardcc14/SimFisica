class Student:
    def __init__(self, name, id):   
        self.name = name
        self.id = id
        self.subjects = []

    def add_grade(self, subject, grade):
        self.subjects.append((subject, grade))

    def average_grade(self):
        sum = 0

        for i in self.subjects:
            sum += i[1]
            average = sum / len(self.subjects)
        return average
    