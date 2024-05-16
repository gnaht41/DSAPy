class sv:
    def __init__(self, maSV, ten, diem):
        self.maSV = maSV
        self.ten = ten
        self.diem = diem
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
    # Chèn

    def _insert(self, node, maSV, ten, diem):
        if maSV == node.maSV:
            print("Trùng mã sinh viên")
            return
        if maSV < node.maSV:
            if node.left is None:
                node.left = sv(maSV, ten, diem)
            else:
                self._insert(node.left, maSV, ten, diem)
        else:
            if node.right is None:
                node.right = sv(maSV, ten, diem)
            else:
                self._insert(node.right, maSV, ten, diem)

    def insert(self, maSV, ten, diem):
        if self.is_empty(self.root):
            self.root = sv(maSV, ten, diem)
        else:
            self._insert(self.root, maSV, ten, diem)
    # Thêm

    def add(self):
        maSV = int(input('Nhập mã sinh viên: '))
        ten = input('Nhập tên sinh viên: ')
        diem = float(input('Nhập điểm của sinh viên: '))
        self.insert(maSV, ten, diem)
    # In

    def _in_print(self, node):
        if node:
            self._in_print(node.left)
            print(
                f'(MaSV: {node.maSV} - ten: {node.ten} - diem: {node.diem})', end=' ')
            self._in_print(node.right)

    def _print(self):
        self._in_print(self.root)
    # Đếm số lượng lá

    def _in_count(self, node):
        if node is None:
            return 0
        return 1 + self._in_count(node.left) + self._in_count(node.right)

    def _count(self):
        return self._in_count(self.root)
    # Đếm số nút lá

    def _count_leaf_nodes(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaf_nodes(node.left) + self._count_leaf_nodes(node.right)

    def count_leaf_nodes(self):
        return self._count_leaf_nodes(self.root)
    # Min

    def _min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    # Xóa

    def _detele(self, node, masv):
        if node is None:
            return node
        if masv < node.maSV:
            node.left = self._detele(node.left, masv)
        elif masv > node.maSV:
            node.right = self._detele(node.right, masv)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._min(node.right)
                node.maSV = temp.maSV
                node.ten = temp.ten
                node.diem = temp.diem
                node.right = self._detele(node.right, temp.maSV)
        return node

    def _in_delete(self, masv):
        self.root = self._detele(self.root, masv)
    # Tính chiều cao của cây

    def _height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
        return max(left_height, right_height) + 1

    def height(self):
        return self._height(self.root)
    # Tìm kiếm một node có maSV

    def search(self, maSV):
        return self._search(self.root, maSV)

    def _search(self, node, maSV):
        if node is None or node.maSV == maSV:
            return node
        if maSV < node.maSV:
            return self._search(node.left, maSV)
        else:
            return self._search(node.right, maSV)
    # Kiểm tra cây rỗng

    def is_empty(self, node):
        return node is None
    # Kiểm tra nút có phải nút lá hay không

    def is_leafNode(self, node):
        return node.left is None and node.right is None
    # Kiểm tra nút n có phải là nút cha của nút m không

    def is_parent(self, n, m):
        if n.left is None or m is None:
            return False
        if n.left == m or n.right == m:
            return True
        return self.is_parent(n.left, m) or self.is_parent(n.right, m)
    # Duyệt tuần tự

    def _tuanTu(self, node):
        if node:
            print(
                f'(MaSV: {node.maSV} - ten: {node.ten} - diem: {node.diem})', end=' ')
            self._tuanTu(node.left)
            self._tuanTu(node.right)

    def tuanTu(self):
        self._tuanTu(self.root)
    # Duyệt trung tự

    def _trungTu(self, node):
        if node:
            self._trungTu(node.left)
            print(
                f'(MaSV: {node.maSV} - ten: {node.ten} - diem: {node.diem})', end=' ')
            self._trungTu(node.right)

    def trungTu(self):
        self._trungTu(self.root)
    # Duyệt hậu tự

    def _hauTu(self, node):
        if node:
            self._hauTu(node.right)
            self._hauTu(node.left)
            print(
                f'(MaSV: {node.maSV} - ten: {node.ten} - diem: {node.diem})', end=' ')

    def hauTu(self):
        self._hauTu(self.root)
    # Đếm số nút trung gian của cây

    def _count_parent(self, node):
        if node is None:
            return 0
        if node.left is not None or node.right is not None:
            return 1 + self._count_parent(node.left) + self._count_parent(node.right)
        return self._count_parent(node.left) + self._count_parent(node.right)

    def count_parent(self):
        return self._count_parent(self.root)
    # Tìm nút có giá trị lớn nhất

    def _max_node(self, node):
        if node is None:
            return None

    def _max(self):
        return self._max_node(self.root)
    # Đếm số có giá trị nhỏ nhất

    def _min_node(self, node):
        if node is None:
            return None
        current = node
        while current.left is not None:
            current = current.left
        return current.maSV

    def _min(self):
        return self._min_node(self.root)
    # Tổng giá trị của cây

    def _sum_in(self, node):
        if node is None:
            return None
        if node.right is None and node.left is None:
            return node.maSV
        elif node.right is None:
            return node.left.maSV + node.maSV
        elif node.left is None:
            return node.right.maSV + node.maSV
        return self._sum_in(node.left) + self._sum_in(node.right)

    def _sum(self):
        return self._sum_in(self.root)
    # Tính giá trị trung bình các nút

    def _avl(self):
        return self._sum() / self._count()
    # Tìm max của điểm sinh viên

    def max_score(self, node):
        if node is None:
            return None
        temp = node.diem
        if node.left is not None:
            temp = max(temp, self.max_score(node.left))
        if node.right is not None:
            temp = max(temp, self.max_score(node.right))
        return temp

    def _max_score(self):
        return self.max_score(self.root)
    # Tìm min của điểm sinh viên

    def min_score(self, node):
        if node is None:
            return None
        temp = node.diem
        if node.left is not None:
            temp = min(temp, self.min_score(node.left))
        if node.right is not None:
            temp = min(temp, self.min_score(node.right))
        return temp

    def _min_score(self):
        return self.min_score(self.root)

    # Tính tổng giá trị các nút
    def sum_score(self, node):
        if node == None:
            return 0
        return node.diem + self.sum_score(node.left) + self.sum_score(node.right)

    def _sum_score(self):
        return self.sum_score(self.root)
    # Trung bình điểm

    def avl_score(self):
        return self._sum_score() / self._count()


def main():
    root = Tree()
    print("----------Menu----------")
    print("1. Nhập")
    print("2. Xuất")
    print("3. Kích thước của cây")
    print("4. Đếm số nút lá")
    print("5. Xóa một nút trong cây")
    print("6. Tính chiều cao của cây")
    print("7. Tìm kiếm node")
    print("8. Kiểm tra n có phải nút lá hay không")
    print("9. Kiểm tra nút n có phải là nút cha của m không")
    print("10. Duyệt tuần tự - duyệt trung tự - duyệt hậu tự")
    print("11. Đếm số nút trung gian trong cây")
    print("12. Nút có giá trị lớn nhất, nhỏ nhất, tổng giá trị các nút, trung bình giá trị các nút")
    print("13. Yêu cầu giống câu 12 nhưng làm theo điểm thi")
    while True:
        n = int(input('\nNhập lựa chọn của bạn: '))
        if n == 1:
            a = int(input('Nhập số lượng sinh viên: '))
            for i in range(a):
                print(f'Sinh viên {i+1}: ')
                root.add()
        elif n == 2:
            root._print()
        elif n == 3:
            print('Kích thước của cây là', root._count())
        elif n == 4:
            print('Số nút lá có trong cây: ', root.count_leaf_nodes())
        elif n == 5:
            c = int(input('Nhập mã sinh viên cần xóa: '))
            root._in_delete(c)
            print(f'Đã xóa sinh viên có mã số {c}')
        elif n == 6:
            print('Chiều cao của cây là: ', root.height())
        elif n == 7:
            d = int(input('Nhập mã sinh viên cần tìm: '))
            tam = root.search(d)
            if tam is None:
                print('Không tìm thấy mã sinh viên')
            else:
                print(f'Mã sinh viên: {
                      tam.maSV} - Tên sinh viên: {tam.ten} - Điểm sinh viên: {tam.diem}')
        elif n == 8:
            e = int(input('Nhập số cần kiểm tra'))
            tim = root.search(e)
            if tim:
                if root.is_leafNode(tim):
                    print(f'{e} là nút lá')
                else:
                    print(f'{e} không là nút lá')
            else:
                print(f'không tìm thấy {e}')
        elif n == 9:
            f = int(input('Nhập nút n'))
            g = int(input('Nhập nút m'))
            parent = root.search(f)
            children = root.search(g)
            if parent is None or children is None:
                print(f'Không có nút {f} hoặc {g} trong cây')
            else:
                if root.is_parent(parent, children):
                    print(f'{f} là nút cha của {g}')
                else:
                    print(f'{f} không là nút cha của {g}')
        elif n == 10:
            print(''''
                  1. Duyệt tuần tự
                  2. Duyệt trung tự
                  3. Duyệt hậu tự
                  ''')
            lc = int(input('Nhập lựa chọn của bạn '))
            if lc == 1:
                root.tuanTu()
            elif lc == 2:
                root.trungTu()
            elif lc == 3:
                root.hauTu()
        elif n == 11:
            print("Tổng số nút cha trong cây là: ", root.count_parent())
        elif n == 12:
            print(''''
                  1. Nút có giá trị lớn nhất
                  2. Nút có giá trị nhỏ nhất
                  3. Tổng giá trị các nút
                  4. Trung bình giá trị các nút
                  ''')
            lc1 = int(input('Nhập lựa chọn của bạn '))
            if lc1 == 1:
                print('Giá trị lớn nhất là: ', root._max())
            elif lc1 == 2:
                print('Giá trị nhỏ nhất là: ', root._min())
            elif lc1 == 3:
                print('Tổng giá trị: ', root._sum())
            elif lc1 == 4:
                print('Giá trị trung bình của các nút: ', root._avl())
        elif n == 13:
            print(''''
                  1. Nút có giá trị lớn nhất
                  2. Nút có giá trị nhỏ nhất
                  3. Tổng giá trị các nút
                  4. Trung bình giá trị các nút
                  ''')
            lc2 = int(input('Nhập lựa chọn của bạn '))
            if lc2 == 1:
                print('Giá trị lớn nhất là: ', root._max_score())
            elif lc2 == 2:
                print('Giá trị nhỏ nhất là: ', root._min_score())
            elif lc2 == 3:
                print('Tổng giá trị: ', root._sum_score())
            elif lc2 == 4:
                print('Giá trị trung bình của các nút: ', root.avl_score())


if __name__ == "__main__":
    main()
