class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def enroll_course(self, course):
        if course.course_id not in self.courses:
            self.courses[course.course_id] = []

    def assign_grade(self, course, grade):
        if course.course_id in self.courses:
            self.courses[course.course_id].append(Grade(grade, course))
        else:
            print("Student is not enrolled in this course.")

    def calculate_gpa(self):
        total_grade_points = 0
        total_credits = 0

        for course_id, grades in self.courses.items():
            for grade in grades:
                total_grade_points += grade.grade * grade.course.credit
                total_credits += grade.course.credit

        if total_credits == 0:
            return 0
        else:
            return total_grade_points / total_credits


class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit


class Grade:
    def __init__(self, grade, course):
        self.grade = grade
        self.course = course



math_course = Course(1, "Math", 3)
physics_course = Course(2, "Physics", 4)


student1 = Student(101, "Alice")
student2 = Student(102, "Bob")


student1.enroll_course(math_course)
student1.enroll_course(physics_course)

student2.enroll_course(math_course)


student1.assign_grade(math_course, 85)
student1.assign_grade(physics_course, 90)

student2.assign_grade(math_course, 75)


print(f"{student1.name}'s GPA: {student1.calculate_gpa()}")
print(f"{student2.name}'s GPA: {student2.calculate_gpa()}")
