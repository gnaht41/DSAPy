class IdValue:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def info(self):
        return f"Id: {self.id}, value: {self.value}"


class IdValueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def info(self):
        return self.data.info()


class IdValueSLL:
    # 1. Khởi tạo 1 danh sách liên kết
    def __init__(self):
        self.head = None
        self.tail = None

    # 2. Thêm 1 node vào DSLK
    def append(self, new_data):
        new_node = IdValueNode(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # 3. Thêm vào một vị trí bất kỳ
    def insert_at_position(self, position, new_data):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.prepend(new_data)
            return
        new_node = IdValueNode(new_data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Invalid position")
                return
            current = current.next
        if current:
            new_node.next = current.next
            current.next = new_node

    # 4. Thêm vào đầu DSLK
    def prepend(self, new_data):
        new_node = IdValueNode(new_data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    # 5. Thêm vào cuối DSLK
    def addTail(self, new_data):
        self.append(new_data)

    # 6. Xóa phần tử nằm ở đầu DSLK
    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    # 7. Xóa phần tử ở cuối DSLK
    def delete_last(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        current = self.head
        while current.next != self.tail:
            current = current.next
        current.next = None
        self.tail = current

    # 8. Xóa phần tử tại 1 vị trí bất kỳ
    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.delete_first()
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Invalid position")
                return
            current = current.next
        if current is None or current.next is None:
            print("Invalid position")
            return
        current.next = current.next.next

    # 9. Tìm số chẵn trong DSLK
    def find_even_numbers(self):
        current = self.head
        even_numbers = []
        while current:
            if current.data.value % 2 == 0:
                even_numbers.append(current.data)
            current = current.next
        return even_numbers

    # 10. Tìm số lẻ trong DSLK
    def find_odd_numbers(self):
        current = self.head
        odd_numbers = []
        while current:
            if current.data.value % 2 != 0:
                odd_numbers.append(current.data)
            current = current.next
        return odd_numbers

    # 11. Tìm số chính phương trong DSLK
    def is_perfect_square(self, num):
        return int(num**0.5) ** 2 == num

    def find_perfect_squares(self):
        current = self.head
        perfect_squares = []
        while current:
            if self.is_perfect_square(current.data.value):
                perfect_squares.append(current.data)
            current = current.next
        return perfect_squares

    # 12. Tìm số nguyên tố trong DSLK
    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def find_prime_numbers(self):
        current = self.head
        prime_numbers = []
        while current:
            if self.is_prime(current.data.value):
                prime_numbers.append(current.data)
            current = current.next
        return prime_numbers

    # 13. Tìm số lớn nhất trong DSLK
    def find_maximum(self):
        if self.head is None:
            return None
        current = self.head
        maximum = current.data.value
        while current:
            if current.data.value > maximum:
                maximum = current.data.value
            current = current.next
        return maximum

    # 14. Tìm số nhỏ nhất trong DSLK
    def find_minimum(self):
        if self.head is None:
            return None
        current = self.head
        minimum = current.data.value
        while current:
            if current.data.value < minimum:
                minimum = current.data.value
            current = current.next
        return minimum

    # 15. Đếm số lớn nhất trong DSLK
    def count_maximum(self):
        if self.head is None:
            return 0
        maximum = self.find_maximum()
        count = 0
        current = self.head
        while current:
            if current.data.value == maximum:
                count += 1
            current = current.next
        return count

    # 16. Đếm số số nhỏ nhất trong DSLK
    def count_minimum(self):
        if self.head is None:
            return 0
        minimum = self.find_minimum()
        count = 0
        current = self.head
        while current:
            if current.data.value == minimum:
                count += 1
            current = current.next
        return count

    # 17. Cập nhật lại giá trị tại 1 vị trí trong DSLK
    def update_at_position(self, position, new_value):
        if position < 0:
            print("Invalid position")
            return
        current = self.head
        for _ in range(position):
            if current is None:
                print("Invalid position")
                return
            current = current.next
        if current:
            current.data.value = new_value

    # 18. Cập nhật lại giá trị ở đầu DSLK
    def update_at_head(self, new_value):
        if self.head:
            self.head.data.value = new_value

    # 19. Cập nhật lại giá trị ở cuối DSLK
    def update_at_tail(self, new_value):
        if self.tail:
            self.tail.data.value = new_value

    # 20. In ra kết quả
    def checkResult(self):
        currently = self.head
        while currently is not None:
            kq = str(currently.data.info()) + "\n"
            print(kq)
            currently = currently.next

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def isDuplicated(self, id):
        currently = self.head
        while currently != None and currently.data.id != id:
            currently = currently.next
        if currently != None:
            return True
        return False


def main():
    # Khởi tạo danh sách liên kết
    ds = IdValueSLL()

    # Thêm các phần tử vào DSLK
    ds.append(IdValue("a", 1))
    ds.append(IdValue("b", 2))
    ds.append(IdValue("c", 3))
    ds.append(IdValue("d", 4))
    ds.append(IdValue("e", 5))

    # In ra danh sách liên kết sau khi đã thêm
    print("Danh sách liên kết sau khi đã thêm:")
    ds.checkResult()

    # Kiểm tra DSLK có trống hay không
    print("\nKiểm tra DSLK có trống hay không:", ds.isEmpty())

    # Kiểm tra xem phần tử "b" có bị trùng hay không
    print("\nKiểm tra xem phần tử 'b' có bị trùng hay không:", ds.isDuplicated("b"))

    # Xóa phần tử đầu tiên và in ra danh sách liên kết
    ds.delete_first()
    print("\nDanh sách liên kết sau khi xóa phần tử đầu tiên:")
    ds.checkResult()

    # Xóa phần tử cuối cùng và in ra danh sách liên kết
    ds.delete_last()
    print("\nDanh sách liên kết sau khi xóa phần tử cuối cùng:")
    ds.checkResult()

    # Xóa phần tử ở vị trí 1 và in ra danh sách liên kết
    ds.delete_at_position(1)
    print("\nDanh sách liên kết sau khi xóa phần tử ở vị trí 1:")
    ds.checkResult()

    # Thêm phần tử mới vào vị trí 2 và in ra danh sách liên kết
    ds.insert_at_position(2, IdValue("f", 6))
    print("\nDanh sách liên kết sau khi thêm phần tử mới vào vị trí 2:")
    ds.checkResult()

    # Tìm số chẵn trong DSLK và in ra kết quả
    print("\nCác số chẵn trong DSLK là:")
    print([node.info() for node in ds.find_even_numbers()])

    # Tìm số lẻ trong DSLK và in ra kết quả
    print("\nCác số lẻ trong DSLK là:")
    print([node.info() for node in ds.find_odd_numbers()])

    # Tìm số chính phương trong DSLK và in ra kết quả
    print("\nCác số chính phương trong DSLK là:")
    print([node.info() for node in ds.find_perfect_squares()])

    # Tìm số nguyên tố trong DSLK và in ra kết quả
    print("\nCác số nguyên tố trong DSLK là:")
    print([node.info() for node in ds.find_prime_numbers()])

    # Tìm số lớn nhất trong DSLK
    print("\nSố lớn nhất trong DSLK là:", ds.find_maximum())

    # Tìm số nhỏ nhất trong DSLK
    print("Số nhỏ nhất trong DSLK là:", ds.find_minimum())

    # Đếm số lớn nhất trong DSLK
    print("Số lớn nhất xuất hiện", ds.count_maximum(), "lần trong DSLK")

    # Đếm số nhỏ nhất trong DSLK
    print("Số nhỏ nhất xuất hiện", ds.count_minimum(), "lần trong DSLK")

    # Cập nhật lại giá trị tại vị trí 1 trong DSLK
    ds.update_at_position(1, 10)
    print("\nDanh sách liên kết sau khi cập nhật giá trị tại vị trí 1:")
    ds.checkResult()

    # Cập nhật lại giá trị ở đầu DSLK
    ds.update_at_head(100)
    print("\nDanh sách liên kết sau khi cập nhật giá trị ở đầu DSLK:")
    ds.checkResult()

    # Cập nhật lại giá trị ở cuối DSLK
    ds.update_at_tail(200)
    print("\nDanh sách liên kết sau khi cập nhật giá trị ở cuối DSLK:")
    ds.checkResult()


if __name__ == "__main__":
    main()
