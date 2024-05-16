'''
Định nghĩa lớp DSLienKet mô tả 1 danh sách liên kết các phương thức
__init__(self): khởi tạo
__str__(self):
them_dau(self, gia_tri):
them_duoi(self, gia_tri):
lay_dau(self):
xoa_dau(self):
'''
#TAO NÚT
class Nut:
    def __init__(self,gia_tri):
        self.gia_tri = gia_tri
        self.nut_ke_tiep= None
    #def Định nghĩa hàm khởi tạo node
#class
class DSLienKetHD:
    def __init__(self):
        self.dau = None
        self.duoi= None
    #def
    #đổi về chuỗi
    def __str__(self):
        kq= ''
        stt =0
        hien_tai=self.dau
        while hien_tai != None:
            stt += 1
            if stt ==1:# phần tử đầu tiên
                kq += '' + str(hien_tai.gia_tri)
            else:
                kq += '->' + str(hien_tai.gia_tri)
            #if
            hien_tai = hien_tai.nut_ke_tiep
        #while
        return kq
    #def
    #Thêm đẫu
    def them_dau(self, gia_tri):
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        else:
            nut.nut_ke_tiep - self.dau
            self.dau = nut
        #if
    #def
    #Them duoi
    def them_duoi(self, gia_tri):
        nut = Nut(gia_tri)
        if self.dau ==None :#Nút dâu tiên
            self.dau = nut
            self.duoi = nut
        else: #không phải là nút đãu tiên
            self.duoi.nut_ke_tiep = nut
            self.duoi =nut
        #if
    #def
    #Lấy giá trị phân từ dâu tiên
    def lay_dau(self):
        if self.dau == None:
            return None
        else:
            return self.dau.gia_tri
        #if
    #def
    #xoa dau
    def xoa_dau(self):
        tam = self.dau
        if self.dau == self.duoi:
            self.dau = None
            self.duoi = None
        else:
            self.dau = self.dau.nut_ke_tiep
        #if
        del tam
    #def
#class