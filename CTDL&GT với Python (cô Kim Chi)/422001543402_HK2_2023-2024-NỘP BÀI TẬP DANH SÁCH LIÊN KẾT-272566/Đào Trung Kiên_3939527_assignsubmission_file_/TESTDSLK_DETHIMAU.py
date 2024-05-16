from DSLK_DETHIMAU import *
def print_menu():
    print("Menu:")
    print("1. Kiểm tra xem danh sách có trống không")
    print("2. Kiểm tra xem ID có bị trùng lặp trong danh sách không")
    print("3. Thêm một mục mới vào cuối danh sách")
    print("4. Exit")

sll = IdValueSLL()

while True:
    print_menu()
    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        if sll.isEmpty():
            print("Danh sách trống.")
        else:
            print("Danh sách không trống.")
    elif choice == "2":
        id_to_check = input("Nhập ID để kiểm tra trùng lặp: ")
        if sll.isDuplicated(id_to_check):
            print(f"ID '{id_to_check}' bị trùng lặp trong danh sách.")
        else:
            print(f"ID '{id_to_check}' không trùng lặp trong danh sách.")
    elif choice == "3":
        id_value = IdValue(input("Nhập ID: "), int(input("Nhập giá trị: ")))
        sll.addTail(id_value)
        print("Mục được thêm vào cuối danh sách.")
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập một tùy chọn hợp lệ.")
