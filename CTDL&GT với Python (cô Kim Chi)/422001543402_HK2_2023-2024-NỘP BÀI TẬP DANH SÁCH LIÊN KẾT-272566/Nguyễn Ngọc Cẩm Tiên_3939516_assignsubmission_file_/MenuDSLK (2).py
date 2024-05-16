from DSLienKet import DSLienKet
if __name__ == "__main__":
    danh_sach = DSLienKet()
    while True:
        print("\nMenu:")
        print("1. Thêm một số pt vào cuối ds")
        print("2. Thêm 1 pt vào trước pt nào đó")
        print("3. In ds")
        print("4. In ds theo thứ tự ngược")
        print("5. Tìm GTNN, GTLN trong ds")
        print("6. Tính tổng số âm, tổng số dương trong ds")
        print("7. Tính tích các số trong ds")
        print("8. Tính tổng bình phương của các số trong ds")
        print("9. Nhập x, xuất các số là số nguyên tố của x")
        print("10. Nhập x, xuất các số là ước số của x")
        print("11. Nhập x, tìm giá trị đầu tiên trong ds mà >x.")
        print("12. Xuất số nguyên tố cuối cùng trong ds")
        print("13. Đếm các số nguyên tố")
        print("14. Kiểm tra xem ds có phải đã được sắp tăng không")
        print("15. Kiểm tra xem ds có các pt đối xứng nhau hay không")
        print("16. Xóa pt cuối")
        print("17. Xóa pt đầu")
        print("18. Hủy toàn bộ ds")
        print("0. Thoát chương trình")
        
        choice = int(input("Chọn chức năng: "))

        if choice == 1:
            gia_tri = int(input("Nhập số cần thêm vào cuối danh sách: "))
            danh_sach.them(gia_tri)
        elif choice == 2:
            gia_tri = int(input("Nhập số cần thêm: "))
            chi_muc = int(input("Nhập vị trí cần chèn: "))
            danh_sach.chen(chi_muc, gia_tri)
        elif choice == 3:
            danh_sach.in_ds()
        elif choice == 4:
            danh_sach.in_ds_nguoc()
        elif choice == 5:
            min_val, max_val = danh_sach.tim_min_max()
            print("Giá trị nhỏ nhất trong danh sách:", min_val)
            print("Giá trị lớn nhất trong danh sách:", max_val)
        elif choice == 6:
            so_duong, so_am = danh_sach.dem_sAm_sDuong()
            print("Tổng số âm trong danh sách là:", so_am)
            print("Tổng số dương trong danh sách là:", so_am)
        elif choice == 7:
            print("Tích của các số trong danh sách:")
            danh_sach.tich_so()
        elif choice == 8:
            print("Tổng bình phương của các số trong danh sách:", danh_sach.tong_binh_phuong())
        elif choice == 9:
            x = int(input("Nhập x: "))
            print("Các số nguyên tố là ước số của", x, "là:")
            danh_sach.tim_so_ngto(x)
        elif choice == 10:
            x = int(input("Nhập x: "))
            divisors = danh_sach.tim_uoc_so(x)
            print("Các ước số của", x, "là:", divisors)
        elif choice == 11:
            x = int(input("Nhập x: "))
            result = danh_sach.tim_gia_tri_dau(x)
            if result:
                print("Giá trị đầu tiên trong danh sách lớn hơn", x, "là:", result)
            else:
                print("Không tìm thấy giá trị nào lớn hơn", x, "trong danh sách.")
        elif choice == 12:
            pass
        elif choice == 13:
            count = danh_sach.dem_so_ngto()
            print("Số lượng số nguyên tố trong danh sách là:", count)
        elif choice == 14:
            pass
        elif choice == 15:
           pass
        elif choice == 16:
            pass
        elif choice == 17:
           pass
        elif choice == 18:
            danh_sach.xoa_het()
            print("Đã hủy toàn bộ danh sách.")
        elif choice == 0:
            print("Thoát chương trình.")
            break
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn lại.")