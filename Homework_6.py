class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

class Parent:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Parent):
     def rate_hw(self, student, course, grade_hw):
         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                    student.grades[course] += [grade_hw]
            else:
                    student.grades[course] = [grade_hw]
         else:
            return 'Ошибка'
class lecturer(Parent):
    def rate_lecture(self, student, course, grade_lecture):
        self.student = student
        self.course = course
        self.grade_lecture = grade_lecture
        self.courses_in_progress = []
        self.grades = {}
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade_lecture]
            else:
                student.grades[course] = [grade_lecture]
        else:
            return 'Ошибка'


best_lecturer = lecturer('Type', 'Function')
#best_lecturer.courses_in_progress += ['Python']

cool_lecturer = lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_lecturer.rate_lecture(best_lecturer, 'Python', 10)
cool_lecturer.rate_lecture(best_lecturer, 'Python', 10)
#cool_lecturer.rate_hw(best_lecturer, 'Python', 10)

print(best_lecturer.grades)




