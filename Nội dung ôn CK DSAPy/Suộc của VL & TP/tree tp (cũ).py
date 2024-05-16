class Student:
    def __init__(self, masv, hoten, malop, diem_tb):
        self.masv = masv
        self.hoten = hoten
        self.malop = malop
        self.diem_tb = diem_tb
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert_recursive(self, node, masv, hoten, malop, diem_tb):
        if masv < node.masv:
            if node.left is None:
                node.left = Student(masv, hoten, malop, diem_tb)
            else:
                self.insert_recursive(node.left, masv, hoten, malop, diem_tb)
        else:
            if node.right is None:
                node.right = Student(masv, hoten, malop, diem_tb)
            else:
                self.insert_recursive(node.right, masv, hoten, malop, diem_tb)

    def insert(self, masv, hoten, malop, diem_tb):
        if self.root is None:
            self.root = Student(masv, hoten, malop, diem_tb)
        else:
            self.insert_recursive(self.root, masv, hoten, malop, diem_tb)

    def add_student(self):
        masv = input("Nhập mã sinh viên: ")
        hoten = input("Nhập họ tên: ")
        malop = input("Nhập mã lớp: ")
        diem_tb = float(input("Nhập điểm trung bình: "))
        self.insert(masv, hoten, malop, diem_tb)

    # duyệt và xuất dữ liệu cây theo thứ tự LNR ra màn hình theo mã số sinh viên
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print("MASV:", node.masv, "- Họ tên:", node.hoten,
                  "- Mã lớp:", node.malop, "- Điểm TB:", node.diem_tb)
            self.inorder_traversal(node.right)

    def in_order_print(self):
        self._inorder_traversal(self.root)

    # đếm số nút lá
    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def count_nodes(self):
        return self._count_nodes(self.root)

    # tính chiều cao cây
    def _height(self, node):
        if node is None:
            return 0
        return max(self._height(node.left), self._height(node.right)) + 1

    def height(self):
        return self._height(self.root)

    def search(self, masv):
        return self._search_recursive(self.root, masv)

    def _search_recursive(self, node, masv):
        if node is None or node.masv == masv:
            return node
        if masv < node.masv:
            return self._search_recursive(node.left, masv)
        return self._search_recursive(node.right, masv)

    # xoá 1 node có mã sv được nhập
    def delete(self, masv):
        self.root = self._delete_recursive(self.root, masv)

    def _delete_recursive(self, node, masv):
        if node is None:
            return node
        if masv < node.masv:
            node.left = self._delete_recursive(node.left, masv)
        elif masv > node.masv:
            node.right = self._delete_recursive(node.right, masv)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.masv = temp.masv
            node.right = self._delete_recursive(node.right, temp.masv)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def sort(self):
        sorted_list = []
        self._inorder_append(self.root, sorted_list)
        self.root = None
        for student in sorted_list:
            self.insert(student.masv, student.hoten,
                        student.malop, student.diem_tb)

    def _inorder_append(self, node, sorted_list):
        if node:
            self._inorder_append(node.left, sorted_list)
            sorted_list.append(node)
            self._inorder_append(node.right, sorted_list)


def main():
    bst = Tree()
    n = int(input("Nhập số sinh viên: "))
    for _ in range(n):
        bst.add_student()

    print("Duyệt và xuất dữ liệu của cây theo thứ tự LNR (MASV):")
    bst.in_order_print()

    print("\nSố nút của cây:", bst.count_nodes())

    print("Chiều cao của cây:", bst.height())

    masv_search = input("Nhập mã sinh viên cần tìm kiếm: ")
    student_found = bst.search(masv_search)
    if student_found:
        print("Thông tin sinh viên cần tìm kiếm:")
        print("MASV:", student_found.masv, "- Họ tên:", student_found.hoten,
              "- Mã lớp:", student_found.malop, "- Điểm TB:", student_found.diem_tb)
    else:
        print("Không tìm thấy sinh viên có mã", masv_search)

    masv_delete = input("Nhập mã sinh viên cần xóa: ")
    bst.delete(masv_delete)
    print("Sau khi xóa, số nút của cây:", bst.count_nodes())

    print("Sắp xếp cây theo MASV:")
    bst.sort()

    print("Duyệt và xuất dữ liệu của cây theo thứ tự LNR (MASV) sau khi sắp xếp:")
    bst.in_order_print()


main()
