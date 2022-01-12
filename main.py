class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def student_med_rate(self):
        st_med_rate = round(float(sum(self.grades.values()) / len(self.grades)), 1)
        return st_med_rate

    def __str__(self):
        some_student = f'Студент\n'
        some_student += f'Имя: {self.name}\n'
        some_student += f'Фамилия: {self.surname}\n'
        some_student += f'Средняя оценка за домашние задания: {self.student_med_rate()}\n'
        some_student += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        some_student += f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return some_student

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer class')
            return
        return self.student_med_rate() < other.lecturer_med_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def lecturer_med_rate(self):
        lec_med_rate = round(float(sum(self.grades.values()) / len(self.grades)), 1)
        return lec_med_rate

    def __str__(self):
        some_lecturer = f'Лектор\n'
        some_lecturer += f'Имя: {self.name}\n'
        some_lecturer += f'Фамилия: {self.surname}\n'
        some_lecturer += f'Средняя оценка за лекции: {self.lecturer_med_rate()}\n'
        return some_lecturer

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student class')
            return
        return self.lecturer_med_rate() < other.student_med_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Ревьюер\n'
        some_reviewer += f'Имя: {self.name}\n'
        some_reviewer += f'Фамилия: {self.surname}\n'
        return some_reviewer


student_1 = Student('Jimi', 'Hendrix', 'male')
student_1.finished_courses = ['Введение в програмирование', 'Git']
student_1.courses_in_progress = ['Python']
student_1.grades = {'Введение в програмирование': 9.2, 'Git': 8.7, 'Python': 9.8}

student_2 = Student('Mick', 'Jagger', 'male')
student_2.finished_courses = ['Введение в програмирование', 'Git']
student_2.courses_in_progress = ['Python']
student_2.grades = {'Введение в програмирование': 8.2, 'Git': 7.8, 'Python': 8.3}

lecturer_1 = Lecturer('Syd', 'Barret')
lecturer_1.courses_attached = ['Введение в програмирование', 'Git', 'Python']
lecturer_1.grades = {'Введение в програмирование': 9.2, 'Git': 9.7, 'Python': 9.9}

lecturer_2 = Lecturer('Robert', 'Smith')
lecturer_2.courses_attached = ['Введение в програмирование', 'Git', 'Python']
lecturer_2.grades = {'Введение в програмирование': 8.2, 'Git': 8.7, 'Python': 9.5}

reviewer_1 = Reviewer('Kurt', 'Cobain')
reviewer_1.courses_attached = ['Введение в програмирование', 'Git', 'Python']

reviewer_2 = Reviewer('James', 'Hatfield')
reviewer_2.courses_attached = ['Введение в програмирование', 'Git', 'Python']
student_courses_list_grades = [student_1.grades, student_2.grades]
lecturers_courses_list_grades = [lecturer_1.grades, lecturer_2.grades]


def get_st_avg_grade(course_name):
    sum_grade = 0
    for course in student_courses_list_grades:
        if course_name in course:
            sum_grade += course[course_name]
    return f'{course_name} = {round(sum_grade / len(student_courses_list_grades), 1)}'


def get_st_avg_grade_all():
    print('Средние оценки студентов по всем курсам:')
    print(get_st_avg_grade('Введение в програмирование'))
    print(get_st_avg_grade('Git'))
    print(f"{get_st_avg_grade('Python')}\n")


def get_lct_avg_grade(course_name):
    sum_grade = 0
    for course in lecturers_courses_list_grades:
        if course_name in course:
            sum_grade += course[course_name]
    return f'{course_name} = {round(sum_grade / len(lecturers_courses_list_grades), 1)}'


def get_lct_avg_grade_all():
    print('Средние оценки лекторов по всем курсам:')
    print(get_lct_avg_grade('Введение в програмирование'))
    print(get_lct_avg_grade('Git'))
    print(f"{get_lct_avg_grade('Python')}\n")


print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
print(f'{student_1 < lecturer_1}\n')
get_st_avg_grade_all()
get_lct_avg_grade_all()
