from BT2DSLK import *
def main():
    danh_sach = DSLienket()
    while True:
        print("\n----- MENU -----")
        print("1. Thêm một số vào cuối danh sách")
        print("2. Thêm một số vào trước một số khác")
        print("3. In danh sách")
        print("4. In danh sách theo thứ tự ngược")
        print("5. Tìm giá trị lớn nhất và nhỏ nhất trong danh sách")
        print("6. Tính tổng số âm và dương trong danh sách")
        print("7. Tính tích các số trong danh sách")
        print("8. Tính tổng bình phương của các số trong danh sách")
        print("9. Nhập x, xuất các số là số nguyên tố của x")
        print("10. Nhập x, xuất các số là ước số của x")
        print("11. Nhập x, tìm giá trị đầu tiên trong danh sách mà > x")
        print("12. Xuất số nguyên tố cuối cùng trong danh sách")
        print("13. Đếm số lượng số nguyên tố trong danh sách")
        print("14. Kiểm tra xem danh sách có được sắp xếp tăng không")
        print("15. Kiểm tra xem danh sách có các phần tử đối xứng không")
        print("16. Xóa phần tử cuối cùng trong danh sách")
        print("17. Xóa phần tử đầu tiên trong danh sách")
        print("18. Hủy toàn bộ danh sách")
        print("0. Thoát chương trình")
        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            gia_tri = int(input("Nhập giá trị muốn thêm vào cuối danh sách: "))
            danh_sach.them_cuoi(gia_tri)
        elif lua_chon == '2':
            gia_tri = int(input("Nhập giá trị muốn thêm: "))
            gia_tri_truoc = int(input("Nhập giá trị muốn thêm trước: "))
            danh_sach.them_truoc(gia_tri, gia_tri_truoc)
        elif lua_chon == '3':
            print("Danh sách:", end=" ")
            danh_sach.in_ds()
        elif lua_chon == '4':
            print("Danh sách theo thứ tự ngược:", end=" ")
            danh_sach.in_ds_nguoc()
        elif lua_chon == '5':
            max_value, min_value = danh_sach.tim_max_min()
            print("Giá trị lớn nhất trong danh sách:", max_value)
            print("Giá trị nhỏ nhất trong danh sách:", min_value)
        elif lua_chon == '6':
            tong_am, tong_duong = danh_sach.tong_so_am_duong()
            print("Tổng số âm trong danh sách:", tong_am)
            print("Tổng số dương trong danh sách:", tong_duong)
        elif lua_chon == '7':
            print("Tích của các số trong danh sách:", danh_sach.tich_so())
        elif lua_chon == '8':
            print("Tổng bình phương của các số trong danh sách:", danh_sach.tong_binh_phuong())
        elif lua_chon == '9':
            x = int(input("Nhập giá trị x: "))
            danh_sach.so_nguyen_to_cua_x(x)
        elif lua_chon == '10':
            x = int(input("Nhập giá trị x: "))
            danh_sach.uoc_so_cua_x(x)
        elif lua_chon == '11':
            x = int(input("Nhập giá trị x: "))
            gia_tri = danh_sach.gia_tri_dau_tien_lon_hon_x(x)
            if gia_tri is not None:
                print("Giá trị đầu tiên trong danh sách lớn hơn", x, "là:", gia_tri)
        elif lua_chon == '12':
            danh_sach.so_nguyen_to_cuoi_cung()
        elif lua_chon == '13':
            danh_sach.dem_so_nguyen_to()
        elif lua_chon == '14':
            if danh_sach.kiem_tra_sap_tang():
                print("Danh sách đã được sắp xếp tăng.")
            else:
                print("Danh sách chưa được sắp xếp tăng.")
        elif lua_chon == '15':
            if danh_sach.kiem_tra_doi_xung():
                print("Danh sách có các phần tử đối xứng.")
            else:
                print("Danh sách không có các phần tử đối xứng.")
        elif lua_chon == '16':
            danh_sach.xoa_cuoi()
            print("Đã xóa phần tử cuối cùng trong danh sách.")
        elif lua_chon == '17':
            danh_sach.xoa_dau()
            print("Đã xóa phần tử đầu tiên trong danh sách.")
        elif lua_chon == '18':
            danh_sach.huy_toan_bo()
            print("Đã hủy toàn bộ danh sách.")
        elif lua_chon == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
