from BT4DSLK_Sach import *
def main():
    thu_vien = ThuVien()

    while True:
        print("\n----- MENU -----")
        print("1. Thêm sách mới vào đầu danh sách")
        print("2. Thêm sách mới vào cuối danh sách")
        print("3. Xuất danh sách sách")
        print("4. Số lượng sách của một tác giả")
        print("5. Các sách được phát hành trong một năm của một nhà xuất bản")
        print("6. Tìm kiếm và thêm sách mới (nếu chưa tồn tại)")
        print("7. Xóa sách khỏi danh sách")
        print("0. Thoát chương trình")
        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            ten_sach = input("Nhập tên sách: ")
            tac_gia = input("Nhập tác giả (các tác giả cách nhau bằng dấu phẩy): ")
            nha_xuat_ban = input("Nhập nhà xuất bản: ")
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            gia = int(input("Nhập giá: "))
            thu_vien.them_sach_dau(ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)
        elif lua_chon == '2':
            ten_sach = input("Nhập tên sách: ")
            tac_gia = input("Nhập tác giả (các tác giả cách nhau bằng dấu phẩy): ")
            nha_xuat_ban = input("Nhập nhà xuất bản: ")
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            gia = int(input("Nhập giá: "))
            thu_vien.them_sach_cuoi(ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)
        elif lua_chon == '3':
            thu_vien.xuat_danh_sach_sach()
        elif lua_chon == '4':
            ten_tac_gia = input("Nhập tên tác giả: ")
            print("Số lượng sách của tác giả", ten_tac_gia, "là:", thu_vien.so_luong_sach_tac_gia(ten_tac_gia))
        elif lua_chon == '5':
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            nha_xuat_ban = input("Nhập nhà xuất bản: ")
            print("Các sách được phát hành trong năm", nam_xuat_ban, "của nhà xuất bản", nha_xuat_ban, "là:")
            sach_phathanh = thu_vien.sach_theo_nam_nxb(nam_xuat_ban, nha_xuat_ban)
            for sach in sach_phathanh:
                print(sach)
        elif lua_chon == '6':
            ten_sach_can_tim = input("Nhập tên sách cần tìm: ")
            ten_sach_moi = input("Nhập tên sách mới: ")
            tac_gia = input("Nhập tác giả (các tác giả cách nhau bằng dấu phẩy): ")
            nha_xuat_ban = input("Nhập nhà xuất bản: ")
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            gia = int(input("Nhập giá: "))
            thu_vien.tim_sach_va_them_moi(ten_sach_can_tim, ten_sach_moi, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)
        elif lua_chon == '7':
            print("\n----- Xóa sách -----")
            print("1. Xóa sách đầu danh sách")
            print("2. Xóa sách cuối danh sách")
            print("3. Xóa sách theo tên")
            xoa_lua_chon = input("Nhập lựa chọn của bạn: ")
            if xoa_lua_chon == '1':
                thu_vien.xoa_sach_dau()
            elif xoa_lua_chon == '2':
                thu_vien.xoa_sach_cuoi()
            elif xoa_lua_chon == '3':
                ten_sach_can_xoa = input("Nhập tên sách cần xóa: ")
                thu_vien.xoa_sach_theo_ten(ten_sach_can_xoa)
            else:
                print("Lựa chọn không hợp lệ.")
        elif lua_chon == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
