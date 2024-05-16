class Nut:
    def __init__(self, data):
        self.data = data
        self.nutKeTiep = None
class Stack:
    def __init__(self):
        self.top = None
    def isEmpty(self):
        return self.top == None
    def push(self, newdata):
        nut = Nut(newdata)
        if self.isEmpty():
            self.top = nut
        else:
            nut.nutKeTiep = self.top
            self.top = nut
    def pop(self):
        if self.isEmpty():
            print("Ngăn sắp xếp rỗng.")
            return None
        else:
            hienTai = self.top
            self.top = self.top.nutKeTiep
            return hienTai.data
    def peek(self):
        if self.isEmpty():
            print("Ngăn sắp xếp rỗng.")
            return None
        else:
            return self.top.data
    def display(self):
        cur = self.top
        if self.isEmpty():
            print("Ngắn sắp xếp rỗng.")
        else:
            while cur != None:
                print(cur.data)
                cur = cur.nutKeTiep
    def size(self):
        cur = self.top
        i = 0
        while cur != None:
            i += 1
            cur = cur.nutKeTiep
        return i
def main():
    s = Stack()
    s.push(5)
    s.push(10)
    s.push(12)
    print("Phần tử ở đỉnh ngăn xếp: ", s.peek())
    s.display()
    print("Phần tử bị loại bỏ: ", s.pop())
    s.display()
    print("Kích thước của ngăn sắp xếp: ", s.size())
if __name__ == "__main__":
    main()