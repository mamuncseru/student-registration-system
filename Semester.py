
from . import Course

class Semester:

    def __init__(self, id: int, name: str):

        self.id = id
        self.name = name
        
        
        self.courses = []

    def __repr__(self):
        return f'Semester info: \nt\Semester id: {self.id}, \n\tSemester name: {self.name}'\
            f'\n\t: Courses: {self.course_info()}'
    def freeze(self):
        pass

    def attend(self):
        pass

    def add_course(self, total_courses, course_ids, course_codes, course_titles):

        for i in range(total_courses):
            self.courses.append(Course(course_ids[i], course_codes[i], course_titles[i]))

    def course_info(self):
        if len(self.courses) == 0:
            return 'no courses added'

        else:
            for course in self.courses:
                return course


