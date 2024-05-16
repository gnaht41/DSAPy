import random


def sapXepChanLe(a):
    soChan = []
    soLe = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            soChan.append(a[i])
            soChan.sort()
        if a[i] % 2 != 0:
            soLe.append(a[i])
            soLe.sort()
    a = soChan + soLe
    return a


def demSoLonNhat(a):
    max = a[0]
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max


def main():

    a = [2, 4, 6, 8]
    a.reverse()
    print(f"Mảng sau khi đảo ngược là {a}")
    a = [3, 8, 1, 6, 7, 4, 2, 5]
    print(f"Mảng sau khi sắp xếp chẵn lẻ là {sapXepChanLe(a)}")
    a = [2, 4, 6, 8, 5, 8, 1, 8]
    print(f"Số lần lặp lại số lớn nhất là {a.count(demSoLonNhat(a))}")
    a.remove(2)
    print(f"Mảng sau khi xóa số 2 là {a}")
    a = [1, 3, 4, 6, 7]
    a.insert(1, 2)
    print(f"Mảng sau khi thêm số vào là {a}")


if __name__ == "__main__":
    main()
