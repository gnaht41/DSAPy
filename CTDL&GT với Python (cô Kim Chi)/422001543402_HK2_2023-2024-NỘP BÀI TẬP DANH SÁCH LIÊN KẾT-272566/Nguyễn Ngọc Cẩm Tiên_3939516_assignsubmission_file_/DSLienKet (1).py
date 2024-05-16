#TAO NÚT
class Nut:
    def __init__(self,gia_tri):
        self.gia_tri = gia_tri
        self.nut_ke_tiep= None

    #def Định nghĩa hàm khởi tạo node
    #class
class DSLienKet:
    def __init__(self):
        self.dau = None
        self.duoi= None

    #def
    def in_ds(self):
        stt =0
        hien_tai=self.dau
        kq= 'DS['
        while hien_tai != None:
            stt += 1
            if stt ==1:
                kq += '' + str(hien_tai.gia_tri)
            else:
                kq += '->' + str(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        kq += ']'
        print(kq)
    #def
    def them(self,gia_tri):
        nut= Nut(gia_tri)
        if self.dau==None: #thêm đầu
            self.dau =nut
            self.duoi =nut
        else:#thêm cuối
            self.duoi.nut_ke_tiep=nut
            self.duoi =nut
    

    def chen(self, chi_muc, gia_tri):
        nut = Nut(gia_tri)
        truoc = None
        hien_tai =self.dau
        i=0
        while i < chi_muc and hien_tai != None:
            i +=1
            truoc = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
        if truoc == None:
            # them vao dau ds
            nut.nut_ke_tiep = self.dau
            self.dau = nut
            if self.duoi ==None:
                self.duoi = nut
        else:
            if hien_tai == None:
                #them vao cuoi ds
                self.duoi.nut_ke_tiep =nut
                self.duoi = nut
            else:
                #them vao giua ds
                truoc.nut_ke_tiep = nut
                nut.nut_ke_tiep = hien_tai
    
    
    def tim(self, gia_tri):
        hien_tai = self.dau
        vi_tri = 0
        while hien_tai != None and hien_tai.gia_tri != gia_tri:
            hien_tai = hien_tai.nut_ke_tiep
            vi_tri += 1
        if hien_tai == None:
            return None
        else:
            return vi_tri
    
    
    def xoa(self, gia_tri):
        hien_tai = self.dau
        truoc = None
        while hien_tai != None and hien_tai.gia_tri != gia_tri:
            truoc = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
        if hien_tai != None:
            #tim thay
            if hien_tai == self.dau and hien_tai == self.duoi:
                #xoa phan tu duy nhat
                self.dau = self.duoi = None
            elif hien_tai == self.dau:
                # xoa phan tu dau tien khong duy nhat
                self.dau = self.dau.nut_ke_tiep
            elif hien_tai == self.duoi:
                # xoa phan tu duoi vaf khong duy nhat
                truoc.nut_ke_tiep = None
                self.duoi = truoc
            else:
                # xoa o giua
                truoc.nut_ke_tiep = hien_tai.nut_ke_tiep
            del hien_tai
    
    def cap_nhat(self,vi_tri, gia_tri):
        hien_tai = self.dau
        i=0
        while i < vi_tri and hien_tai != None:
            i +=1
            hien_tai = hien_tai.nut_ke_tiep
        if hien_tai != None:
            hien_tai.gia_tri = gia_tri
    
    
    def xoa_het(self):
        hien_tai = self.dau
        self.dau = self.duoi = None
        while hien_tai != None:
            tam = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
            del tam
            
    def in_ds_nguoc(self):
        hien_tai = self.dau
        while hien_tai:
            print(hien_tai.gia_tri, duoi=" ")
            hien_tai = hien_tai.nut_ke_tiep
        print()
        
    def tim_min_max(self):
        if not self.dau:
            return None, None
        hien_tai = self.dau
        min_val = max_val = hien_tai.gia_tri
        while hien_tai:
            if hien_tai.gia_tri < min_val:
                min_val = hien_tai.gia_tri
            if hien_tai.gia_tri > max_val:
                max_val = hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return min_val, max_val
    
    def dem_sAm_sDuong(self):
        if not self.dau:
            return 0, 0
        hien_tai = self.dau
        so_duong = so_am = 0
        while hien_tai:
            if hien_tai.gia_tri > 0:
                so_duong += 1
            elif hien_tai.gia_tri < 0:
                so_am += 1
            hien_tai = hien_tai.nut_ke_tiep
        return so_duong, so_am
            
    def tich_so(self):
        if not self.dau:
            return 0
        kq = 1
        hien_tai = self.dau
        while hien_tai:
            kq *= hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return kq
    
    def tong_binh_phuong(self):
        if not self.dau:
            return 0
        kq = 0
        hien_tai = self.dau
        while hien_tai:
            kq += pow(hien_tai.gia_tri, 2)
            hien_tai = hien_tai.nut_ke_tiep
        return kq
    
    def tim_so_ngto(self, x):
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        hien_tai = self.dau
        prime_factors = []
        while hien_tai:
            if x % hien_tai.gia_tri == 0 and is_prime(hien_tai.gia_tri):
                prime_factors.append(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        return prime_factors
    
    def tim_uoc_so(self, x):
        divisors = []
        hien_tai = self.dau
        while hien_tai:
            if x % hien_tai.gia_tri == 0:
                divisors.append(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        return divisors

    def tim_gia_tri_dau(self, x):
        hien_tai = self.dau
        while hien_tai:
            if hien_tai.gia_tri > x:
                return hien_tai.gia_tri
            hien_tai = hien_tai.nut_ke_tiep
        return None
    
    def dem_so_ngto(self):
        count = 0
        hien_tai = self.dau
        while hien_tai:
            if self.is_prime(hien_tai.gia_tri):
                count += 1
            hien_tai = hien_tai.nut_ke_tiep
        return count