from . import Semester

class Student(Semester):
    def __init__(self, id: int, semister_name: str, registrationNo: str, Name: str):
        super().__(self, id, semister_name)
        self.__registrationNo = registrationNo
        self.__Name = Name

    def enroll(self):
        pass

    def __repr__(self):
        return f'student Name: {self.__Name}\n Student registration no: {self.__registrationNo}'



