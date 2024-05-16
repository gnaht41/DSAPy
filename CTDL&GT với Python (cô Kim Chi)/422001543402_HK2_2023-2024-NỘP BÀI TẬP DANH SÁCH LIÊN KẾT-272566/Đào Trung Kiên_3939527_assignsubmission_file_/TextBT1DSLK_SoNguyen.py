from BT1DSLK_SoNguyen import *
def main():
    danh_sach = DSLienket()
    while True:
        gia_tri = input("Nhập một số nguyên (END để kết thúc): ")
        if gia_tri == 'END':
            break
        danh_sach.them(int(gia_tri))

    print("Số lượng các phần tử trong danh sách:", danh_sach.so_luong_phan_tu())
    print("Tổng giá trị của các số trong danh sách:", danh_sach.tong_gia_tri())
    max_value, min_value = danh_sach.max_min()
    print("Giá trị lớn nhất trong danh sách:", max_value)
    print("Giá trị nhỏ nhất trong danh sách:", min_value)
    print("Danh sách sắp xếp theo thứ tự tăng dần:", danh_sach.sap_xep_tang())
    print("Danh sách sắp xếp theo thứ tự giảm dần:", danh_sach.sap_xep_giam())
    print("Danh sách các phần tử có giá trị là chẵn:", danh_sach.so_chan())
    gia_tri_tim = int(input("Nhập giá trị bạn muốn tìm trong danh sách: "))
    if danh_sach.tim_gia_tri(gia_tri_tim):
        print(f"Giá trị {gia_tri_tim} có trong danh sách.")
    else:
        print(f"Giá trị {gia_tri_tim} không có trong danh sách.")

if __name__ == "__main__":
    main()
