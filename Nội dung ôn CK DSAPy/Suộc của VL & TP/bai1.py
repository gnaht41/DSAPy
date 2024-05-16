class sv:
    def __init__(self, maSV, ten):
        self.maSV = maSV
        self.ten = ten
        self.left = None
        self.right = None


class tree:
    def __init__(self):
        self.root = None
    # 1.	Kiểm tra cây rỗng

    def is_empty(self, node):
        return node is None
    #    Chèn

    def insert(self, node, maSV, ten):
        if maSV < node.maSV:
            if node.left is None:
                node.left = sv(maSV, ten)
            else:
                self.insert(node.left, maSV, ten)
        elif maSV > node.maSV:
            if node.right is None:
                node.right = sv(maSV, ten)
            else:
                self.insert(node.right, maSV, ten)

    def _insert(self, maSV, ten):
        if self.is_empty(self.root):
            self.root = sv(maSV, ten)
        else:
            self.insert(self.root, maSV, ten)
    # Them

    def _add(self):
        maSV = int(input('Nhập mã sinh viên: '))
        ten = input('Nhập tên sinh viên: ')
        self._insert(maSV, ten)
    # 2.	Duyệt tiền tự, trung tự, hậu tự.

    def NLR(self, node):
        if node:
            print(
                f'(Mã sinh viên: {node.maSV} - Tên sinh viên: {node.ten})', end=' ')
            self.NLR(node.left)
            self.NLR(node.right)

    def _NLR(self):
        self.NLR(self.root)

    # 3.    Xóa một giá trị trong cây
    def delete(self, node, maSV):
        if node is None:
            return node
        if maSV < node.maSV:
            node.left = self.delete(node.left, maSV)
        elif maSV > node.maSV:
            node.right = self.delete(node.right, maSV)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._min(node.right)
                node.maSV = temp.maSV
                node.ten = temp.ten
                node.right = self.delete(node.right, temp.maSV)
        return node

    def _delete(self, maSV):
        self.root = self.delete(self.root, maSV)

    # Min
    def _min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # 4.	Kiểm tra nút n có phải là nút lá không.
    def is_nutLa(self, n):
        return n.left is None and n.right is None

    # 5.	Kiểm tra nút n có phải là nút cha của nút m không.
    def nutCha(self, n, m):
        if n.left == m or n.right == m:
            return True
        else:
            return False

    # Tìm
    def tim(self, node, maSV):
        if node is None or node.maSV == maSV:
            return node
        if maSV < node.maSV:
            return self.tim(node.left, maSV)
        else:
            return self.tim(node.right, maSV)

    def _tim(self, maSV):
        return self.tim(self.root, maSV)

    # 6.    Tính chiều cao cây
    def chieuCao(self, node):
        if node is None:
            return 0
        else:
            tamleft = self.chieuCao(node.left)
            tamright = self.chieuCao(node.right)
        return max(tamleft, tamright) + 1

    def _chieuCao(self):
        return self.chieuCao(self.root)

    # 7.	Tính số nút của cây
    def soNut(self, node):
        if node is None:
            return 0
        return 1 + self.soNut(node.left) + self.soNut(node.right)

    def _soNut(self):
        return self.soNut(self.root)

    # 8.	Đếm số nút lá của cây.
    def nutLa(self, node):
        if node is None:
            return 0
        if self.is_nutLa(node):
            return 1
        return self.nutLa(node.left) + self.nutLa(node.right)

    def _nutLa(self):
        return self.nutLa(self.root)

    # 9.	Đếm số nút trung gian của cây.
    def nutTrungGian(self, node):
        if node is None:
            return 0
        if node.right is not None or node.left is not None:
            return 1 + self.nutTrungGian(node.left) + self.nutTrungGian(node.right)
        return self.nutTrungGian(node.left) + self.nutTrungGian(node.right)

    def _nutTrungGian(self):
        return self.nutTrungGian(self.root) - 1

    # 10.	Nút có giá trị lớn nhất
    def _max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.maSV
    # 11.   nhỏ nhất

    def in_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.maSV
    # 12.   tổng giá trị các nút

    def in_sum(self, node):
        if node is None:
            return 0
        leftSum = self.in_sum(node.left)
        rightSum = self.in_sum(node.right)
        return node.maSV + leftSum + rightSum

    def _sum(self):
        return self.in_sum(self.root)
    # 13.   trung bình giá trị các nút

    def _avl(self):
        if self.root is None:
            return 0
        else:
            return self._sum() / self._soNut()


def main():

    root = tree()
    while True:
        print('\n1. Nhập thông tin viên: ')
        print('2. Duyệt NLR')
        print('3. Delete')
        print('4. Kiểm tra có n phải nút lá không')
        print('5. Kiểm tra n có phải cha của m không')
        print('6. Tính chiều cao của cây')
        print('7. Đếm số nút của cây')
        print('8. Đếm số nút lá của cây')
        print('9. Đếm số nút trung gian')
        print('10. Tìm max của cây')
        print('11. Tìm min của cây')
        print('12. Tính tổng cây')
        print('13. Tính trung bình')
        lc = int(input('\nNhập lựa chọn của bạn: '))
        if lc == 1:
            n = int(input('Nhập số lượng sinh viên: '))
            for i in range(n):
                print(f'\n-----Sinh viên {i+1}-----\n')
                root._add()
        elif lc == 2:
            root._NLR()
        elif lc == 3:
            n1 = int(input('Nhập mã sinh viên cần xóa: '))
            root._delete(n1)
        elif lc == 4:
            n2 = int(input('Nhập số cần kiểm tra: '))
            a = root._tim(n2)
            if a:
                if root.is_nutLa(a):
                    print(f'{n2} là nút lá')
                else:
                    print(f'{n2} không là nút lá')
            else:
                print(f'Không tìm thấy {n2} trong cây')
        elif lc == 5:
            n3 = int(input('Nhập n: '))
            n4 = int(input('Nhập m: '))
            a1 = root._tim(n3)
            a2 = root._tim(n4)
            if a1 is not None and a2 is not None:
                if root.nutCha(a1, a2):
                    print(f'{n3} là nút cha của {n4}')
                else:
                    print(f'{n3} không là nút cha của {n4}')
            else:
                print(f'Không tìm thấy {n3} hoặc {n4}')
        elif lc == 6:
            print('Chiều cao của cây là: ', root._chieuCao())
        elif lc == 7:
            print('Số lượng nút trong cây là: ', root._soNut())
        elif lc == 8:
            print('Số lượng nút lá của cây là: ', root._nutLa())
        elif lc == 9:
            print('Số lượng nút trung gian trong cây là: ', root._nutTrungGian())
        elif lc == 10:
            print('Max của cây là: ', root._max())
        elif lc == 11:
            print('Min của cây là: ', root.in_min())
        elif lc == 12:
            print('Tổng số cây: ', root._sum())
        elif lc == 13:
            print('Trung bình cây: ', root._avl())


if __name__ == '__main__':
    main()
