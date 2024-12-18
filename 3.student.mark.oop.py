import curses
import math


class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.courses = {}

    def add_course_mark(self, course_id, mark, credit):
        self.courses[course_id] = {"mark": mark, "credit": credit}

    def calculate_gpa(self):
        if not self.courses:
            return 0.0
        total_weighted_marks = sum(info["mark"] * info["credit"] for info in self.courses.values())
        total_credits = sum(info["credit"] for info in self.courses.values())
        return round(total_weighted_marks / total_credits, 1)

    def __str__(self):
        return f"{self.student_id}: {self.name}, Sinh ngày: {self.dob}"


class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit
        self.marks = {}

    def add_mark(self, student_id, mark):
        self.marks[student_id] = mark

    def __str__(self):
        return f"{self.course_id}: {self.name} (Tín chỉ: {self.credit})"


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                print("Giá trị phải là số nguyên dương!")
            except ValueError:
                print("Giá trị không hợp lệ. Hãy nhập lại!")

    def add_student(self):
        curses.endwin()
        print("\nNhập thông tin sinh viên:")
        student_id = input("ID sinh viên: ")
        name = input("Tên sinh viên: ")
        dob = input("Ngày sinh (DD/MM/YYYY): ")
        self.students.append(Student(student_id, name, dob))
        print(f"Đã thêm sinh viên: {name}")
        input("Nhấn Enter để quay lại menu...")
        curses.doupdate()

    def add_course(self):
        curses.endwin()
        print("\nNhập thông tin môn học:")
        course_id = input("ID môn học: ")
        name = input("Tên môn học: ")
        credit = self.input_number("Số tín chỉ: ")
        self.courses.append(Course(course_id, name, credit))
        print(f"Đã thêm môn học: {name}")
        input("Nhấn Enter để quay lại menu...")
        curses.doupdate()

    def input_marks(self):
        if not self.courses:
            curses.endwin()
            print("Chưa có môn học nào. Thêm môn học trước đi!")
            input("Nhấn Enter để quay lại menu...")
            curses.doupdate()
            return
        if not self.students:
            curses.endwin()
            print("Chưa có sinh viên nào. Thêm sinh viên trước đi!")
            input("Nhấn Enter để quay lại menu...")
            curses.doupdate()
            return

        curses.endwin()
        print("\nDanh sách môn học:")
        for course in self.courses:
            print(course)

        course_id = input("Chọn ID môn học để nhập điểm: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print("ID môn học không hợp lệ!")
            input("Nhấn Enter để quay lại menu...")
            curses.doupdate()
            return

        for student in self.students:
            while True:
                try:
                    mark = float(input(f"Nhập điểm cho {student.name}: "))
                    mark = math.floor(mark * 10) / 10  # Làm tròn xuống 1 chữ số thập phân
                    if 0 <= mark <= 20:
                        course.add_mark(student.student_id, mark)
                        student.add_course_mark(course_id, mark, course.credit)
                        break
                    else:
                        print("Điểm phải từ 0 đến 20!")
                except ValueError:
                    print("Điểm phải là số!")
        input("Nhấn Enter để quay lại menu...")
        curses.doupdate()

    def calculate_gpa(self, stdscr):
        if not self.students:
            stdscr.addstr(0, 0, "Chưa có sinh viên nào!")
            stdscr.refresh()
            stdscr.getch()
            return

        stdscr.clear()
        stdscr.addstr(0, 0, "Bảng điểm GPA của sinh viên:")
        for i, student in enumerate(self.students, start=1):
            gpa = student.calculate_gpa()
            stdscr.addstr(i, 0, f"{student.name} ({student.student_id}): GPA = {gpa}")
        stdscr.refresh()
        stdscr.getch()

    def sort_students_by_gpa(self, stdscr):
        if not self.students:
            stdscr.addstr(0, 0, "Chưa có sinh viên nào!")
            stdscr.refresh()
            stdscr.getch()
            return

        sorted_students = sorted(self.students, key=lambda s: s.calculate_gpa(), reverse=True)
        stdscr.clear()
        stdscr.addstr(0, 0, "Danh sách sinh viên theo GPA (giảm dần):")
        for i, student in enumerate(sorted_students, start=1):
            stdscr.addstr(i, 0, f"{student.name} ({student.student_id}): GPA = {student.calculate_gpa()}")
        stdscr.refresh()
        stdscr.getch()

    def list_students(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Danh sách sinh viên:")
        for i, student in enumerate(self.students, start=1):
            stdscr.addstr(i, 0, str(student))
        stdscr.refresh()
        stdscr.getch()

    def list_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Danh sách môn học:")
        for i, course in enumerate(self.courses, start=1):
            stdscr.addstr(i, 0, str(course))
        stdscr.refresh()
        stdscr.getch()

    def main_menu(self, stdscr):
        curses.curs_set(0)  # Ẩn con trỏ
        current_row = 0
        menu = [
            "Nhập thông tin sinh viên",
            "Nhập thông tin môn học",
            "Nhập điểm cho môn học",
            "Tính GPA của sinh viên",
            "Sắp xếp sinh viên theo GPA",
            "Xem danh sách sinh viên",
            "Xem danh sách môn học",
            "Thoát",
        ]

        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Quản lý điểm sinh viên:")

            # Hiển thị menu
            for i, option in enumerate(menu):
                if i == current_row:
                    stdscr.addstr(i + 1, 0, f"> {option}", curses.A_REVERSE)
                else:
                    stdscr.addstr(i + 1, 0, f"  {option}")

            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                # Thực hiện lựa chọn
                if current_row == 0:
                    self.add_student()
                elif current_row == 1:
                    self.add_course()
                elif current_row == 2:
                    self.input_marks()
                elif current_row == 3:
                    self.calculate_gpa(stdscr)
                elif current_row == 4:
                    self.sort_students_by_gpa(stdscr)
                elif current_row == 5:
                    self.list_students(stdscr)
                elif current_row == 6:
                    self.list_courses(stdscr)
                elif current_row == 7:
                    break

            stdscr.refresh()


if __name__ == "__main__":
    sms = StudentManagementSystem()
    curses.wrapper(sms.main_menu)
