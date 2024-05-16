import math


class Nut:
    def __init__(self, data):
        self.data = data
        self.next = None


class DSLK:
    # 1. Khoi tao DSLK
    def __init__(self):
        self.head = None
        self.tail = None

    # 2. Them 1 node vao DSLK
    def append(self, data):
        nut = Nut(data)
        if self.head == None:
            self.head = nut
            self.tail = nut
        else:
            self.tail.next = nut
            self.tail = nut

    # 3. Them 1 vi tri bat ki
    def append_position(self, location, data):
        previous = None
        current = self.head
        nut = Nut(data)
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

    # 4. Them dau
    def appendHead(self, data):
        nut = Nut(data)
        if self.head == None:
            self.head = nut
        else:
            nut.next = self.head
            self.head = nut

    # 5. Them duoi
    def appendTail(self, data):
        nut = Nut(data)
        if self.head == None:
            self.head = nut
        else:
            self.tail.next = nut
            self.tail = nut

    # 6. Xuat
    def display(self):
        kq = "["
        current = self.head
        vt = 0
        while current != None:
            vt += 1
            if vt == 1:
                kq += "" + str(current.data)
            else:
                kq += ", " + str(current.data)
            current = current.next
        kq += "] "
        print(kq)

    # 7. Xoa dau
    def removeFirst(self):
        if self.head == None:
            raise ValueError("Data is empty!!!")
        else:
            self.head = self.head.next

    # 8. Xoa duoi
    def removeTail(self):
        if self.head == None:
            raise ValueError("Data is empty!!!")
        else:
            current = self.head
            while current.next.next != None:
                current = current.next
            current.next = None

    # 9. Xoa o vi tri bat ki
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

    # 10. Tim chan
    def even(self):
        current = self.head
        a = []
        while current != None:
            if current.data % 2 == 0:
                a.append(current.data)
            current = current.next  # Move the pointer to the next node
        return a

    # 11. Tim le
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


def main():
    ds = DSLK()
    ds.append(3)
    ds.appendHead(2)
    ds.appendTail(7)
    ds.append_position(0, 4)
    ds.append(5)
    ds.appendHead(6)
    ds.appendTail(9)
    ds.append_position(0, 100)
    ds.append_position(0, 100)
    print("------------------- Display-----------------")
    ds.display()
    print()
    chan_list = ds.even()
    print("Số chẵn trong DSLK:", chan_list)

    # Gọi hàm odd để tìm số lẻ
    le_list = ds.odd()
    print("Số lẻ trong DSLK:", le_list)
    # So chính phương
    list_square = ds.perfect_square()
    print(f"Perfect square in data: ", list_square)
    # So nguyen to
    print(f"Prime in data: ", ds.isPrime())
    print(f"Max in data: ", ds.max_value())
    print(f"Min in data: ", ds.min_value())
    print(f"Count max in data: ", ds.count_max())
    print(f"Count min in data: ", ds.count_min())
    ds.update(0, 2000)
    ds.display()
    ds.update_first(1011.11)
    ds.display()
    ds.update_last(30020)
    ds.display()


if __name__ == "__main__":
    main()
