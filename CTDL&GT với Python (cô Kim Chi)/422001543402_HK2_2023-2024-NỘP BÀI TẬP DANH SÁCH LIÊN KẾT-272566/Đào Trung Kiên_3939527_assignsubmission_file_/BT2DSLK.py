class Nut:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.nut_ke_tiep = None

class DSLienket:
    def __init__(self):
        self.dau = None
        self.duoi = None

    def them_cuoi(self, gia_tri):
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        else:
            self.duoi.nut_ke_tiep = nut
            self.duoi = nut

    def them_truoc(self, gia_tri, gia_tri_truoc):
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        elif self.dau.gia_tri == gia_tri_truoc:
            nut.nut_ke_tiep = self.dau
            self.dau = nut
        else:
            hien_tai = self.dau
            while hien_tai.nut_ke_tiep != None:
                if hien_tai.nut_ke_tiep.gia_tri == gia_tri_truoc:
                    nut.nut_ke_tiep = hien_tai.nut_ke_tiep
                    hien_tai.nut_ke_tiep = nut
                    return
                hien_tai = hien_tai.nut_ke_tiep
            print(f"Không tìm thấy giá trị {gia_tri_truoc} trong danh sách.")

    def in_ds(self):
        if self.dau == None:
            print("Danh sách rỗng.")
            return
        hien_tai = self.dau
        while hien_tai != None:
            print(hien_tai.gia_tri, end=" ")
            hien_tai = hien_tai.nut_ke_tiep
        print()

    def in_ds_nguoc(self):
        if self.dau == None:
            print("Danh sách rỗng.")
            return
        arr = []
        hien_tai = self.dau
        while hien_tai != None:
            arr.append(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        arr.reverse()
        for gia_tri in arr:
            print(gia_tri, end=" ")
        print()

    def tim_max_min(self):
        if self.dau == None:
            return None, None
        max_value = min_value = self.dau.gia_tri
        hien_tai = self.dau.nut_ke_tiep
        while hien_tai != None:
            if hien_tai.gia_tri > max_value:
                max_value = hien_tai.gia_tri
            if hien_tai.gia_tri < min_value:
                min_value = hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return max_value, min_value

    def tong_so_am_duong(self):
        if self.dau == None:
            return 0, 0
        tong_am = tong_duong = 0
        hien_tai = self.dau
        while hien_tai != None:
            if hien_tai.gia_tri < 0:
                tong_am += hien_tai.gia_tri
            else:
                tong_duong += hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return tong_am, tong_duong

    def tich_so(self):
        if self.dau == None:
            return 0
        tich = 1
        hien_tai = self.dau
        while hien_tai != None:
            tich *= hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return tich

    def tong_binh_phuong(self):
        if self.dau == None:
            return 0
        tong_binh_phuong = 0
        hien_tai = self.dau
        while hien_tai != None:
            tong_binh_phuong += hien_tai.gia_tri ** 2
            hien_tai = hien_tai.nut_ke_tiep
        return tong_binh_phuong

    def so_nguyen_to_cua_x(self, x):
        if self.dau == None:
            print("Danh sách rỗng.")
            return
        print(f"Các số nguyên tố của {x} trong danh sách là:")
        hien_tai = self.dau
        while hien_tai != None:
            if self.kiem_tra_so_nguyen_to(hien_tai.gia_tri) and hien_tai.gia_tri % x == 0:
                print(hien_tai.gia_tri, end=" ")
            hien_tai = hien_tai.nut_ke_tiep
        print()

    def uoc_so_cua_x(self, x):
        if self.dau == None:
            print("Danh sách rỗng.")
            return
        print(f"Các ước số của {x} trong danh sách là:")
        hien_tai = self.dau
        while hien_tai != None:
            if x % hien_tai.gia_tri == 0:
                print(hien_tai.gia_tri, end=" ")
            hien_tai = hien_tai.nut_ke_tiep
        print()

    def gia_tri_dau_tien_lon_hon_x(self, x):
        if self.dau == None:
            print("Danh sách rỗng.")
            return
        hien_tai = self.dau
        while hien_tai != None:
            if hien_tai.gia_tri > x:
                return hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        print("Không có giá trị nào lớn hơn", x, "trong danh sách.")

    def so_nguyen_to_cuoi_cung(self):
        if self.dau == None:
            print("Danh sách rỗng.")
            return
        nguyen_to_cuoi_cung = None
        hien_tai = self.dau
        while hien_tai != None:
            if self.kiem_tra_so_nguyen_to(hien_tai.gia_tri):
                nguyen_to_cuoi_cung = hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        if nguyen_to_cuoi_cung:
            print("Số nguyên tố cuối cùng trong danh sách là:", nguyen_to_cuoi_cung)
        else:
            print("Không có số nguyên tố trong danh sách.")

    def dem_so_nguyen_to(self):
        if self.dau == None:
            print("Danh sách rỗng.")
            return
        count = 0
        hien_tai = self.dau
        while hien_tai != None:
            if self.kiem_tra_so_nguyen_to(hien_tai.gia_tri):
                count += 1
            hien_tai = hien_tai.nut_ke_tiep
        print("Số lượng số nguyên tố trong danh sách là:", count)

    def kiem_tra_sap_tang(self):
        if self.dau == None:
            return False
        hien_tai = self.dau
        while hien_tai.nut_ke_tiep != None:
            if hien_tai.gia_tri > hien_tai.nut_ke_tiep.gia_tri:
                return False
            hien_tai = hien_tai.nut_ke_tiep
        return True

    def kiem_tra_doi_xung(self):
        if self.dau == None:
            return False
        arr = []
        hien_tai = self.dau
        while hien_tai != None:
            arr.append(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        return arr == arr[::-1]

    def xoa_cuoi(self):
        if self.dau == None:
            print("Danh sách rỗng.")
            return
        if self.dau.nut_ke_tiep == None:
            self.dau = self.duoi = None
            return
        hien_tai = self.dau
        while hien_tai.nut_ke_tiep != self.duoi:
            hien_tai = hien_tai.nut_ke_tiep
        hien_tai.nut_ke_tiep = None
        self.duoi = hien_tai

    def xoa_dau(self):
        if self.dau == None:
            print("Danh sách rỗng.")
            return
        self.dau = self.dau.nut_ke_tiep
        if self.dau == None:
            self.duoi = None

    def huy_toan_bo(self):
        self.dau = self.duoi = None

    def kiem_tra_so_nguyen_to(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

