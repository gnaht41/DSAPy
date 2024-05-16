class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Sach:
    def __init__(self, ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia):
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.nha_xuat_ban = nha_xuat_ban
        self.nam_xuat_ban = nam_xuat_ban
        self.gia = gia

class ThuVien:
    def __init__(self):
        self.head = None

    def them_sach(self, sach):
        new_node = Node(sach)
        if not self.head:
            self.head = new_node
            return "Sách đã được thêm vào danh sách."
        current = self.head
        while current.next:
            if current.data.ten_sach == sach.ten_sach:
                return "Sách đã tồn tại. Vui lòng nhập tên khác."
            current = current.next
        if current.data.ten_sach == sach.ten_sach:
            return "Sách đã tồn tại. Vui lòng nhập tên khác."
        current.next = new_node
        return "Sách đã được thêm vào danh sách."

    def them_sach_dau_danh_sach(self, sach):
        new_node = Node(sach)
        if not self.head:
            self.head = new_node
            return "Sách đã được thêm vào đầu danh sách."
        if self.head.data.ten_sach == sach.ten_sach:
            return "Sách đã tồn tại. Vui lòng nhập tên khác."
        new_node.next = self.head
        self.head = new_node
        return "Sách đã được thêm vào đầu danh sách."

    def xuat_danh_sach_sach(self):
        if not self.head:
            print("Danh sách sách trống.")
        else:
            current = self.head
            while current:
                sach = current.data
                print(f"Tên sách: {sach.ten_sach}, Tác giả: {', '.join(sach.tac_gia)}, Nhà xuất bản: {sach.nha_xuat_ban}, Năm xuất bản: {sach.nam_xuat_ban}, Giá: {sach.gia}")
                current = current.next

    def dem_so_luong_sach_theo_tac_gia(self, tac_gia_can_dem):
        count = 0
        current = self.head
        while current:
            if tac_gia_can_dem in current.data.tac_gia:
                count += 1
            current = current.next
        return count

    def tim_sach_theo_nxb_va_nam(self, nxb, nam_xuat_ban):
        sach_tim_thay = []
        current = self.head
        while current:
            if current.data.nha_xuat_ban == nxb and current.data.nam_xuat_ban == nam_xuat_ban:
                sach_tim_thay.append(current.data)
            current = current.next
        return sach_tim_thay

    def tim_va_them_sach_moi(self, ten_sach_can_tim):
        current = self.head
        while current:
            if current.data.ten_sach == ten_sach_can_tim:
                print(f"Sách đã được tìm thấy: Tên sách: {current.data.ten_sach}, Tác giả: {', '.join(current.data.tac_gia)}, Nhà xuất bản: {current.data.nha_xuat_ban}, Năm xuất bản: {current.data.nam_xuat_ban}, Giá: {current.data.gia}")
                return self.them_sach_moi()
            current = current.next
        print("Không tìm thấy sách.")

    def them_sach_moi(self):
        ten_sach = input("Nhập tên sách mới: ")
        tac_gia = input("Nhập tác giả (các tác giả cách nhau bởi dấu phẩy): ").split(',')
        nha_xuat_ban = input("Nhập nhà xuất bản: ")
        nam_xuat_ban = int(input("Nhập năm xuất bản: "))
        gia = int(input("Nhập giá sách: "))
        sach_moi = Sach(ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)
        return self.them_sach(sach_moi)

    def xoa_sach(self, phuong_thuc):
        if not self.head:
            print("Danh sách sách trống. Không có sách để xóa.")
            return
        if phuong_thuc == "dau":
            self.head = self.head.next
            print("Đã xóa sách ở đầu danh sách.")
            return
        current = self.head
        prev = None
        while current:
            if current.data.ten_sach == phuong_thuc:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                print(f"Đã xóa sách có tên {phuong_thuc} khỏi danh sách.")
                return
            prev = current
            current = current.next
        print("Không tìm thấy sách cần xóa.")

    def chay_thu_vien(self):
        while True:
            print("\n1. Thêm sách mới vào danh sách")
            print("2. Thêm sách mới vào đầu danh sách")
            print("3. Xuất danh sách sách")
            print("4. Đếm số lượng sách của một tác giả")
            print("5. Tìm sách theo nhà xuất bản và năm")
            print("6. Tìm và thêm sách mới")
            print("7. Xóa sách")
            print("8. Thoát")
            lua_chon = input("Nhập lựa chọn của bạn: ")

            if lua_chon == '1':
                self.them_sach_moi()
            elif lua_chon == '2':
                self.them_sach_dau_danh_sach()
            elif lua_chon == '3':
                self.xuat_danh_sach_sach()
            elif lua_chon == '4':
                tac_gia_can_dem = input("Nhập tên tác giả cần đếm: ")
                print(f"Số lượng sách của tác giả {tac_gia_can_dem}: {self.dem_so_luong_sach_theo_tac_gia(tac_gia_can_dem)}")
            elif lua_chon == '5':
                nxb = input("Nhập tên nhà xuất bản: ")
                nam_xuat_ban = int(input("Nhập năm xuất bản: "))
                sach_tim_thay = self.tim_sach_theo_nxb_va_nam(nxb, nam_xuat_ban)
                for sach in sach_tim_thay:
                    print(f"Tìm thấy sách: Tên sách: {sach.ten_sach}, Tác giả: {', '.join(sach.tac_gia)}, Nhà xuất bản: {sach.nha_xuat_ban}, Năm xuất bản: {sach.nam_xuat_ban}, Giá: {sach.gia}")
            elif lua_chon == '6':
                ten_sach_can_tim = input("Nhập tên sách cần tìm và thêm: ")
                self.tim_va_them_sach_moi(ten_sach_can_tim)
            elif lua_chon == '7':
                phuong_thuc_xoa = input("Nhập phương thức xóa (dau, ten): ")
                self.xoa_sach(phuong_thuc_xoa)
            elif lua_chon == '8':
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    thu_vien = ThuVien()
    thu_vien.chay_thu_vien()
