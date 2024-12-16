import math
from datetime import date
from abc import ABC, abstractmethod

# Lớp trương trường hàm cơ sở
def round_number(number, decimals=2):
    return math.floor(number * 10**decimals) / 10**decimals

# Lớp trường Abstract ABC
class Person(ABC):
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)
        self.courses = []

    def describe(self):
        print(f"ID: {self.id}, Tên: {self.name}, Ngày sinh: {self.dob}")

    def add_course(self, course):
        self.courses.append(course)

    def list_courses(self):
        print(f"Khóa học của {self.name}:")
        for course in self.courses:
            print(f"{course['name']} (ID: {course['id']}), Tín chỉ: {course['credit']}, Điểm: {course['mark']}")

    def gpa(self):
        total_credits = sum(c['credit'] for c in self.courses)
        total_points = sum(c['mark'] * c['credit'] for c in self.courses)
        return round_number(total_points / total_credits) if total_credits > 0 else 0.0

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, id, name, dob):
        student = Student(id, name, dob)
        self.students.append(student)

    def list_students(self):
        print("Danh sách sinh viên:")
        for student in self.students:
            student.describe()
            print(f"GPA: {student.gpa()}\n")

    def list_student_courses(self, student_id):
        student = self.get_student_by_id(student_id)
        if student:
            student.list_courses()
        else:
            print("Không tìm thấy sinh viên!")

    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda s: s.gpa(), reverse=True)
        print("\nDanh sách sinh viên theo GPA giảm dần:")
        self.list_students()

    def input_student(self):
        id = input("Nhập ID sinh viên: ")
        name = input("Nhập tên sinh viên: ")
        dob = input("Nhập ngày sinh (yyyy-mm-dd): ")
        self.add_student(id, name, dob)

    def input_course_for_student(self):
        student_id = input("Nhập ID sinh viên: ")
        student = self.get_student_by_id(student_id)
        if not student:
            print("Sinh viên không tồn tại!")
            return
        
        course_id = input("Nhập ID khóa học: ")
        name = input("Nhập tên khóa học: ")
        credit = int(input("Nhập số tín chỉ: "))
        mark = float(input("Nhập điểm số: "))
        student.add_course({"id": course_id, "name": name, "credit": credit, "mark": mark})
        print("\nKhóa học đã được thêm!\n")

# Menu chính
def main():
    management = StudentManagement()
    
    while True:
        print("\n===== Chương trình Quản lý Sinh Viên =====")
        print("1. Thêm sinh viên")
        print("2. Thêm khóa học cho sinh viên")
        print("3. Hiển thị thông tin sinh viên")
        print("4. Xem danh sách khóa học của sinh viên")
        print("5. Sắp xếp sinh viên theo GPA")
        print("6. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            management.input_student()
        elif choice == "2":
            management.input_course_for_student()
        elif choice == "3":
            management.list_students()
        elif choice == "4":
            student_id = input("Nhập ID sinh viên: ")
            management.list_student_courses(student_id)
        elif choice == "5":
            management.sort_students_by_gpa()
        elif choice == "6":
            print("Kết thúc chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng thử lại.")

if __name__ == "__main__":
    main()
