class MonHoc:
    # tạo ra một đối tượng 
    def __init__(self, maMH, tenMH, soTC):
        self.maMH = maMH
        self.tenMH = tenMH
        self.soTC = soTC

    def hienThiMonHoc(self):
        print("Mã môn học: ", self.maMH)
        print("Tên môn học: ", self.tenMH)
        print("Số tín chỉ: ", self.soTC)

#  
# mh1 = MonHoc(1, "Lập trình Python", 3)
# mh2 = MonHoc(2, "Lập trình Java", 3)

danhSachMonHoc = []


def nhapDanhSachMonHoc():
    soluong = int(input("Nhập vào số lượng: "))
    for i in range(soluong):
        maMH = input("Nhập mã môn học: ")
        tenMH = input("Nhập tên môn học: ")
        soTC = int(input("Nhập số tín chỉ: "))
        print("\n")
        # khởi tạo ra 1 biến tên mh
        mh = MonHoc(maMH, tenMH, soTC)
        danhSachMonHoc.append(mh)

def hienThiDSMonHoc():
    print("Thông tin danh sách môn học")
    for i in range(len(danhSachMonHoc)):
        print("Môn học thứ ", i+1)
        danhSachMonHoc[i].hienThiMonHoc()
        print("\n")

def ThemMonHoc():
    print("Nhập vào thông tin môn học cần thêm")
    maMH = input("Nhập mã môn học: ")
    tenMH = input("Nhập tên môn học: ")
    soTC = int(input("Nhập số tín chỉ: "))
    mh = MonHoc(maMH, tenMH, soTC)
    danhSachMonHoc.append(mh)
    print("\n")

def XoaMonHoc(ma_del):
    for i in danhSachMonHoc:
        if (i.maMH == ma_del):
            danhSachMonHoc.remove(i)

def TimkiemThongTin(thongtin):
    for i in range(len(danhSachMonHoc)):
        if (danhSachMonHoc[i].maMH == thongtin or danhSachMonHoc[i].tenMH == thongtin or danhSachMonHoc[i].soTC == int(thongtin)):
            danhSachMonHoc[i].hienThiMonHoc()
        else:
            print("khong có thông tin môn học cần tìm")


def GhiDSVaoTep():
    with open("MonHoc.txt","w") as file:
        n = len(danhSachMonHoc)
        file.write(str(n) + "\n")
        for i in range(n):
            file.write(danhSachMonHoc[i].maMH + "\n")
            file.write(danhSachMonHoc[i].tenMH + "\n")
            file.write(str(danhSachMonHoc[i].soTC) + "\n")


def docDSMonHoc():
    with open("MonHoc.txt","r") as file:
        n = int(file.readline())
        print("Số lượng môn học là: ", n)
        for i in range(n):
            print("mã môn học", file.readline())
            print("tên môn học", file.readline())
            print("số tín chỉ", file.readline())



def main():

    while True:
        print("1. Nhập danh sách môn học")
        print("2. Đọc danh sách môn học từ tệp")
        print("3. Hiển thị danh sách môn học")
        print("4. Thêm một môn học mới")
        print("5. Xoá một môn học theo mã")
        print("6. Tìm kiếm môn học")
        print("7. Lưu")
        print("Thoát")

        chon = int(input("\nMời bạn chọn chức năng [1-7]"))
        if chon == 1:
            nhapDanhSachMonHoc()
        elif chon == 2:
            print("\nDanh sách môn học từ tệp")
            docDSMonHoc()
        elif chon == 3:
            hienThiDSMonHoc()
        elif chon == 4:
            ThemMonHoc()
            print("\nDanh sách môn học sau khi thêm")
            hienThiDSMonHoc()
        elif chon == 5:
            ma_del = input('Nhập mã cần xoá: ')
            XoaMonHoc(ma_del)
            print("\nDanh sách môn học sau khi xoá mã: ", ma_del)
            hienThiDSMonHoc()
        elif chon == 6:
            thongtin = input("\nMời bạn nhập vào thông tin cần tìm: ")
            TimkiemThongTin(thongtin)
        elif chon == 6:
            GhiDSVaoTep()
        else:
            break

        

main()