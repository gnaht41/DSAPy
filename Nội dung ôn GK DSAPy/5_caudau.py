#1. Viết một hàm để đảo ngược một mảng trong Python
def daoNguoc1(a):
    # Đảo ngược mảng không có giá trị trả về
    a.reverse()
mang1 = [1,2,3,4,5]
daoNguoc1(mang1)
print(f'Mang dao nguoc 1: {mang1}')

def daoNguoc2(a):
    # Đảo ngược mảng có giá trị trả về
    mangDaoNguoc = []
    for i in reversed(a):
        mangDaoNguoc.append(i)
    return mangDaoNguoc
mang2 = [1,2,3,4,5]
print(f'Mang dao nguoc 2: {daoNguoc2(mang2)}')

#2. Cho một mảng yêu cầu sắp xếp số chẵn trước và số lẻ sau, thứ tự số chẵn và lẻ phải được sắp xếp lại
def sapXepChanLe(a):
    chan = []
    le = []
    for i in a:
        if i % 2 == 0:
            chan.append(i)
    for i in a:
        if i % 2 != 0:
            le.append(i)
    return sorted(chan) + sorted(le)
mang3 = [3,8,1,6,7,4,2,5]
print(f'Mang sau khi sap xep chan le {sapXepChanLe(mang3)}')

#3. Đếm số lượng phần tử lớn nhất trong mảng
def demSoPhanTuLonNhat(a):
    dem = 0
    for i in a:
        if i == max(a):
            dem += 1
    return f'So lon nhat: {max(a)}, so luong: {dem}'    
mang4 = [2,4,6,8,5,8,1,8]
print(demSoPhanTuLonNhat(mang4))

#4. Viết một hàm xóa một phần tử cụ thể ra khỏi mảng
def xoaPhanTu(a, x):
    dem = 0
    for i in a[:]:
        if i == x:
            a.remove(i)
            dem += 1
    if dem != 0:
        return f'Xoa phan tu {x} thanh cong'
    else:
        return f'Khong co phan tu {x} can xoa'
mang5 = [2,4,6,8,5,8,1,8]
print(xoaPhanTu(mang5,2))

#5. Thêm phần tử vào mảng theo thứ tự
def themTheoThuTu(a, x):
    a.append(x)
    return sorted(a)
mang6 = [1,3,4,6,7]
x = 2
print(themTheoThuTu(mang6,x))