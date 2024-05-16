class Sach:
    def __init__(self, ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia):
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.nha_xuat_ban = nha_xuat_ban
        self.nam_xuat_ban = nam_xuat_ban
        self.gia = gia
        self.next = None

class ThuVien:
    def __init__(self):
        self.head = None

    def them_sach_dau(self, ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia):
        sach_moi = Sach(ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)
        if self.head is None:
            self.head = sach_moi
        else:
            sach_moi.next = self.head
            self.head = sach_moi

    def them_sach_cuoi(self, ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia):
        sach_moi = Sach(ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)
        if self.head is None:
            self.head = sach_moi
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = sach_moi

    def xuat_danh_sach_sach(self):
        if self.head is None:
            print("Danh sách sách trong thư viện rỗng.")
            return
        current = self.head
        while current:
            print("Tên sách:", current.ten_sach)
            print("Tác giả:", current.tac_gia)
            print("Nhà xuất bản:", current.nha_xuat_ban)
            print("Năm xuất bản:", current.nam_xuat_ban)
            print("Giá:", current.gia)
            print("-------------------------")
            current = current.next

    def so_luong_sach_tac_gia(self, ten_tac_gia):
        count = 0
        current = self.head
        while current:
            if ten_tac_gia in current.tac_gia:
                count += 1
            current = current.next
        return count

    def sach_theo_nam_nxb(self, nam_xuat_ban, nha_xuat_ban):
        sach_phathanh = []
        current = self.head
        while current:
            if current.nam_xuat_ban == nam_xuat_ban and current.nha_xuat_ban == nha_xuat_ban:
                sach_phathanh.append(current.ten_sach)
            current = current.next
        return sach_phathanh

    def tim_sach_va_them_moi(self, ten_sach_can_tim, ten_sach_moi, tac_gia, nha_xuat_ban, nam_xuat_ban, gia):
        current = self.head
        while current:
            if current.ten_sach == ten_sach_can_tim:
                print("Sách đã tồn tại trong thư viện.")
                return
            current = current.next
        print("Sách chưa có trong thư viện.")
        them_sach_moi = input("Bạn có muốn thêm sách mới không? (yes/no): ")
        if them_sach_moi.lower() == 'yes':
            self.them_sach_cuoi(ten_sach_moi, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)

    def xoa_sach_dau(self):
        if self.head is None:
            print("Danh sách sách trong thư viện rỗng.")
            return
        self.head = self.head.next

    def xoa_sach_cuoi(self):
        if self.head is None:
            print("Danh sách sách trong thư viện rỗng.")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def xoa_sach_theo_ten(self, ten_sach_can_xoa):
        if self.head is None:
            print("Danh sách sách trong thư viện rỗng.")
            return
        if self.head.ten_sach == ten_sach_can_xoa:
            self.head = self.head.next
            return
        previous = self.head
        current = self.head.next
        while current:
            if current.ten_sach == ten_sach_can_xoa:
                previous.next = current.next
                return
            previous = current
            current = current.next
        print("Không tìm thấy sách có tên", ten_sach_can_xoa, "trong thư viện.")

# Hàm chính
