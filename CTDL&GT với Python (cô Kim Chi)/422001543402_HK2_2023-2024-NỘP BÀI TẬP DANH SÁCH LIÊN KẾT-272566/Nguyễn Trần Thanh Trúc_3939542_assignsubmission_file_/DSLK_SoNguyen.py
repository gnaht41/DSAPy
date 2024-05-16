'''
1) Viết chương trình nhập từ bàn phím các số nguyên cho đến khi nhập vào chuỗi rỗng. 
Các số nguyên này được đưa vào 1 danh sách. Xuất ra: 
1. Số lượng các phần tử trong danh sách 
2. Tổng giá trị của các số trong danh sách 
3. Giá trị lớn nhất trong danh sách 
4. Giá trị nhỏ nhất trong danh sách 
5. Sắp xếp Danh sách theo thứ tự tăng dần
6. Sắp xếp Danh sách theo thứ tự giảm dần 
7. Danh sách các phần tử có giá trị là chẵn 
8. Tìm 1 phần tử có giá trị X trong danh sách 
Yêu cầu: Viết bằng danh sách liên kết 
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def count_elements(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def sum_elements(self):
        total = 0
        current = self.head
        while current:
            total += current.data
            current = current.next
        return total

    def max_element(self):
        if not self.head:
            return None
        max_val = self.head.data
        current = self.head.next
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val

    def min_element(self):
        if not self.head:
            return None
        min_val = self.head.data
        current = self.head.next
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val

    def sort_ascending(self):
        sorted_list = []
        current = self.head
        while current:
            sorted_list.append(current.data)
            current = current.next
        sorted_list.sort()
        return sorted_list

    def sort_descending(self):
        sorted_list = self.sort_ascending()
        return sorted_list[::-1]

    def even_elements(self):
        even_list = []
        current = self.head
        while current:
            if current.data % 2 == 0:
                even_list.append(current.data)
            current = current.next
        return even_list

    def find_element(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def input_list(self):
        while True:
            try:
                user_input = input("Nhập số nguyên (nhập chuỗi rỗng để kết thúc): ")
                if user_input == "":
                    break
                self.insert(int(user_input))
            except ValueError:
                print("Vui lòng nhập số nguyên hoặc chuỗi rỗng!")

def main():
    linked_list = LinkedList()
    linked_list.input_list()

    print("\nDanh sách các phần tử:")
    linked_list.display()

    print("\n1. Số lượng các phần tử trong danh sách:", linked_list.count_elements())
    print("2. Tổng giá trị của các số trong danh sách:", linked_list.sum_elements())
    print("3. Giá trị lớn nhất trong danh sách:", linked_list.max_element())
    print("4. Giá trị nhỏ nhất trong danh sách:", linked_list.min_element())
    print("5. Danh sách sắp xếp theo thứ tự tăng dần:", linked_list.sort_ascending())
    print("6. Danh sách sắp xếp theo thứ tự giảm dần:", linked_list.sort_descending())
    print("7. Danh sách các phần tử có giá trị là chẵn:", linked_list.even_elements())

    try:
        target_value = int(input("\nNhập giá trị X để tìm trong danh sách: "))
        if linked_list.find_element(target_value):
            print(f"Giá trị {target_value} có trong danh sách.")
        else:
            print(f"Giá trị {target_value} không có trong danh sách.")
    except ValueError:
        print("Vui lòng nhập số nguyên!")

if __name__ == "__main__":
    main()
