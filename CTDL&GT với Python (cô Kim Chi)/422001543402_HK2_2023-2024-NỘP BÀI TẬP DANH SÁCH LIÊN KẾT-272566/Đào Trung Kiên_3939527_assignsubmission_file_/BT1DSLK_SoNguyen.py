class Nut:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.nut_ke_tiep = None

class DSLienket:
    def __init__(self):
        self.dau = None
        self.duoi = None

    def them(self, gia_tri):
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        else:
            self.duoi.nut_ke_tiep = nut
            self.duoi = nut

    def so_luong_phan_tu(self):
        count = 0
        hien_tai = self.dau
        while hien_tai != None:
            count += 1
            hien_tai = hien_tai.nut_ke_tiep
        return count

    def tong_gia_tri(self):
        total = 0
        hien_tai = self.dau
        while hien_tai != None:
            total += hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return total

    def max_min(self):
        max_value = min_value = self.dau.gia_tri
        hien_tai = self.dau.nut_ke_tiep
        while hien_tai != None:
            if hien_tai.gia_tri > max_value:
                max_value = hien_tai.gia_tri
            if hien_tai.gia_tri < min_value:
                min_value = hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return max_value, min_value

    def sap_xep_tang(self):
        arr = []
        hien_tai = self.dau
        while hien_tai != None:
            arr.append(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        arr.sort()
        return arr

    def sap_xep_giam(self):
        arr = []
        hien_tai = self.dau
        while hien_tai != None:
            arr.append(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        arr.sort(reverse=True)
        return arr

    def so_chan(self):
        chan = []
        hien_tai = self.dau
        while hien_tai != None:
            if hien_tai.gia_tri % 2 == 0:
                chan.append(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        return chan

    def tim_gia_tri(self, gia_tri):
        hien_tai = self.dau
        while hien_tai != None:
            if hien_tai.gia_tri == gia_tri:
                return True
            hien_tai = hien_tai.nut_ke_tiep
        return False
