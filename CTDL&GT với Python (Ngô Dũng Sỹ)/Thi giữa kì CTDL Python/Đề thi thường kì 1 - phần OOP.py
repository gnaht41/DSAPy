import random


class Nguoi:
    tienPhuCap = 100

    def __init__(self, maDD, tenNguoi):
        self.maDD = maDD
        self.tenNguoi = tenNguoi

    def xuat(self):
        print(f"{self.maDD} có tên là {self.tenNguoi}")


class NhanVien(Nguoi):
    def __init__(self, maDD, tenNguoi, namSinh, heSoLuong):
        super().__init__(maDD, tenNguoi)
        self.namSinh = namSinh
        self.heSoluong = heSoLuong

    def tinhTienLuong(self):
        return self.heSoluong * 1550 + NhanVien.tienPhuCap

    def xuat(self):
        print("Mã định danh\tTên nhân viên\tNăm sinh\tHệ số lương\tTiền lương")
        print(
            f"{self.maDD}\t\t{self.tenNguoi}\t\t{self.namSinh}\t\t{self.heSoluong}\t\t{self.tinhTienLuong()}"
        )

    def soSanh(self, other):
        return self.heSoluong > other.heSoLuong


def main():
    print("1.Nhập thông tin cho 1 người\n")
    print("2.Hiển thị thông tin\n")
    print("3.Nhập thông tin n nhân viên\n")
    print("4.In ra n nhân viên\n")
    print("5.Sắp xếp nhân viên\n")

    while True:
        choice = int(input("Nhập lựa chọn : "))
        match choice:
            case 1:
                maDD = int(input("Nhập mã định danh : "))
                tenNguoi = str(input("Nhập tên nhân viên : "))
                namSinh = int(input("Nhập mã năm sinh : "))
                heSoLuong = float(input("Nhập mã hệ số lương : "))
                nv1 = NhanVien(maDD, tenNguoi, namSinh, heSoLuong)

            case 2:
                nv1.xuat()

            case 3:
                n = int(input("Nhập số lượng n : "))
                dsNV = []
                for i in range(n):
                    maDD = int(input("Nhập mã định danh : "))
                    tenNguoi = str(input("Nhập tên nhân viên : "))
                    namSinh = int(input("Nhập mã năm sinh : "))
                    heSoLuong = float(input("Nhập mã hệ số lương : "))
                    nv = NhanVien(maDD, tenNguoi, namSinh, heSoLuong)
                    dsNV.append(nv)
            case 4:
                for i in range(n):
                    dsNV[i].xuat()
            case 5:
                dsNV.sort(key=lambda x: x.heSoluong, reverse=True)
                print("Danh sách nhân viên sau khi sắp xếp:")
                for nv in dsNV:
                    nv.xuat()

            case 0:
                break


if __name__ == "__main__":
    main()
