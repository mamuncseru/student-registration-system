
class Course:

    def __init__(self, id: int, courseTitle: str, courseCode: str):
        self._id = id
        self.courseTitle = courseTitle
        self.courseCode = courseCode

    def __repr__(self):
        return f'course info:\n\tid: {self._id} \n\tcourse title: {self.courseTitle} \n\tcourseCode: {self.courseCode}'

    def register(self):
        pass

    def drop(self):
        pass

    def withdraw(self):
        pass

# testing
ict = Course(1810, 'Information and Communication Engineering', 'ICT101')
print(ict)