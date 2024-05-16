import math
# Bài 1: Số
# 1. Khởi tạo 1 danh sách liên kết
class Nut:
    def __init__(self, data):
        self.data = data
        self.nutKeTiep = None
class DSLK:
    def __init__(self):
        self.head = None
        self.tail = None
# 2. Thêm 1 node vào DSLK
    def them(self, newdata):
        nut = Nut(newdata)  
        if self.head == None:
            self.head = nut
            self.tail = nut
        else:
            self.tail.nutKeTiep = nut
            self.tail = nut                                                                                                                       
# 3. Thêm vào một vị trí bất kỳ
    def themVT(self, viTri, newdata):
        nut = Nut(newdata)
        hienTai = self.head
        truoc = None
        i = 0
        while i < viTri and hienTai != None:
            truoc = hienTai
            i += 1
            hienTai = hienTai.nutKeTiep
        if truoc == None:
            nut.nutKeTiep = self.head
            self.head = nut
            if self.tail == None:
                self.tail = nut
        else:
            if hienTai == None:
                self.tail.nutKeTiep = nut
                self.tail = nut
            else:
                truoc.nutKeTiep = nut
                nut.nutKeTiep = hienTai
# 4. Thêm vào đầu DSLK
    def themDau(self, newdata):
        nut = Nut(newdata)
        if self.head == None:
            self.head = nut
            self.tail = nut
        else:
            nut.nutKeTiep = self.head
            self.head = nut
# 5. Thêm vào cuối DSLK
    def themCuoi(self, newdata):
        nut = Nut(newdata)
        if self.head == None:
            self.head = nut
            self.tail = nut
        else:
            self.tail.nutKeTiep = nut
            self.tail = nut  
# 6. Xóa phần tử nằm ở đầu DSLK
    def xoaDau(self):
        if self.head.nutKeTiep == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.nutKeTiep
# 7. Xóa phần tử ở cuối DSLK
    def xoaCuoi(self):
        if self.head.nutKeTiep == None:
            self.head = None
            self.tail = None
        else:
            hienTai = self.head
            truoc = None
            while hienTai.nutKeTiep != None:
                truoc = hienTai
                hienTai = hienTai.nutKeTiep
            truoc.nutKeTiep = None
            self.tail = truoc
# IN DSLK
    def inds(self):
        hienTai = self.head
        i = 0
        kt = '['
        while hienTai != None:
            i += 1
            if i == 1:
                kt += str(hienTai.data)
            else:
                kt += '->' + str(hienTai.data)
            hienTai = hienTai.nutKeTiep
        kt += ']'
        print(kt)
# 8. Xóa phần tử tại 1 vị trí bất kỳ
    def xoaVT(self, viTri):
        hienTai = self.head
        truoc = None
        vt = 0
        while vt < viTri and hienTai != None:
            vt += 1
            truoc = hienTai
            hienTai = hienTai.nutKeTiep
        if hienTai != None:
            if hienTai == self.head and hienTai == self.tail:
                self.head = None
                self.tail = None
            elif hienTai == self.head:
                self.head = self.head.nutKeTiep
            elif hienTai == self.tail:
                truoc.nutKeTiep = None
                self.tail = truoc
            else:
                truoc.nutKeTiep = hienTai.nutKeTiep           
# 9. Tìm số chẵn trong DSLK
    def timSoChan(self):
        ds = []
        hienTai = self.head
        while hienTai != None:
            if hienTai.data % 2 == 0:
                ds.append(hienTai.data)
            hienTai = hienTai.nutKeTiep
        return ds
# 10. Tìm số lẻ trong DSLK
    def timSoLe(self):
        ds = []
        hienTai = self.head
        while hienTai != None:
            if hienTai.data % 2 != 0:
                ds.append(hienTai.data)
            hienTai = hienTai.nutKeTiep
        return ds
# 11. Tìm số chính phương trong DSLK
    def timSCP(self):
        ds = []
        hienTai = self.head
        while hienTai != None:
            if math.sqrt(hienTai.data)**2 == hienTai.data:
                ds.append(hienTai.data)
            hienTai = hienTai.nutKeTiep
        return ds
