import random
import math


def trungNhau(a, k):
    n = len(a)
    count = 0
    for i in range(n):
        if a[i] == k:
            count += 1
    return count


def soChinhPhuong(n):
    square_root = int(math.sqrt(n))
    return square_root**2 == n


def main():
    a = [2, 4, 2, 8, 6, 8]
    print(f"Các số chỉ xuất hiện 1 lần là : ")
    for i in range(len(a)):
        if trungNhau(a, a[i]) == 1:
            print(f"{a[i]}")

    a = [15, 4, 9, 16, 3, 6]
    dsCP = []
    for i in range(len(a)):
        if soChinhPhuong(a[i]) == True:
            dsCP.append(a[i])
    print(f"Các số chính phương là : {dsCP}")

    a = [2, 4, 6, 8, 5, 1]
    for i in range(len(a)):
        if trungNhau(a, a[i]) > 1:
            a.remove(a[i])
    print(f"\nMảng sau khi xóa trùng lắp : {a}")

    a = [1, 3, 4, 6, 7]
    viTri = int(input("Nhập vị trí muốn thêm : "))
    num = int(input("Nhập số muốn thêm : "))
    a.insert((viTri + 1), num)
    print(a)


if __name__ == "__main__":
    main()
