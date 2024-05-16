class SinhVien:
    def __init__(self, masv, ten_sv, mon_hoc, diem):
        self.masv = masv
        self.ten_sv = ten_sv
        self.mon_hoc = mon_hoc
        self.diem = diem

    def __str__(self):
        return f"MASV: {self.masv}, Tên SV: {self.ten_sv}, Môn Học: {self.mon_hoc}, Điểm: {self.diem}"

def chen_hoc_sinh_cuoi_cung(danh_sach, masv, ten_sv, mon_hoc, diem):
    danh_sach.append(SinhVien(masv, ten_sv, mon_hoc, diem))

def sap_xep_theo_diem(danh_sach):
    danh_sach.sort(key=lambda x: x.diem)

def chen_hoc_sinh_sap_xep(danh_sach, masv, ten_sv, mon_hoc, diem):
    danh_sach.append(SinhVien(masv, ten_sv, mon_hoc, diem))
    sap_xep_theo_diem(danh_sach)

def lay_sv_diem_lon_hon_x(danh_sach, x):
    return [sv for sv in danh_sach if sv.diem > x]

def tim_k_sv_cao_nhat(danh_sach, k):
    danh_sach.sort(key=lambda x: x.diem, reverse=True)
    return danh_sach[:k]

def loai_bo_sv_diem_nho_hon_x(danh_sach, x):
    danh_sach[:] = [sv for sv in danh_sach if sv.diem >= x]

def hop_nhat_danh_sach(danh_sach1, danh_sach2):
    return danh_sach1 + danh_sach2

def in_danh_sach(danh_sach):
    for sv in danh_sach:
        print(sv)

def ghi_ra_file(danh_sach, ten_file):
    with open(ten_file, 'w', encoding='utf-8') as file:
        for sv in danh_sach:
            file.write(f"{sv.code}-{sv.name}-{sv.age}-{sv.salary}\n")