# 12. Tìm số nguyên tố trong DSLK
    def timSNT(self):
        ds = []
        hienTai = self.head
        while hienTai != None:
            a = hienTai.data
            b = 0
            if a > 1: 
                for i in range(2, int(a*0.5)+1):
                    if a % i == 0:
                        b += 1
                if b == 0:
                    ds.append(a)
                    
            hienTai = hienTai.nutKeTiep
        return ds
# 13. Tìm số lớn nhất trong DSLK
    def timMax(self):
        hienTai = self.head
        tam = self.head.data
        while hienTai != None:
            if hienTai.data > tam:
                tam = hienTai.data
            hienTai = hienTai.nutKeTiep
        return tam
# 14. Tìm số nhỏ nhất trong DSLK
    def timMin(self):
        hienTai = self.head
        tam = self.head.data
        while hienTai != None:
            if hienTai.data < tam:
                tam = hienTai.data
            hienTai = hienTai.nutKeTiep
        return tam       
# 15. Đếm số lớn nhất trong DSLK
    def demSoLonNhat(self):
        max = self.timMax()
        i = 0
        hienTai = self.head
        while hienTai != None:
            if hienTai.data == max:
                i += 1
            hienTai = hienTai.nutKeTiep
        return i
# 16. Đếm số số nhỏ nhất trong DSLK
    def demSoNhoNhat(self):
        min = self.timMin()
        i = 0
        hienTai = self.head
        while hienTai != None:
            if hienTai.data == min:
                i += 1
            hienTai = hienTai.nutKeTiep
        return i
# 17. Cập nhật lại giá trị tại 1 vị trí trong DSLK
    def capNhatVT(self, viTri, giaTri):
        hienTai = self.head
        i = 0
        while i < viTri and hienTai != None:
            i += 1
            hienTai = hienTai.nutKeTiep
        if hienTai != None:
            hienTai.data = giaTri
# 18. Cập nhật lại giá trị ở đầu DSLK
    def capNhatDau(self, giaTri):
        if self.head == None:
            raise ValueError("Mày ngu nó rỗng")
        else:
            self.head.data = giaTri
# 19. Cập nhật lại giá trị ở cuối DSLK
    def capNhatCuoi(self, giaTri):
        if self.head == None:
            raise ValueError("Mày ngu nó rỗng")
        else:
            self.tail.data = giaTri
def main():
    ds = DSLK()
    print("Thêm vào danh sách: ")
    ds.them(100)
    ds.them(50)
    ds.themVT(3,4)
    print("Thêm vào đầu danh sách: ")
    ds.them(5)
    print("Thêm vào cuối danh sách: ")
    ds.themCuoi(16)
    ds.inds()
    print("Thêm vào một vị trí nhất định: ")
    ds.themVT(1,4)
    ds.inds()
    print("Xóa phần tử đầu tiên: ")
    ds.xoaDau()
    ds.inds()
    print("Xóa phần tử cuối cùng: ")
    ds.xoaCuoi()
    ds.inds()
    print("Xóa tại một vị trí")
    ds.xoaVT(2)
    ds.inds()
    print("Tìm số chẵn: ", ds.timSoChan())
    print("Tìm số lẽ: ", ds.timSoLe())
    print("Tìm số chính phương: ", ds.timSCP())
    print("Tìm số nguyên tố: ", ds.timSNT())
    print("Tìm số lớn nhất: ", ds.timMax())
    print("Tìm số nhỏ nhất: ", ds.timMin())
    print("Đếm số lớn nhất: ", ds.demSoLonNhat())
    print("Đếm số nhỏ nhất: ", ds.demSoNhoNhat())
    print("Cập nhật giá trị của vị trí: ")
    ds.capNhatVT(2, 5)
    ds.inds()
    print("Cập nhật giá trị đầu: ")
    ds.capNhatDau(2)
    ds.inds()
    print("Cập nhật giá trị cuối: ")
    ds.capNhatCuoi(7)
    ds.inds()    
if __name__ == "__main__":
    main()