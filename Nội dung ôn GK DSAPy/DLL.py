# Bài 1: Số
# 1. Khởi tạo 1 danh sách liên kết
class Nut:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    # 2. Thêm 1 node vào DSLK
    def them1Node(self, newdata):
        nut = Nut(newdata)
        if self.head == None:
            self.head = nut
            self.tail = nut
        else:
            self.tail.next = nut
            nut.prev = self.tail
            self.tail = nut

    ##Check
    def inDS(self):
        hienTai = self.head
        i = 0
        kt = ""
        while hienTai != None:
            i += 1
            if i == 1:
                kt += str(hienTai.data)
            else:
                kt += "->" + str(hienTai.data)
            hienTai = hienTai.next
        print(kt)

    # 3. Thêm vào một vị trí bất kỳ
    def themVT(self, viTri, newdata):
        nut = Nut(newdata)
        hienTai = self.head
        i = 0
        while i < viTri and hienTai != None:
            i += 1
            hienTai = hienTai.next
        if hienTai != None:
            if hienTai == self.head and hienTai == self.tail:
                self.head = nut
                self.tail = nut
            elif hienTai == self.head:
                self.head.prev = nut
                nut.next = self.head
                self.head = nut
            elif hienTai == self.tail:
                self.tail.next = nut
                nut.prev = self.tail
                self.tail = nut
            else:
                hienTai.prev.next = nut
                nut.next = hienTai

    # 4. Thêm vào đầu DSLK
    def themDau(self, newdata):
        nut = Nut(newdata)
        if self.head == None:
            self.head = nut
            self.tail = nut
        else:
            self.head.prev = nut
            nut.next = self.head
            self.head = nut

    # 5. Thêm vào cuối DSLK
    def themCuoi(self, newdata):
        nut = Nut(newdata)
        if self.head == None:
            self.head = nut
            self.tail = nut
        else:
            self.tail.next = nut
            nut.prev = self.tail
            self.tail = nut

    # 6. Xóa phần tử nằm ở đầu DSLK
    def xoaDau(self):
        if self.head == None:
            raise ValueError("Nó rỗng mày ngu!")
        elif self.head.next == None:
            self.head = self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

    # 7. Xóa phần tử ở cuối DSLK
    def xoaCuoi(self):
        if self.head == None:
            raise ValueError("Nó rỗng mày ngu!")
        elif self.head.next == None:
            self.head = self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    # 8. Xóa phần tử tại 1 vị trí bất kỳ
    def xoaVT(self, viTri):
        if self.head == None:
            raise ValueError("Nó rỗng mày ngu!")
        else:
            hienTai = self.head
            i = 0
            truoc = None
            while i < viTri and hienTai != None:
                i += 1
                truoc = hienTai
                hienTai = hienTai.next
            if hienTai != None:
                if hienTai == self.head and hienTai == self.tail:
                    self.head = self.tail = None
                elif hienTai == self.head:
                    self.head.next.prev = None
                    self.head = self.head.next
                elif hienTai == self.tail:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev
                else:
                    truoc.next = hienTai.next
            else:
                raise ValueError("Nhập quá trớn rồi thằng ngu!")

    # 9. Tìm số chẵn trong DSLK
    # 10. Tìm số lẻ trong DSLK
    # 11. Tìm số chính phương trong DSLK
    # 12. Tìm số nguyên tố trong DSLK
    # 13. Tìm số lớn nhất trong DSLK
    # 14. Tìm số nhỏ nhất trong DSLK
    # 15. Đếm số lớn nhất trong DSLK
    # 16. Đếm số số nhỏ nhất trong DSLK
    # 17. Cập nhật lại giá trị tại 1 vị trí trong DSLK
    def capNhatVT(self, viTri, newData):
        if self.head == None:
            raise ValueError("Nó rỗng mày ngu!")
        else:
            hienTai = self.head
            i = 0
            while i < viTri and hienTai != None:
                i += 1
                hienTai = hienTai.next
            if hienTai != None:
                hienTai.data = newData

    # 18. Cập nhật lại giá trị ở đầu DSLK
    def capNhatD(self, newData):
        if self.head == None:
            raise ValueError("Nó rỗng mày ngu!")
        else:
            self.head.data = newData

    # 19. Cập nhật lại giá trị ở cuối DSLK
    def capNhatC(self, newData):
        if self.head == None:
            raise ValueError("Nó rỗng mày ngu!")
        else:
            self.tail.data = newData


def main():
    ds = DLL()
    print("Thêm 1 node vào DSLK: 10-20-30")
    ds.them1Node(10)
    ds.them1Node(20)
    ds.them1Node(30)
    ds.them1Node(70)
    ds.them1Node(80)
    ds.inDS()
    print("\nThêm vào một vị trí bất kỳ: VT-1, 40")
    ds.themVT(1, 40)
    ds.inDS()
    print("\n4. Thêm vào đầu DSLK: 50")
    ds.themDau(50)
    ds.inDS()
    print("\n5. Thêm vào cuối DSLK: 60")
    ds.themCuoi(60)
    ds.inDS()
    print("\n6. Xóa phần tử nằm ở đầu DSLK")
    ds.xoaDau()
    ds.inDS()
    print("\n7. Xóa phần tử ở cuối DSLK")
    ds.xoaCuoi()
    ds.inDS()
    print("\n8. Xóa phần tử tại 1 vị trí bất kỳ")
    ds.xoaVT(4)
    ds.inDS()
    print("\n17. Cập nhật lại giá trị tại 1 vị trí trong DSLK")
    ds.capNhatVT(1, 5)
    ds.inDS()
    print("\n18. Cập nhật lại giá trị ở đầu DSLK")
    ds.capNhatD(6)
    ds.inDS()
    print("\n19. Cập nhật lại giá trị ở cuối DSLK")
    ds.capNhatC(8)
    ds.inDS()


if __name__ == "__main__":
    main()
