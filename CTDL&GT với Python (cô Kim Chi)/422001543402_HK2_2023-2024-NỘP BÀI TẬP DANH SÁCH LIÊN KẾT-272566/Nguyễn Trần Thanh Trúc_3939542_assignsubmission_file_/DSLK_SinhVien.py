class SinhVien:
    def __init__(self, masv, ten_sv, mon_hoc, diem):
        self.masv = masv
        self.ten_sv = ten_sv
        self.mon_hoc = mon_hoc
        self.diem = diem
        self.next = None

class DanhSachSinhVien:
    def __init__(self):
        self.head = None

    def chen_sinh_vien_cuoi_cung(self, sinh_vien):
        if not self.head:
            self.head = sinh_vien
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = sinh_vien

    def sap_xep_theo_diem(self):
        if not self.head or not self.head.next:
            return

        def merge_sort(head):
            if not head or not head.next:
                return head

            middle = self._find_middle(head)
            second_half = middle.next
            middle.next = None

            left = merge_sort(head)
            right = merge_sort(second_half)

            return self._merge(left, right)

        self.head = merge_sort(self.head)

    def _find_middle(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.diem < right.diem:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)

        return result

    def chen_sinh_vien_sap_xep(self, sinh_vien):
        self.sap_xep_theo_diem()
        self.chen_sinh_vien_cuoi_cung(sinh_vien)
        self.sap_xep_theo_diem()

    def lay_sinh_vien_diem_lon_hon(self, x):
        result = []
        current = self.head

        while current:
            if current.diem > x:
                result.append((current.masv, current.ten_sv, current.mon_hoc, current.diem))
            current = current.next

        return result

    def tim_k_sinh_vien_diem_cao_nhat(self, k):
        result = []
        current = self.head

        while current and k > 0:
            result.append((current.masv, current.ten_sv, current.mon_hoc, current.diem))
            current = current.next
            k -= 1

        return result

    def loai_bo_sinh_vien_diem_nho_hon(self, x):
        current = self.head
        prev = None

        while current:
            if current.diem < x:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
            else:
                prev = current
            current = current.next

    def hop_nhat_danh_sach(self, danh_sach_khac):
        current = self.head
        while current.next:
            current = current.next
        current.next = danh_sach_khac.head

    def in_danh_sach(self):
        current = self.head
        while current:
            print(f"MaSV: {current.masv}, TenSV: {current.ten_sv}, MonHoc: {current.mon_hoc}, Diem: {current.diem}")
            current = current.next

    def ghi_vao_file_txt(self, filename):
        with open(filename, 'w') as file:
            current = self.head
            while current:
                file.write(f"{current.masv} {current.ten_sv} {current.mon_hoc} {current.diem}\n")
                current = current.next

# Hàm chính
def main():
    danh_sach_sv = DanhSachSinhVien()

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

        choice = input("Chọn chức năng (0-9): ")

        if choice == '1':
            masv = input("Nhập Mã sinh viên: ")
            ten_sv = input("Nhập Tên sinh viên: ")
            mon_hoc = input("Nhập Môn học: ")
            diem = float(input("Nhập Điểm: "))
            sinh_vien = SinhVien(masv, ten_sv, mon_hoc, diem)
            danh_sach_sv.chen_sinh_vien_cuoi_cung(sinh_vien)

        elif choice == '2':
            danh_sach_sv.sap_xep_theo_diem()
            print("Danh sách sinh viên sau khi sắp xếp theo điểm là: ")
            danh_sach_sv.in_danh_sach()

        elif choice == '3':
            masv = input("Nhập Mã sinh viên: ")
            ten_sv = input("Nhập Tên sinh viên: ")
            mon_hoc = input("Nhập Môn học: ")
            diem = float(input("Nhập Điểm: "))
            sinh_vien = SinhVien(masv, ten_sv, mon_hoc, diem)
            danh_sach_sv.chen_sinh_vien_sap_xep(sinh_vien)
            danh_sach_sv.sap_xep_theo_diem()  # Thêm dòng này để đảm bảo danh sách vẫn được sắp xếp sau khi chèn mới
            print("Danh sách sinh viên sau khi chèn và sắp xếp: ")
            danh_sach_sv.in_danh_sach()


        elif choice == '4':
            x = float(input("Nhập giá trị x: "))
            result = danh_sach_sv.lay_sinh_vien_diem_lon_hon(x)
            print(result)

        elif choice == '5':
            k = int(input("Nhập số sinh viên cần tìm: "))
            result = danh_sach_sv.tim_k_sinh_vien_diem_cao_nhat(k)
            print(result)

        elif choice == '6':
            x = float(input("Nhập giá trị x: "))
            danh_sach_sv.loai_bo_sinh_vien_diem_nho_hon(x)

        elif choice == '7':
            danh_sach_khac = DanhSachSinhVien()
            # Thêm sinh viên vào danh_sach_khac tương tự như chức năng 1
            danh_sach_sv.hop_nhat_danh_sach(danh_sach_khac)

        elif choice == '8':
            danh_sach_sv.in_danh_sach()

        elif choice == '9':
            filename = input("Nhập tên file txt: ")
            danh_sach_sv.ghi_vao_file_txt(filename)

        elif choice == '0':
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
