class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"{self.student_id}: {self.name}, Sinh ngày: {self.dob}"


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.marks = {}

    def add_mark(self, student_id, mark):
        self.marks[student_id] = mark

    def get_marks(self):
        return self.marks

    def __str__(self):
        return f"{self.course_id}: {self.name}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number(self, prompt):
        while True:
            value = input(prompt)
            if value.isdigit() and int(value) > 0:
                return int(value)
            print("Giá trị phải là số nguyên dương!")

    def add_student(self):
        print("Nhập thông tin sinh viên:")
        student_id = input("  ID sinh viên: ")
        name = input("  Tên sinh viên: ")
        dob = input("  Ngày sinh (DD/MM/YYYY): ")
        self.students.append(Student(student_id, name, dob))
        print(f"Đã thêm sinh viên: {name}")

    def add_course(self):
        print("Nhập thông tin môn học:")
        course_id = input("  ID môn học: ")
        name = input("  Tên môn học: ")
        self.courses.append(Course(course_id, name))
        print(f"Đã thêm môn học: {name}")

    def input_marks(self):
        if not self.courses:
            print("Chưa có môn học nào. Thêm môn học trước đi!")
            return

        print("Danh sách môn học:")
        for course in self.courses:
            print(course)

        course_id = input("Chọn ID môn học để nhập điểm: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print("ID môn học không hợp lệ!")
            return

        if not self.students:
            print("Chưa có sinh viên nào. Thêm sinh viên trước đi!")
            return

        for student in self.students:
            while True:
                try:
                    mark = float(input(f"Nhập điểm cho {student.name}: "))
                    if 0 <= mark <= 20:
                        course.add_mark(student.student_id, mark)
                        break
                    else:
                        print("Điểm phải từ 0 đến 20!")
                except ValueError:
                    print("Điểm phải là số!")

    def list_students(self):
        if not self.students:
            print("Chưa có sinh viên nào!")
        else:
            print("Danh sách sinh viên:")
            for student in self.students:
                print(student)

    def list_courses(self):
        if not self.courses:
            print("Chưa có môn học nào!")
        else:
            print("Danh sách môn học:")
            for course in self.courses:
                print(course)

    def show_marks(self):
        if not self.courses:
            print("Chưa có môn học nào!")
            return

        print("Danh sách môn học:")
        for course in self.courses:
            print(course)

        course_id = input("Chọn ID môn học để xem điểm: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print("ID môn học không hợp lệ!")
            return

        marks = course.get_marks()
        if not marks:
            print("Chưa có điểm nào cho môn học này!")
        else:
            print(f"Điểm cho môn {course.name}:")
            for student_id, mark in marks.items():
                student = next((s for s in self.students if s.student_id == student_id), None)
                name = student.name if student else "Không rõ"
                print(f"  {name} ({student_id}): {mark}")

    def main_menu(self):
        while True:
            try:
                print("\nQuản lý điểm sinh viên:")
                print("1. Nhập thông tin sinh viên")
                print("2. Nhập thông tin môn học")
                print("3. Nhập điểm cho môn học")
                print("4. Xem danh sách sinh viên")
                print("5. Xem danh sách môn học")
                print("6. Xem điểm sinh viên theo môn học")
                print("7. Thoát")

                choice = input("Chọn: ")
                if choice == '1':
                    self.add_student()
                elif choice == '2':
                    self.add_course()
                elif choice == '3':
                    self.input_marks()
                elif choice == '4':
                    self.list_students()
                elif choice == '5':
                    self.list_courses()
                elif choice == '6':
                    self.show_marks()
                elif choice == '7':
                    print("Tạm biệt!")
                    break
                else:
                    print("Lựa chọn không hợp lệ!")
            except IOError as e:
                print(f"Lỗi I/O: {e}")
            except Exception as e:
                print(f"Đã xảy ra lỗi: {e}")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.main_menu()
