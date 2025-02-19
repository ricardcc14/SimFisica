from Student import Student

class GraduateStudent(Student):
    def __init__(self, name, id):
        super().__init__(name, id)

    def set_thesis_title(self, title):
        self.thesis = title
    
