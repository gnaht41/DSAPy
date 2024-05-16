class Nut:
    def __init__(self, giatri):
        self.giatri = giatri
        self.nut_ke_tiep = None
class DSLK:
    def __init__(self):
        self.dau = None
        self.duoi = None
    def them(self, giatri):
        nut = Nut(giatri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        else:
            self.duoi.nut_ke_tiep = nut
            self.duoi = nut
            
    def inds(self):
        dautien = self.dau
        vt = 0
        kq = '['
        while dautien != None:
            vt += 1
            if vt == 1:
                kq += str(dautien.giatri)
            else:
                kq += ', ' + str(dautien.giatri)
            dautien = dautien.nut_ke_tiep
        kq += ']'
        print(kq)
        
    def chen(self, chi_muc, gia_tri):
        nut = Nut(gia_tri)
        truoc = None
        hien_tai = self.dau
        i = 0
        while i < chi_muc and hien_tai != None:
            i += 1
            truoc = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
        if truoc == None:
            nut.nut_ke_tiep = self.dau
            self.dau = nut
            if self.duoi == None:
                self.duoi = nut
        else:
            if hien_tai == None:
                self.duoi.nut_ke_tiep = nut
                self.duoi = nut
            else:
                truoc.nut_ke_tiep = nut
                nut.nut_ke_tiep = hien_tai
    
    def tim_ds(self, gia_tri):
        hien_tai = self.dau
        vi_tri = 0
        while hien_tai != None and hien_tai.giatri != gia_tri:
            hien_tai = hien_tai.nut_ke_tiep
            vi_tri += 1
        if hien_tai == None:
            return None
        else:
            return vi_tri
    def xoa(self, gia_tri):
        hien_tai = self.dau
        truoc = None
        while hien_tai != None and hien_tai.giatri != gia_tri:
            truoc = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
        if hien_tai != None:
            # Tim thay
            if hien_tai == self.dau and hien_tai == self.duoi:
            # Chi co mot gia tri
                self.dau = self.duoi = None
            elif hien_tai == self.dau:
            # Gia tri dau va co gia tri sau
                self.dau == self.dau.nut_ke_tiep
            elif hien_tai == self.duoi:
            # Gia tri cuoi va co gia tri truoc do
                truoc.nut_ke_tiep = None
                self.duoi = truoc
            else:
                # Gia tri nam o giua
                truoc.nut_ke_tiep = hien_tai.nut_ke_tiep
    
    def cap_nhat(self, vi_tri, gia_tri):
        hien_tai = self.dau
        i = 0
        while i < vi_tri and hien_tai != None:
            i += 1
            hien_tai = hien_tai.nut_ke_tiep
        if hien_tai != None:
            hien_tai.giatri = gia_tri
            
    def xoa_het(self):
        hien_tai = self.dau
        self.dau = self.duoi = None
        while hien_tai != None:
            tam = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
            del tam
        
    
