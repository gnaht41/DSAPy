class Nut:
    def __init__(self, giaTri):
        self.giaTri = giaTri
        self.nutKeTiep = None


class DSLK:
    def __init__(self):
        self.dau = None
        self.cuoi = None

    def themDS(self, giaTri):
        nut = Nut(giaTri)
        if self.dau == None:
            self.dau = nut
            self.cuoi = nut
        else:
            self.cuoi.nutKeTiep = nut
            self.cuoi = nut

    def inDS(self):
        dauTien = self.dau
        vt = 0
        kt = "["
        while dauTien != None:
            vt += 1
            if vt == 1:
                kt += str(dauTien.giaTri)
            else:
                kt += "," + str(dauTien.giaTri)
            dauTien = dauTien.nutKeTiep
        kt += "]"
        print(kt)

    def chenDS(self, chiMuc, giaTri):
        nut = Nut(giaTri)
        hienTai = self.dau
        vt = 0
        truoc = None
        while vt < chiMuc and hienTai != None:
            vt += 1
            truoc = hienTai
            hienTai = hienTai.nutKeTiep
        if truoc == None:
            nut.nutKeTiep = self.dau
            self.dau = nut
            if self.cuoi == None:
                self.duoi = nut
        else:
            if hienTai == None:
                self.cuoi.nutKeTiep = nut
                self.cuoi = nut
            else:
                truoc.nutKeTiep = nut
                nut.nutKeTiep = hienTai

    def timDS(self, giaTri):
        hienTai = self.dau
        vt = 0
        while hienTai != None and hienTai.giaTri != giaTri:
            hienTai = hienTai.nutKeTiep
            vt += 1
        if hienTai == None:
            return None
        return vt

    def xoaDS(self, giaTri):
        hienTai = self.dau
        truoc = None
        while hienTai != None and hienTai.giaTri != giaTri:
            truoc = hienTai
            hienTai = hienTai.nutKeTiep
        if hienTai != None:
            if hienTai == self.dau and hienTai == self.cuoi:
                self.dau = self.cuoi = None
            elif hienTai == self.dau:
                self.dau = self.dau.nutKeTiep
            elif hienTai == self.cuoi:
                truoc.nutKeTiep = None
                self.cuoi = truoc
            else:
                truoc.nutKeTiep = hienTai.nutKeTiep

    def capNhatDS(self, viTri, giaTri):
        hienTai = self.dau
        vt = 0
        while vt < viTri and hienTai.giaTri != giaTri:
            vt += 1
            hienTai = hienTai.nutKeTiep
        if hienTai != None:
            hienTai.giaTri = giaTri

    def xoaHet(self):
        hienTai = self.dau
        self.dau = self.cuoi = None
        while hienTai != None:
            tam = hienTai
            hienTai = hienTai.nutKeTiep
            del tam


def main():
    ds = DSLK()
    print("Thêm các số")
    ds.themDS(1)
    ds.themDS(2)
    ds.themDS(3)
    print("------------")
    print("In danh sách: ")
    ds.inDS()
    print("------------")
    print("Chèn vào danh sách: ")
    ds.chenDS(1, 4)
    ds.inDS()
    print("------------")
    print("Tìm giá trị trong danh sách: ")
    print(ds.timDS(2))
    print("------------")
    print("Xóa số 2 trong danh sách")
    ds.xoaDS(2)
    ds.inDS()
    print("------------")
    print("Cập nhật lại số 5 tại vị trí 1")
    ds.capNhatDS(1, 5)
    ds.inDS()
    print("------------")
    ds.xoaHet()
    ds.inDS()


if __name__ == "__main__":
    main()
