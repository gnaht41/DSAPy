import math


class IdValue:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def info(self):
        return f"Id: {self.id}, Value: {self.value}"


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
    def addTail(self, newData):
        currently = IdValueNode(newData)

        if self.head is None:
            self.head = currently
            self.tail = currently 
        else:
            self.tail.next = currently
            self.tail = currently

    # 3. Thêm vào một vị trí bất kỳ
    def append_position(self, location, data):
        previous = None
        current = self.head
        nut = IdValueNode(data)
        local = 0
        while current != None and local < location:
            local += 1
            previous = current
            current = current.next
        if previous == None:
            nut.next = self.head
            self.head = nut
            if self.tail == None:
                self.tail = nut
        elif current == None:
            previous.next = nut
            self.tail = previous
        else:
            previous.next = nut
            nut.next = current

    # 4. Thêm vào đầu DSLK
    def appendHead(self, data):
        nut = IdValueNode(data)
        if self.head == None:
            self.head = nut
        else:
            nut.next = self.head
            self.head = nut

    # 5. Thêm vào cuối DSLK
    def appendTail(self, data):
        nut = IdValueNode(data)
        if self.head == None:
            self.head = nut
        else:
            self.tail.next = nut
            self.tail = nut

    # 6. Xóa phần tử nằm ở đầu DSLK
    def removeFirst(self):
        if self.head == None:
            raise ValueError("Data is empty!!!")
        else:
            self.head = self.head.next

    # 7. Xóa phần tử ở cuối DSLK
    def removeTail(self):
        if self.head == None:
            raise ValueError("Data is empty!!!")
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            current.next = None

    # 8. Xóa phần tử tại 1 vị trí bất kỳ
    def remove(self, location):
        previous = None
        current = self.head
        local = 0
        while local < location and current != None:
            local += 1
            previous = current
            current = current.next
        if current != None:
            if current == self.head and current == self.tail:
                self.head = self.tail = None
            elif current == self.head:
                self.head = self.head.next
            elif current == self.tail:
                previous.next = None
                self.tail = previous
            else:
                previous.next = current.next
            del current

    # 9. Tìm số chẵn trong DSLK
    def even(self):
        current = self.head
        a = []
        while current != None:
            if current.data % 2 == 0:
                a.append(current.data)
            current = current.next  # Move the pointer to the next node
        return a

    # 10. Tìm số lẻ trong DSLK
    def odd(self):
        current = self.head
        b = []
        while current != None:
            if current.data % 2 == 1:
                b.append(current.data)
            current = current.next
        return b

    # 11. Tìm số chính phương trong DSLK
    def perfect_square(self):
        current = self.head
        perfect_squares = []
        while current != None:
            if math.sqrt(current.data).is_integer():
                perfect_squares.append(current.data)
            current = current.next
        return perfect_squares

    # 12. Tìm số nguyên tố trong DSLK
    def isPrime(self):
        current = self.head
        arr_prime = []
        a = 0
        while current != None:
            if current.data < 2:
                arr_prime = []
            else:
                for i in range(int(math.sqrt(current.data) + 1)):
                    if current.data % 2 == 0:
                        arr_prime = []
                arr_prime.append(current.data)
            current = current.next
        return arr_prime

    # 13. Tìm số lớn nhất trong DSLK
    def max_value(self):
        if self.head is None:
            return None
        else:
            max = self.head.data
            current = self.head.next
            while current is not None:
                if max < current.data:
                    max = current.data
                current = current.next
            return max

    # 14. Tìm số nhỏ nhất trong DSLK
    def min_value(self):
        if self.head == None:
            return None
        else:
            min = self.head.data
            current = self.head.next
            while current is not None:
                if min > current.data:
                    min = current.data
                current = current.next
            return min

    # 15. Đếm số lớn nhất trong DSLK
    def count_max(self):
        max = self.max_value()
        current = self.head
        a = 0
        while current != None:
            if current.data == max:
                a += 1
            current = current.next
        return a

    # 16. Đếm số số nhỏ nhất trong DSLK
    def count_min(self):
        min = self.min_value()
        current = self.head
        count = 0
        while current != None:
            if min == current.data:
                count += 1
            current = current.next
        return count

    # 17. Cập nhật lại giá trị tại 1 vị trí trong DSLK
    def update(self, location, data):
        if self.head == None:
            return None
        else:
            current = self.head
            local = 0
            while current != None and local < location:
                local += 1
                current = current.next
            if current != None:
                current.data = data

    # 18. Cập nhật lại giá trị ở đầu DSLK
    def update_first(self, data):
        if self.head == None:
            raise ValueError("No data !!!")
        else:
            self.head.data = data

    # 19. Cập nhật lại giá trị ở cuối DSLK
    def update_last(self, data):
        if self.head == None:
            raise ValueError("No data!!")
        else:
            self.tail.data = data

    # 20. In ra kết quả
    def checkResult(self):
        currently = self.head
        while currently is not None:
            kq = str(currently.data.info()) + "\n"
            print(kq)
            currently = currently.next


def main():
    pass


if __name__ == "__main__":
    main()
