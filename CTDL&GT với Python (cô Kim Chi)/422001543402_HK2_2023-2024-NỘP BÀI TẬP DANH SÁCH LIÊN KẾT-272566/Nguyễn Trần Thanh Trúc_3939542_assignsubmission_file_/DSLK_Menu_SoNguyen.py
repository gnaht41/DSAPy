class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DSLienKetDon:
    def __init__(self):
        self.head = None

    def them_cuoi(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def them_truoc(self, value, truoc_value):
        new_node = Node(value)
        if not self.head:
            print("Danh sach rong.")
            return

        if self.head.data == truoc_value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data != truoc_value:
            current = current.next

        if not current.next:
            print(f"Khong tim thay gia tri {truoc_value} trong danh sach.")
            return

        new_node.next = current.next
        current.next = new_node

    def in_ds(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def in_ds_nguoc(self):
        self._in_ds_nguoc(self.head)
        print()

    def _in_ds_nguoc(self, node):
        if node:
            self._in_ds_nguoc(node.next)
            print(node.data, end=" ")

    def tim_gt_min_max(self):
        if not self.head:
            return None, None

        min_value = max_value = self.head.data
        current = self.head.next
        while current:
            min_value = min(min_value, current.data)
            max_value = max(max_value, current.data)
            current = current.next

        return min_value, max_value

    def tinh_tong_am_duong(self):
        sum_positive = sum_negative = 0
        current = self.head
        while current:
            if current.data > 0:
                sum_positive += current.data
            elif current.data < 0:
                sum_negative += current.data
            current = current.next

        return sum_positive, sum_negative

    def tinh_tich(self):
        if not self.head:
            return 0

        result = 1
        current = self.head
        while current:
            result *= current.data
            current = current.next

        return result

    def tinh_tong_binh_phuong(self):
        return sum(x**2 for x in self)

    def tim_so_nguyen_to(self, x):
        prime_factors = []
        current = self.head
        while current:
            if self._la_so_nguyen_to(current.data) and current.data < x:
                prime_factors.append(current.data)
            current = current.next

        return prime_factors

    def tim_uoc_so(self, x):
        return [i for i in range(1, x + 1) if x % i == 0]

    def tim_gt_dau_tien_lon_hon_x(self, x):
        current = self.head
        while current:
            if current.data > x:
                return current.data
            current = current.next
        return None

    def tim_so_nguyen_to_cuoi_cung(self):
        prime_numbers = [i for i in self if self._la_so_nguyen_to(i)]
        return prime_numbers[-1] if prime_numbers else None

    def dem_so_nguyen_to(self):
        return len([i for i in self if self._la_so_nguyen_to(i)])

    def kiem_tra_sap_tang(self):
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def kiem_tra_doi_xung(self):
        values = list(self)
        return values == values[::-1]

    def xoa_cuoi(self):
        if not self.head:
            print("Danh sach rong, khong co phan tu de xoa.")
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None

    def xoa_dau(self):
        if not self.head:
            print("Danh sach rong, khong co phan tu de xoa.")
            return

        self.head = self.head.next

    def huy_ds(self):
        self.head = None

    def _la_so_nguyen_to(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

if __name__ == "__main__":
    ds = DSLienKetDon()

    while True:
        print("\nMenu:")
        print("1. Thêm một số vào cuối danh sách")
        print("2. Thêm một số vào trước một số khác")
        print("3. In danh sách")
        print("4. In danh sách theo thứ tự ngược")
        print("5. Tìm giá trị nhỏ nhất và lớn nhất trong danh sách")
        print("6. Tính tổng số dương và số âm trong danh sách")
        print("7. Tính tích của các số trong danh sách")
        print("8. Tính tổng bình phương các số trong danh sách")
        print("9. Nhập x, xuất các số là số nguyên tố nhỏ hơn x")
        print("10. Nhập x, xuất các ước số của x")
        print("11. Nhập x, tìm giá trị đầu tiên trong danh sách lớn hơn x")
        print("12. Xuất số nguyên tố cuối cùng trong danh sách")
        print("13. Đếm số nguyên tố trong danh sách")
        print("14. Kiểm tra xem danh sách có sắp tăng không")
        print("15. Kiểm tra xem danh sách có các phần tử đối xứng hay không")
        print("16. Xóa phần tử cuối cùng")
        print("17. Xóa phần tử đầu tiên")
        print("18. Hủy toàn bộ danh sách")
        print("0. Thoát")
        
        choice = int(input("Nhập lựa chọn của bạn: "))

        if choice == 0:
            break
        elif choice == 1:
            value = int(input("Nhập giá trị: "))
            ds.them_cuoi(value)
        elif choice == 2:
            value = int(input("Nhập giá trị: "))
            before_value = int(input("Nhập giá trị trước đó: "))
            ds.them_truoc(value, before_value)
        elif choice == 3:
            ds.in_ds()
        elif choice == 4:
            ds.in_ds_nguoc()
        elif choice == 5:
            min_val, max_val = ds.tim_gt_min_max()
            print(f"Giá trị nhỏ nhất: {min_val}, Giá trị lớn nhất: {max_val}")
        elif choice == 6:
            sum_pos, sum_neg = ds.tinh_tong_am_duong()
            print(f"Tổng số dương: {sum_pos}, Tổng số âm: {sum_neg}")
        elif choice == 7:
            product = ds.tinh_tich()
            print(f"Tích của các số: {product}")
        elif choice == 8:
            sum_squares = ds.tinh_tong_binh_phuong()
            print(f"Tổng bình phương của các số: {sum_squares}")
        elif choice == 9:
            x = int(input("Nhập x: "))
            prime_factors = ds.tim_so_nguyen_to(x)
            print(f"Các số nguyên tố nhỏ hơn {x}: {prime_factors}")
        elif choice == 10:
            x = int(input("Nhập x: "))
            divisors = ds.tim_uoc_so(x)
            print(f"Các ước số của {x}: {divisors}")
        elif choice == 11:
            x = int(input("Nhập x: "))
            first_greater = ds.tim_gt_dau_tien_lon_hon_x(x)
            print(f"Giá trị đầu tiên lớn hơn {x}: {first_greater}")
        elif choice == 12:
            last_prime = ds.tim_so_nguyen_to_cuoi_cung()
            print(f"Số nguyên tố cuối cùng trong danh sách: {last_prime}")
        elif choice == 13:
            count_primes = ds.dem_so_nguyen_to()
            print(f"Số lượng số nguyên tố trong danh sách: {count_primes}")
        elif choice == 14:
            is_sorted = ds.kiem_tra_sap_tang()
            print(f"Danh sách có sắp tăng: {is_sorted}")
        elif choice == 15:
            is_symmetric = ds.kiem_tra_doi_xung()
            print(f"Danh sách có các phần tử đối xứng: {is_symmetric}")
        elif choice == 16:
            ds.xoa_cuoi()
            print("Đã xóa phần tử cuối cùng.")
        elif choice == 17:
            ds.xoa_dau()
            print("Đã xóa phần tử đầu tiên.")
        elif choice == 18:
            ds.huy_ds()
            print("Đã hủy toàn bộ danh sách.")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
