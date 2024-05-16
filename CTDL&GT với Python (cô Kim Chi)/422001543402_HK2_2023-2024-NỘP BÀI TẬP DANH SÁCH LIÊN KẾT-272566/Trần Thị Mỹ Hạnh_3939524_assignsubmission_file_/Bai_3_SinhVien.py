class SinhVien:
    def __init__(self, masv, ten_sv, mon_hoc, diem):
        self.masv = masv
        self.ten_sv = ten_sv
        self.mon_hoc = mon_hoc
        self.diem = diem

    def __repr__(self):
        return f"Student(MaSV: {self.masv}, TenSV: {self.ten_sv}, MonHoc: {self.mon_hoc}, Diem: {self.diem})"

class DSLK_SinhVien:
    def __init__(self):
        self.head = None

    def append(self, student):
        new_node = Node(student)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def sort_by_score(self):
        if not self.head or not self.head.next:
            return

        current = self.head.next
        self.head.next = None
        while current:
            next_node = current.next
            self.insert_sorted(current)
            current = next_node

    def insert_sorted(self, new_node):
        if not self.head or self.head.data.diem >= new_node.data.diem:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data.diem < new_node.data.diem:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insert_sorted_and_reorder(self, student):
        self.append(student)
        self.sort_by_score()

    def students_with_score_greater_than(self, x):
        result = DSLK_SinhVien()
        current = self.head
        while current:
            if current.data.diem > x:
                result.append(current.data)
            current = current.next
        return result

    def find_k_students_with_highest_score(self, k):
        result = DSLK_SinhVien()
        current = self.head
        scores = []
        while current:
            scores.append(current.data.diem)
            current = current.next
        scores.sort(reverse=True)
        current = self.head
        count = 0
        while current and count < k:
            if current.data.diem in scores[:k]:
                result.append(current.data)
                count += 1
            current = current.next
        return result

    def remove_students_with_score_less_than(self, x):
        current = self.head
        prev = None
        while current:
            if current.data.diem < x:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
            else:
                prev = current
            current = current.next

    def merge(self, other_list):
        current = other_list.head
        while current:
            self.append(current.data)
            current = current.next

    def print_students(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            current = self.head
            while current:
                file.write(f"{current.data.masv}, {current.data.ten_sv}, {current.data.mon_hoc}, {current.data.diem}\n")
                current = current.next


# Hàm main
def main():
    student_list = DSLK_SinhVien()

    # Thêm sinh viên vào danh sách
    student1 = SinhVien("SV001", "Nguyen Van A", "Toan", 8.5)
    student2 = SinhVien("SV002", "Tran Thi B", "Van", 7.2)
    student3 = SinhVien("SV003", "Le Van C", "Anh", 9.0)

    student_list.append(student1)
    student_list.append(student2)
    student_list.append(student3)

    while True:
        print("\nMenu:")
        print("1. Chèn một học sinh mới vào danh sách cuối cùng.")
        print("2. Sắp xếp danh sách theo thứ tự tăng dần của Điểm.")
        print("3. Chèn một học sinh mới vào danh sách đã sắp xếp để có danh sách cũng đã sắp xếp.")
        print("4. Lấy danh sách sinh viên có Điểm lớn hơn x.")
        print("5. Tìm kiếm k sinh viên có Điểm cao nhất.")
        print("6. Loại bỏ tất cả sinh viên có Điểm nhỏ hơn x.")
        print("7. Hợp nhất vào danh sách sinh viên.")
        print("8. In ra màn hình danh sách sinh viên.")
        print("9. Ghi danh sách học sinh ra file txt.")
        print("0. Thoát chương trình.")

        choice = int(input("Chọn chức năng: "))

        if choice == 1:
            masv = input("Nhập Mã SV: ")
            ten_sv = input("Nhập Tên SV: ")
            mon_hoc = input("Nhập Môn Học: ")
            diem = float(input("Nhập Điểm: "))
            new_student = SinhVien(masv, ten_sv, mon_hoc, diem)
            student_list.append(new_student)
        elif choice == 2:
            student_list.sort_by_score()
        elif choice == 3:
            masv = input("Nhập Mã SV: ")
            ten_sv = input("Nhập Tên SV: ")
            mon_hoc = input("Nhập Môn Học: ")
            diem = float(input("Nhập Điểm: "))
            new_student = SinhVien(masv, ten_sv, mon_hoc, diem)
            student_list.insert_sorted_and_reorder(new_student)
        elif choice == 4:
            x = float(input("Nhập x: "))
            students_with_higher_score = student_list.students_with_score_greater_than(x)
            print("Danh sách sinh viên có Điểm lớn hơn", x, ":")
            students_with_higher_score.print_students()
        elif choice == 5:
            k = int(input("Nhập k: "))
            k_students_with_highest_score = student_list.find_k_students_with_highest_score(k)
            print("Danh sách", k, "sinh viên có Điểm cao nhất:")
            k_students_with_highest_score.print_students()
        elif choice == 6:
            x = float(input("Nhập x: "))
            student_list.remove_students_with_score_less_than(x)
            print("Đã loại bỏ tất cả sinh viên có Điểm nhỏ hơn", x)
        elif choice == 7:
            # Tạo danh sách sinh viên mới
            new_student_list = DSLK_SinhVien()
            new_student1 = SinhVien("SV004", "Pham Van D", "Ly", 8.7)
            new_student2 = SinhVien("SV005", "Hoang Thi E", "Sinh", 9.5)
            new_student_list.append(new_student1)
            new_student_list.append(new_student2)

            # Hợp nhất danh sách mới vào danh sách hiện tại
            student_list.merge(new_student_list)
            print("Đã hợp nhất danh sách sinh viên mới vào danh sách hiện tại")
        elif choice == 8:
            print("Danh sách sinh viên:")
            student_list.print_students()
        elif choice == 9:
            filename = input("Nhập tên file txt muốn ghi: ")
            student_list.write_to_file(filename)
            print(f"Đã ghi danh sách sinh viên ra file {filename}.")
        elif choice == 0:
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()