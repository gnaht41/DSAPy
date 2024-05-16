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

    def them_sach(self, sach):
        if self.head is None:
            self.head = sach
        else:
            current = self.head
            while current.next:
                if current.ten_sach == sach.ten_sach:
                    print("Tên sách đã tồn tại trong thư viện.")
                    return
                current = current.next
            current.next = sach

    def them_sach_dau(self, sach):
        if self.head is None:
            self.head = sach
        else:
            sach.next = self.head
            self.head = sach

    def xuat_danh_sach_sach(self):
        current = self.head
        if current is None:
            print("Thư viện trống.")
            return
        while current:
            print("Tên sách:", current.ten_sach)
            print("Tác giả:", current.tac_gia)
            print("Nhà xuất bản:", current.nha_xuat_ban)
            print("Năm xuất bản:", current.nam_xuat_ban)
            print("Giá:", current.gia)
            print("-----------------------")
            current = current.next

    def dem_so_sach_cua_tac_gia(self, tac_gia):
        count = 0
        current = self.head
        while current:
            if tac_gia in current.tac_gia:
                count += 1
            current = current.next
        return count

    def sach_phat_hanh_trong_nam_cua_nha_xuat_ban(self, nam, nha_xuat_ban):
        sach_phat_hanh = []
        current = self.head
        while current:
            if current.nam_xuat_ban == nam and current.nha_xuat_ban == nha_xuat_ban:
                sach_phat_hanh.append(current.ten_sach)
            current = current.next
        return sach_phat_hanh

    def tim_sach_theo_ten(self, ten_sach):
        current = self.head
        while current:
            if current.ten_sach == ten_sach:
                return current
            current = current.next
        return None

    def them_sach_sau_khi_tim(self, ten_sach, sach_moi):
        sach = self.tim_sach_theo_ten(ten_sach)
        if sach:
            if self.tim_sach_theo_ten(sach_moi.ten_sach):
                print("Tên sách đã tồn tại trong thư viện.")
                return
            sach_moi.next = sach.next
            sach.next = sach_moi
        else:
            print("Không tìm thấy sách.")

    def xoa_sach(self, ten_sach):
        if self.head is None:
            print("Thư viện trống.")
            return

        current = self.head
        if current.ten_sach == ten_sach:
            self.head = current.next
            return

        prev = None
        while current and current.ten_sach != ten_sach:
            prev = current
            current = current.next

        if current is None:
            print("Không tìm thấy sách.")
            return

        prev.next = current.next


def main():
    thu_vien = ThuVien()

    while True:
        print("\nChọn chức năng:")
        print("1. Thêm sách mới vào danh sách.")
        print("2. Thêm sách vào đầu danh sách.")
        print("3. Xuất danh sách các cuốn sách.")
        print("4. Số lượng sách của một tác giả.")
        print("5. Danh sách các sách phát hành trong một năm của một nhà xuất bản.")
        print("6. Tìm và thêm sách mới.")
        print("7. Xóa sách.")
        print("0. Thoát.")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == "1":
            ten_sach = input("Nhập tên sách: ")
            tac_gia = input("Nhập tác giả (cách nhau bởi dấu phẩy): ").split(", ")
            nha_xuat_ban = input("Nhập nhà xuất bản: ")
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            gia = int(input("Nhập giá sách: "))
            sach_moi = Sach(ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)
            thu_vien.them_sach(sach_moi)

        elif lua_chon == "2":
            ten_sach = input("Nhập tên sách: ")
            tac_gia = input("Nhập tác giả (cách nhau bởi dấu phẩy): ").split(", ")
            nha_xuat_ban = input("Nhập nhà xuất bản: ")
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            gia = int(input("Nhập giá sách: "))
            sach_moi = Sach(ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)
            thu_vien.them_sach_dau(sach_moi)

        elif lua_chon == "3":
            thu_vien.xuat_danh_sach_sach()

        elif lua_chon == "4":
            tac_gia = input("Nhập tên tác giả: ")
            print("Số lượng sách của tác giả", tac_gia, "là:", thu_vien.dem_so_sach_cua_tac_gia(tac_gia))

        elif lua_chon == "5":
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            nha_xuat_ban = input("Nhập tên nhà xuất bản: ")
            sach_phat_hanh = thu_vien.sach_phat_hanh_trong_nam_cua_nha_xuat_ban(nam_xuat_ban, nha_xuat_ban)
            if sach_phat_hanh:
                print(f"Các sách được phát hành trong năm {nam_xuat_ban} của nhà xuất bản {nha_xuat_ban}:")
                for sach in sach_phat_hanh:
                    print(sach)
            else:
                print("Không có sách nào được phát hành trong năm và nhà xuất bản này.")

        elif lua_chon == "6":
            ten_sach = input("Nhập tên sách cần tìm: ")
            sach_tim_duoc = thu_vien.tim_sach_theo_ten(ten_sach)
            if sach_tim_duoc:
                print("Tìm thấy sách:")
                print("Tên sách:", sach_tim_duoc.ten_sach)
                print("Tác giả:", sach_tim_duoc.tac_gia)
                print("Nhà xuất bản:", sach_tim_duoc.nha_xuat_ban)
                print("Năm xuất bản:", sach_tim_duoc.nam_xuat_ban)
                print("Giá:", sach_tim_duoc.gia)
                lua_chon_them = input("Bạn có muốn thêm sách mới vào sau sách này không? (C/K): ")
                if lua_chon_them.upper() == 'C':
                    ten_sach_moi = input("Nhập tên sách mới: ")
                    tac_gia_moi = input("Nhập tác giả mới (cách nhau bởi dấu phẩy): ").split(", ")
                    nha_xuat_ban_moi = input("Nhập nhà xuất bản mới: ")
                    nam_xuat_ban_moi = int(input("Nhập năm xuất bản mới: "))
                    gia_moi = int(input("Nhập giá sách mới: "))
                    sach_moi = Sach(ten_sach_moi, tac_gia_moi, nha_xuat_ban_moi, nam_xuat_ban_moi, gia_moi)
                    thu_vien.them_sach_sau_khi_tim(ten_sach, sach_moi)
            else:
                print("Không tìm thấy sách.")

        elif lua_chon == "7":
            ten_sach = input("Nhập tên sách cần xóa: ")
            thu_vien.xoa_sach(ten_sach)

        elif lua_chon == "0":
            print("Kết thúc chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()

