from . import Student

class Undergraduate(Student):

    def __init__(self, id: int, semester_name: str, registrationNo: str, Name: str):

        super().__init__(id, semester_name, registrationNo, Name)

    def enroll():
        pass

    def update():
        pass

    def __repr__(self):
        return f'This is a undergraduate student. student name: {super().__Name}, student registration no: {super().__registrationNo}'    
    
