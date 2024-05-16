from SinhVien import DanhSachSinhVien
if __name__ == "__main__":
     ds_sv = DanhSachSinhVien()
    sv1 = SinhVien("SV001", "Nguyen Van A", "Toan", 8.5)
    sv2 = SinhVien("SV002", "Tran Thi B", "Van", 7.2)
    sv3 = SinhVien("SV003", "Le Van C", "Anh", 6.8)
    ds_sv.chen_hoc_sinh_moi_cuoi_cung(sv1)
    ds_sv.chen_hoc_sinh_moi_cuoi_cung(sv2)
    ds_sv.chen_hoc_sinh_moi_cuoi_cung(sv3)

    # Sắp xếp danh sách theo điểm
    ds_sv.sap_xep_theo_diem()

    # Chèn một sinh viên mới sau khi đã sắp xếp
    sv4 = SinhVien("SV004", "Pham Thi D", "Ly", 9.0)
    ds_sv.chen_hoc_sinh_moi_sau_sap_xep(sv4)

    # Lấy danh sách sinh viên có điểm lớn hơn x
    danh_sach_lon_hon_7 = ds_sv.lay_sinh_vien_diem_lon_hon_x(7.0)
    print("Danh sách sinh viên có điểm lớn hơn 7.0:")
    for sv in danh_sach_lon_hon_7:
        print(sv)

    # Tìm k sinh viên có điểm cao nhất
    k_sinh_vien_cao_nhat = ds_sv.tim_k_sinh_vien_coi_diem_cao_nhat(2)
    print("2 sinh viên có điểm cao nhất:")
    for sv in k_sinh_vien_cao_nhat:
        print(sv)

    # Loại bỏ sinh viên có điểm nhỏ hơn 7.0
    ds_sv.loai_bo_sinh_vien_diem_nho_hon_x(7.0)

    # In ra danh sách sinh viên sau khi loại bỏ
    print("Danh sách sinh viên sau khi loại bỏ sinh viên có điểm nhỏ hơn 7.0:")
    ds_sv.in_danh_sach_sinh_vien()

    # Tạo danh sách mới để hợp nhất
    ds_sv_moi = DanhSachSinhVien()
    sv5 = SinhVien("SV005", "Hoang Thi E", "Sinh", 8.3)
    sv6 = SinhVien("SV006", "Ngo Van F", "Hoa", 7.5)
    ds_sv_moi.chen_hoc_sinh_moi_cuoi_cung(sv5)
    ds_sv_moi.chen_hoc_sinh_moi_cuoi_cung(sv6)

    # Hợp nhất danh sách mới vào danh sách cũ
    ds_sv.hop_nhat_danh_sach(ds_sv_moi.danh_sach)

    # In ra danh sách sinh viên sau khi hợp nhất
    print("Danh sách sinh viên sau khi hợp nhất:")
    ds_sv.in_danh_sach_sinh_vien()

    # Ghi danh sách sinh viên ra file txt
    ds_sv.ghi_danh_sach_ra_file_txt("danh_sach_sinh_vien.txt")