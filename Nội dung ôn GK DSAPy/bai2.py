# Bài 2: Đối tượng
# 1. Thêm 1 sinh viên vào DSLK
# 2. Cập nhật thông tin sinh viên tại vị trí trong DSLK?
# 3. Xóa sinh viên ra khỏi DSLK
# 4. Tìm kiếm sinh viên “A” có trong DSLK không?
class Student:
    def __init__(self, name, born, studentID):
        self.name = name
        self.born = born
        self.studentID = studentID
        self.next = None

    def info(self):
        return f"Name: {self.name}, Born: {self.born}, Student ID: {self.studentID}"


class LinkedStudent:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Them
    def append(self, stu):
        student_node = stu
        if self.head is None:
            self.head = student_node
            self.tail = student_node
        else:
            self.tail.next = student_node
            self.tail = student_node

    # 0. In
    def display(self):
        current = self.head
        kq = "---------Display-----------\n"
        while current is not None:
            kq += current.info() + "\n"
            current = current.next
        print(kq)

    # 2. Cap nhat
    def update(self, location, name):
        current = self.head
        local = 0
        while current is not None and local < location:
            local += 1
            current = current.next
        if current is not None and local == location:
            current.name = name

    # 3. Xoa
    def remove(self, name):
        previous = None
        current = self.head
        while (
            current is not None and current.name.strip().lower() != name.strip().lower()
        ):
            previous = current
            current = current.next
        if current != None:
            if current == self.head and current == self.tail:
                self.head = self.tail = None
            elif previous == None:
                self.head = self.head.next
            elif current == None:
                previous.next = current
                self.tail = current
            else:
                previous.next = current.next
            del current

    # 4. Tim kiem
    def sreach(self, studentID):
        if self.head == None:
            raise ValueError("No data !!!")
        else:
            current = self.head
            location = 0
            while current != None and current.studentID != studentID:
                location += 1
                current = current.next
            if current != None:
                return location
            else:
                return None


def main():
    ds = LinkedStudent()
    a = Student("Tom", 2004, 111)
    b = Student("Mark", 2001, 131)
    c = Student("Peter", 2006, 112)
    ds.append(a)
    ds.append(b)
    ds.append(c)

    ds.display()
    ds.update(0, "Timmy")
    ds.display()
    ds.remove("   timmy")
    ds.display()
    vt = ds.sreach(131)
    print(vt)


if __name__ == "__main__":
    main()
