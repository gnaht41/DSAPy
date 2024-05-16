class Nut:
    # Định nghĩa lớp nút
    def __init__(self, khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai = None
    # def

    def chen(self, khoa):
        if self is None:
            nut = Nut(khoa)
            self = nut
            return
        # if Nút chưa được khởi tạo
        # nút đã khởi tạo rồi,Nút khác None
        if khoa < self.khoa:
            if self.trai == None:
                self.trai = Nut(khoa)  # Nút trái chưa có giá tri
            else:  # Nút trái đã có giá trị
                self.trai.chen(khoa)
            # if
        elif khoa > self.khoa:
            if self.phai == None:
                self.phai = Nut(khoa)  # Tạo 1 nút mới
            else:
                # có nút bên phải rồi
                self.phai.chen(khoa)  # gọi đệ quy
            # if
        else:
            # Không lớn hơn hay không nhỏ hơn, bị trùng khoá
            print(f'Bị trùng khoá {khoa}')
        # if
    # def
# class Nut
# Định nghĩa lớp cây nhị phân tìm kiếm


class CayNhiPhanTimKiem:
    def __init__(self, khoa=None):
        if khoa == None:  # Không truyền vào tham số
            self.goc = None
        else:
            self.goc = Nut(khoa)
        # if
    # def
    # Chèn vào 1 giá trị khoá

    def chen(self, khoa):
        if self.goc == None:
            self.goc = Nut(khoa)
        else:  # Có nút rồi
            self.goc.chen(khoa)
        # if
    # def Chèn 1 nút vào cây
    # Xoá 1 nút

    def xoa(self, khoa):
        nut_cha = None
        cha_con = None
        nut_ht = self.goc
        # tìm nút xoá,
        # Các trường hợp xoá nút lá, xoá nút có 1 con trái, xoá nút có 1 con phải, xoá nút có cả 2 con, xoá nút gốc
        while nut_ht != None:
            if nut_ht.khoa > khoa:  # khoá xoá nhỏ hơn
                nut_cha = nut_ht
                nut_ht = nut_ht.trai  # tìm nhánh bên trái
                cha_con = 'trai'
            elif nut_ht.khoa < khoa:
                nut_cha = nut_ht
                nut_ht = nut_ht.phai
                cha_con = 'phai'
            else:  # bằng, tìm thấy nghĩa là xoá nút này
                if nut_cha == None:  # Nút gốc
                    # xoá nút gốc
                    # Nếu nút gốc không có 2 con
                    if nut_ht.trai == None and nut_ht.phai == None:
                        # xoá nút gốc mà không có con
                        self.goc = None
                    # if
                    elif nut_ht.trai == None:
                        # Nút trái không có con, xoá nút gốc chỉ có 1 nút con bên phải
                        self.goc = nut_ht.phai
                    elif nut_ht.phai == None:
                        # xoá nút chỉ có 1 con bên trái
                        self.goc = nut_ht.trai
                    else:
                        # xoá nút gốc có đủ 2 con
                        # xoay trái
                        self.goc = nut_ht.phai
                        tam = self.goc
                        while tam.trai != None:  # Truy tìm đến cực trái để gắn nhánh trái xuống bên trái của nút cực trái
                            tam = tam.trai
                        # while
                        tam.trai = nut_ht.trai
                    # if
                elif nut_ht.trai == None and nut_ht.phai == None:
                    # Không phải nút gốc. Xoá nút lá, không có con trái và phải
                    if cha_con == 'trai':
                        nut_cha.trai = None
                    else:
                        nut_cha.phai = None
                    # if
                elif nut_ht.trai == None:
                    # Không phải nút là mà là nút giữa.
                    # Xoá nút chỉ có 1 con bên phai
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                    # if
                elif nut_ht.phai == None:
                    # xoá nút giữa chỉ có 1 con bên trái
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.trai
                    else:
                        nut_cha.phai = nut_ht.trai
                else:
                    # xoá nút có đủ 2 con
                    # xoay trái
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                    # if
                    if nut_ht.phai.trai == None:
                        nut_ht.phai.trai = nut_ht.trai
                    else:  # nút chưa là None, truy tìm nút tận cùng bên trái
                        tam = nut_ht.phai
                        while tam.trai != None:
                            tam = tam.trai
                        # while
                        tam.trai = nut_ht.trai
                    # if
                # if
                del nut_ht
                break
                # if
        # while
    # def
    # Duyệt cây

    def duyet_trai_nut_phai(self, goc=0):
        # Duyệt theo LNR
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        # if
        # kiểm tra nút hiện tại có bằng None không
        if nut_ht == None:
            return []
        else:  # cây có giá trị
            kq = []
            kq_trai = self.duyet_trai_nut_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            # For duyệt trái
            kq.append(nut_ht.khoa)
            # Duyệt phải
            kq_phai = self.duyet_trai_nut_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            # for
            return kq
        # if
    # def
    # =============================
    # Duyet NLR

    def duyet_nut_trai_phai(self, goc=0):
        # Duyệt theo NLR
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        # if
        # kiểm tra nút hiện tại có bằng None không
        if nut_ht == None:
            return []
        else:  # cây có giá trị
            kq = []
            kq.append(nut_ht.khoa)
            kq_trai = self.duyet_nut_trai_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            # For duyệt trái

            # Duyệt phải
            kq_phai = self.duyet_nut_trai_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            # for
            return kq
        # if
    # def
# ======================Duyệt LPN

    def duyet_trai_phai_nut(self, goc=0):
        # Duyệt theo LRN
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        # if
        # kiểm tra nút hiện tại có bằng None không
        if nut_ht == None:
            return []
        else:  # cây có giá trị
            kq = []
            kq_trai = self.duyet_trai_phai_nut(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            # For duyệt trái

            # Duyệt phải
            kq_phai = self.duyet_trai_phai_nut(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            # Not
            kq.append(nut_ht.khoa)
            # for
            return kq
        # if
    # def
    # Tìm

    def tim(self, khoa):
        if self.goc == None:
            # Cây rỗng
            return
        # if
        nut_ht = self.goc
        kq = ''
        while (nut_ht != None and nut_ht.khoa != khoa):
            kq = kq + f'{nut_ht.khoa} -> '
            if khoa <= nut_ht.khoa:
                nut_ht = nut_ht.trai  # Đi tìm bên nhánh trái
            else:
                nut_ht = nut_ht.phai  # đi về bên phải
            # if
        # while
        if nut_ht == None:  # Tìm không thấy
            return None
        else:  # Tìm thấy
            kq = kq + f'{nut_ht.khoa}'
            return kq
        # if
    # def
 # class
# Hàm main


def main():
    SO_PHAN_TU = 10
    cay = CayNhiPhanTimKiem()
    print('******Chèn vào cây**********')
    tap_gia_tri = set()
    from random import randint
    while len(tap_gia_tri) < SO_PHAN_TU:
        # Lấy 10 phần tử không trùng nhau nên dùng tập hợp
        gt = randint(1, 100)
        tap_gia_tri.add(gt)
    # while
    tap_gia_tri = list(tap_gia_tri)  # Phát sinh danh sách ngẫu nhiên
    # tap_gia_tri = [66,46,84,11,81, 99,36,77,83, 87,100, 86, 85]
    print('Chèn lần lượt', tap_gia_tri)
    for x in tap_gia_tri:
        cay.chen(x)
    kq = cay.duyet_trai_nut_phai()
    print('********Duyệt cây theo Trai - Nut - Phai (LNR):', kq)

    kq = cay.duyet_nut_trai_phai()
    print('********Duyệt cây theo  Nut - Trai -Phai (NLR):', kq)

    kq = cay.duyet_trai_phai_nut()
    print('********Duyệt cây theo  Trai -Phai - Nut (LRN):', kq)
    gt = int(input('Nhập vào giá trị cần xoá '))
    print(f'Xoa {gt}')
    cay.xoa(gt)
    kq = cay.duyet_trai_nut_phai()
    print('********Duyệt cây theo Trai - Nut - Phai (LNR):', kq)

    kq = cay.duyet_nut_trai_phai()
    print('********Duyệt cây theo  Nut - Trai -Phai (NLR):', kq)

    kq = cay.duyet_trai_phai_nut()
    print('********Duyệt cây theo  Trai -Phai - Nut (LRN):', kq)
    # Tìm
    while True:
        nhap = input('Nhập vào khoá cần tìm ')
        if nhap == '':
            break
        # if
        gt = int(nhap)
        kq = cay.tim(gt)
        if kq == None:
            print(f'Không tim thấy {gt}')
        else:  # Tìm thấy
            print(f'Tìm thấy {gt}:{kq}')


        # if
    # while
# def
if __name__ == '__main__':
    main()
# if


# def
