from BT3DSLK_SinhVien import *
def main():
    danh_sach_sinh_vien = []

    # Thêm một số sinh viên vào danh sách
    chen_hoc_sinh_cuoi_cung(danh_sach_sinh_vien, "SV001", "Nguyen Van A", "Toan", 8.5)
    chen_hoc_sinh_cuoi_cung(danh_sach_sinh_vien, "SV002", "Tran Thi B", "Van", 7.0)
    chen_hoc_sinh_cuoi_cung(danh_sach_sinh_vien, "SV003", "Le Van C", "Anh", 9.0)

    print("Danh sách sinh viên ban đầu:")
    in_danh_sach(danh_sach_sinh_vien)

    print("\nThêm một học sinh mới vào danh sách cuối cùng:")
    chen_hoc_sinh_cuoi_cung(danh_sach_sinh_vien, "SV004", "Pham Thi D", "Ly", 6.5)
    in_danh_sach(danh_sach_sinh_vien)

    print("\nSắp xếp danh sách theo thứ tự tăng dần của Điểm:")
    sap_xep_theo_diem(danh_sach_sinh_vien)
    in_danh_sach(danh_sach_sinh_vien)

    print("\nThêm một học sinh mới vào danh sách đã sắp xếp để có danh sách cũng đã sắp xếp:")
    chen_hoc_sinh_sap_xep(danh_sach_sinh_vien, "SV005", "Hoang Van E", "Hoa", 8.0)
    in_danh_sach(danh_sach_sinh_vien)

    print("\nLấy danh sách sinh viên có Điểm lớn hơn 7.0:")
    sv_diem_lon_hon_7 = lay_sv_diem_lon_hon_x(danh_sach_sinh_vien, 7.0)
    in_danh_sach(sv_diem_lon_hon_7)

    print("\nTìm kiếm 2 sinh viên có Điểm cao nhất:")
    k_sv_cao_nhat = tim_k_sv_cao_nhat(danh_sach_sinh_vien, 2)
    in_danh_sach(k_sv_cao_nhat)

    print("\nLoại bỏ tất cả sinh viên có Điểm nhỏ hơn 7.0:")
    loai_bo_sv_diem_nho_hon_x(danh_sach_sinh_vien, 7.0)
    in_danh_sach(danh_sach_sinh_vien)

    print("\nHợp nhất vào danh sách sinh viên:")
    danh_sach_ket_hop = hop_nhat_danh_sach(danh_sach_sinh_vien, sv_diem_lon_hon_7)
    in_danh_sach(danh_sach_ket_hop)

    print("\nGhi danh sách sinh viên ra file txt:")
    ghi_ra_file(danh_sach_sinh_vien, "danh_sach_sinh_vien.txt")
    print("Đã ghi danh sách sinh viên vào file danh_sach_sinh_vien.txt")

if __name__ == "__main__":
    main()