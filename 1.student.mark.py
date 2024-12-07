
students = []
courses = []
marks = {}

# Nhập số lượng sinh viên
def input_number_of_students():
    while True:
        num_students = input("Số lượng sinh viên: ")
        if num_students.isdigit() and int(num_students) > 0:
            return int(num_students)
        else:
            print("Số lượng sinh viên phải là số nguyên dương!")

# Nhập thông tin sinh viên
def input_student_information():
    print("Nhập thông tin sinh viên:")
    student_id = input("  ID sinh viên: ")
    student_name = input("  Tên sinh viên: ")
    student_dob = input("  Ngày sinh (DD/MM/YYYY): ")
    students.append((student_id, student_name, student_dob))
    print(f"Đã thêm sinh viên: {student_name}")

# Nhập số lượng môn học
def input_number_of_courses():
    while True:
        num_courses = input("Số lượng môn học: ")
        if num_courses.isdigit() and int(num_courses) > 0:
            return int(num_courses)
        else:
            print("Số lượng môn học phải là số nguyên dương!")

# Nhập thông tin môn học
def input_course_information():
    print("Nhập thông tin môn học:")
    course_id = input("  ID môn học: ")
    course_name = input("  Tên môn học: ")
    courses.append((course_id, course_name))
    marks[course_id] = {}
    print(f"Đã thêm môn học: {course_name}")

# Nhập điểm cho môn học
def input_marks_for_course():
    if len(courses) == 0:
        print("Chưa có môn học nào. Thêm môn học trước đi!")
        return
    print("Danh sách môn học:")
    for c in courses:
        print(f"  {c[0]}: {c[1]}")
    course_id = input("Chọn ID môn học để nhập điểm: ")
    if course_id not in marks:
        print("ID môn học không hợp lệ!")
        return
    if len(students) == 0:
        print("Chưa có sinh viên nào. Thêm sinh viên trước đi!")
        return
    for s in students:
        while True:
            mark = input(f"Nhập điểm cho {s[1]}: ")
            try:
                mark = float(mark)
                if 0 <= mark <= 20:
                    marks[course_id][s[0]] = mark
                    break
                else:
                    print("Điểm phải từ 0 đến 20!")
            except:
                print("Điểm phải là số!")

# Xem danh sách môn học
def list_courses():
    if len(courses) == 0:
        print("Chưa có môn học nào!")
    else:
        print("Danh sách môn học:")
        for c in courses:
            print(f"  {c[0]}: {c[1]}")

# Xem danh sách sinh viên
def list_students():
    if len(students) == 0:
        print("Chưa có sinh viên nào!")
    else:
        print("Danh sách sinh viên:")
        for s in students:
            print(f"  {s[0]}: {s[1]}, Sinh ngày: {s[2]}")

# Xem điểm sinh viên theo môn học
def show_student_marks_for_course():
    if len(courses) == 0:
        print("Chưa có môn học nào!")
        return
    print("Danh sách môn học:")
    for c in courses:
        print(f"  {c[0]}: {c[1]}")
    course_id = input("Chọn ID môn học để xem điểm: ")
    if course_id not in marks:
        print("ID môn học không hợp lệ!")
        return
    if len(marks[course_id]) == 0:
        print("Chưa có điểm nào cho môn học này!")
    else:
        print(f"Điểm cho môn {course_id}:")
        for sid, mark in marks[course_id].items():
            name = next((s[1] for s in students if s[0] == sid), "Không rõ")
            print(f"  {name} ({sid}): {mark}")

# Menu chính
def main():
    while True:
        print("\nQuản lý điểm sinh viên:")
        print("1. Nhập số lượng sinh viên")
        print("2. Nhập thông tin sinh viên")
        print("3. Nhập số lượng môn học")
        print("4. Nhập thông tin môn học")
        print("5. Nhập điểm cho môn học")
        print("6. Xem danh sách môn học")
        print("7. Xem danh sách sinh viên")
        print("8. Xem điểm sinh viên theo môn học")
        print("9. Thoát")
        choice = input("Chọn: ")
        if choice == '1':
            for _ in range(input_number_of_students()):
                input_student_information()
        elif choice == '2':
            input_student_information()
        elif choice == '3':
            for _ in range(input_number_of_courses()):
                input_course_information()
        elif choice == '4':
            input_course_information()
        elif choice == '5':
            input_marks_for_course()
        elif choice == '6':
            list_courses()
        elif choice == '7':
            list_students()
        elif choice == '8':
            show_student_marks_for_course()
        elif choice == '9':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
