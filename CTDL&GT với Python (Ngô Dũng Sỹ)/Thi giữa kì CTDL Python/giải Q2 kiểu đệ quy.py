import math


def tinhTong(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n/math.sqrt(n)+tinhTong(n-1)


def main():
    n = int(input('Nhập số n : '))
    while True:
        if n > 0:
            print(f'Tổng từ 1 đến n/căn n là : {round(tinhTong(n),2)}')
            break
        else:
            print('Giá trị n ko hợp lệ')
            break


if __name__ == '__main__':
    main()
