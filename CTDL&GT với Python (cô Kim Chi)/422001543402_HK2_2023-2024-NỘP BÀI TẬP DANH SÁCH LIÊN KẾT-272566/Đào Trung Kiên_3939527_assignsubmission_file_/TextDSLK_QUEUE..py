from DSLK_QUEUE import DSLienKetHD

class HangDoi:
    #Queue
    def __init__(self):
        self.danh_sach = DSLienKetHD()
    #def
    def __str__(self):
        kq= 'Hang Doi ['
        kq= kq + str(self.danh_sach)
        kq= kq +']'
        return kq
    #def
    #Kiến tra hàng dại rõng
    def la_rong(self):
        #is empty
        return self.danh_sach.dau == None
    #def

    def xep_hang(self,gia_tri):
        #enqueue
        self.danh_sach.them_duoi(gia_tri)
    #def
    #Lấy ra
    def ra_hang(self):
        #dequeue
        if self.la_rong():
            return None
        else:
            kq = self.danh_sach.lay_dau()# lay ra nhưng chưa xoá
            self.danh_sach.xoa_dau()
            return kq
        #if
    #def
#class
if __name__ =='__main__':
    hang_doi = HangDoi()
    print(hang_doi)

    print('-------Xep hang-------')
    for x in range(1,6):
        print(f'* Xếp hạng {x}')
        hang_doi.xep_hang(x)
        print(hang_doi)
    #for
        
    print('-------Ra hang-------')
    while not hang_doi.la_rong():
        gt = hang_doi.ra_hang()
        print(f'* Ra hàng ->{gt}')
        print(hang_doi)
    #while
#if