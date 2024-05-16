class Student:
    def __init__(self, maSV, hoTen, maLop, diemTB):
        self.maSV = maSV
        self.hoTen = hoTen
        self.maLop = maLop
        self.diemTB = diemTB
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    # 1.	Nhập dữ liệu cho cây. Mỗi node là thông tin một sinh viên gồm: Masv, Hoten, Malop, ĐiemTB.
    # Kiểm tra nếu masv trùng thì thông báo trùng và nhập lại masv khác. Trong đó MASV là khoá chính.
    def addStudent(self):
        maSV = int(input('\nNhập mssv : '))
        hoTen = input('\nNhập họ tên : ')
        maLop = input('\nNhập mã lớp : ')
        diemTB = float(input('\nNhập điểm trung bình : '))
        self._insert(maSV, hoTen, maLop, diemTB)

    # 2.	Đếm số nút lá của cây
    def countLeaf(self, node):
        if node is None:
            return 0
        count = 0
        if node.left is None and node.right is None:
            count = 1
        return count+self.countLeaf(node.left)+self.countLeaf(node.right)

    def _countLeaf(self):
        return self.countLeaf(self.root)

    # 3.	Tính chiều cao của cây
    def height(self, node):
        if node is None:
            return 0
        else:
            heightLeft = self.height(node.left)
            heightRight = self.height(node.right)
        return max(heightLeft, heightRight)+1

    def _height(self):
        return self.height(self.root)

    # 4.	Chèn một Node vào cây.
    def insert(self, node, maSV, hoTen, maLop, diemTB):
        if maSV == node.maSV:
            print('\nTrùng mã!')
            return
        if maSV < node.maSV:
            if node.left is None:
                node.left = Student(maSV, hoTen, maLop, diemTB)
            else:
                self.insert(node.left, maSV, hoTen, maLop, diemTB)
        else:
            if node.right is None:
                node.right = Student(maSV, hoTen, maLop, diemTB)
            else:
                self.insert(node.right, maSV, hoTen, maLop, diemTB)

    def _insert(self, maSV, hoTen, maLop, diemTB):
        if self.root is None:
            self.root = Student(maSV, hoTen, maLop, diemTB)
        else:
            self.insert(self.root, maSV, hoTen, maLop, diemTB)

    # 5.	Tìm kiếm một Node có giá trị MASV được nhập vào từ bàn phím.
    def search(self, node, maSV):
        if node is None:
            return None
        elif node.maSV == maSV:
            return node
        elif maSV < node.maSV:
            return self.search(node.left, maSV)
        elif maSV > node.maSV:
            return self.search(node.right, maSV)

    def _search(self, maSV):
        return self.search(self.root, maSV)

    # 6.	Xóa một Node có MASV được nhập vào từ bàn phím.
    def delete(self, node, maSV):
        if node is None:
            return None
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
                temp = self.minVal(node.right)
                node.maSV = temp.maSV
                node.hoTen = temp.hoTen
                node.maLop = temp.maLop
                node.diemTB = temp.diemTB
                node.right = self.delete(node.right, node.maSV)
        return node

    def _delete(self, maSV):
        return self.delete(self.root, maSV)

    # 7.	Kiểm tra cây rỗng
    def isEmpty(self, node):
        if node is None:
            return True
        return False

    def _isEmpty(self):
        return self.isEmpty(self.root)

    # 8.	Kiểm tra nút n có phải là nút lá không.
    def isLeaf(self, node):
        return node.left is None and node.right is None

    def _isLeaf(self, node):
        return self.isLeaf(node)

    # 9.	Kiểm tra nút n có phải là nút cha của nút m không.
    def isParentOf(self, parent, child):
        if parent.left == child or parent.right == child:
            return True
        return False

    def _isParentOf(self, parent, child):
        return self.isParentOf(parent, child)

    # 10.	Duyệt tiền tự (NLR), trung tự (LNR), hậu tự (LRN).
    def preOrder(self, node):
        if node:
            print('Ma sv : ', node.maSV, 'Ho ten : ', node.hoTen,
                  'Ma lop : ', node.maLop, 'Diem tb : ', node.diemTB, end='\n')
            self.preOrder(node.left)
            self.preOrder(node.right)

    def _preOrder(self):
        return self.preOrder(self.root)

    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            print('Ma sv : ', node.maSV, 'Ho ten : ', node.hoTen,
                  'Ma lop : ', node.maLop, 'Diem tb : ', node.diemTB, end='\n')
            self.inOrder(node.right)

    def _inOrder(self):
        return self.inOrder(self.root)

    def postOrder(self, node):
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print('Ma sv : ', node.maSV, 'Ho ten : ', node.hoTen,
                  'Ma lop : ', node.maLop, 'Diem tb : ', node.diemTB, end='\n')

    def _postOrder(self):
        return self.postOrder(self.root)

    # 11.	Đếm số nút trung gian của cây.
    def countIntermediate(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 0
        count = 0
        if node is self.root and (node.left is not None or node.right is not None):
            count = 1
        return count+self.countIntermediate(node.left)+self.countIntermediate(node.right)

    def _countIntermediate(self):
        return self.countIntermediate(self.root)

    # 12.	Nút có giá trị lớn nhất, nhỏ nhất, tổng giá trị các nút, trung bình giá trị các nút
    def minVal(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _minVal(self):
        return self.minVal(self.root)

    def minScore(self, node):
        if node is None:
            return None
        temp = node.diemTB
        if node.left is not None:
            temp = min(temp, self.minScore(node.left))
        if node.right is not None:
            temp = min(temp, self.minScore(node.right))
        return temp

    def _minScore(self):
        return self.minScore(self.root)

    def maxScore(self, node):
        if node is None:
            return None
        temp = node.diemTB
        if node.left is not None:
            temp = max(temp, self.maxScore(node.left))
        if node.right is not None:
            temp = max(temp, self.maxScore(node.right))
        return temp

    def _maxScore(self):
        return self.maxScore(self.root)

    def sumScore(self, node):
        if node is None:
            return 0
        return node.diemTB+self.sumScore(node.left)+self.sumScore(node.right)

    def _sumScore(self):
        return self.sumScore(self.root)

    def avgScore(self, node):
        if node is None:
            return 0
        return self.sumScore(node)/self.countNode(node)

    def _avgScore(self):
        return self.avgScore(self.root)

    # 13.	Tính và trả về số lượng các node của cây nhị phân gồm các giá trị nguyên
    # Gợi ý:  tham khảo hàm NLR để viết hàm CountNode
    def countNode(self, node):
        if node is None:
            return 0
        return 1+self.countNode(node.left)+self.countNode(node.right)

    def _countNode(self):
        return self.countNode(self.root)

    # 14.	Ghi vào và đọc file
    def inOrderToFile(self, node, file):
        if node:
            self.inOrderToFile(node.left, file)
            print('Ma sv : ', node.maSV, 'Ho ten : ', node.hoTen,
                  'Ma lop : ', node.maLop, 'Diem tb : ', node.diemTB, end='\n', file=file)
            self.inOrderToFile(node.right, file)

    def writeToFile(self, node, file):
        with open(file, 'w') as f:
            self.inOrderToFile(node, f)

    def _writeToFile(self, file):
        return self.writeToFile(self.root, file)

    def readFromFile(self, file):
        with open(file, 'r') as f:
            content = f.read()
        return content

    def _readFromFile(self, file):
        print(self.readFromFile(file))


def main():
    bst = BSTree()

    print('\nMENU')
    print('\n1.	Nhập dữ liệu cho cây.')
    print('\n2.	Đếm số nút lá của cây')
    print('\n3.	Tính chiều cao của cây')
    print('\n4.	Chèn một Node vào cây.')
    print('\n5.	Tìm kiếm một Node có giá trị MASV được nhập vào từ bàn phím.')
    print('\n6.	Xóa một Node có MASV được nhập vào từ bàn phím. ')
    print('\n7.	Kiểm tra cây rỗng')
    print('\n8.	Kiểm tra nút n có phải là nút lá không.')
    print('\n9.	Kiểm tra nút n có phải là nút cha của nút m không. ')
    print('\n10. Duyệt tiền tự (NLR), trung tự (LNR), hậu tự (LRN).')
    print('\n11. Đếm số nút trung gian của cây.')
    print('\n12. Nút có giá trị lớn nhất, nhỏ nhất, tổng giá trị các nút, trung bình giá trị các nút')
    print('\n13. Tính và trả về số lượng các node của cây nhị phân gồm các giá trị nguyên')
    print('\n14.	Ghi vào và đọc file')
    print('\n\n')
    while True:
        choose = int(input('\nNhập lựa chọn của bạn : '))
        if choose == 1:
            n = int(input('\nNhập số lượng sv: '))
            for i in range(n):
                bst.addStudent()
            bst._inOrder()
            print('\n')

        if choose == 2:
            print(f'\nSố node lá là : {bst._countLeaf()}')
            print('\n')

        if choose == 3:
            print(f'\nChiều cao của cây là : {bst._height()}')
            print('\n')

        if choose == 4:
            bst._insert(5, 'Nguyen Van A', 'K62', 3.0)
            bst._insert(3, 'Tran Van B', 'K62', 2.5)
            bst._insert(7, 'Le Thi C', 'K62', 3.8)
            bst._insert(2, 'Pham Van D', 'K62', 2.8)
            bst._insert(6, 'Hoang Thi E', 'K62', 3.2)
            bst._insert(8, 'Vu Van F', 'K62', 3.7)
            bst._preOrder()
            print('\n')

        if choose == 5:
            maSV = int(input('\nNhập mã sv muốn tìm : '))
            if bst._search(maSV):
                print(f'\nTìm thấy sv có mã {maSV}')
            else:
                print('\nKo tìm thấy sv!')
            print('\n')

        if choose == 6:
            nodeDel = int(input('\nNhập mssv của sv muốn xóa : '))
            bst._delete(nodeDel)
            print('\nKQ sau khi xóa : ')
            bst._preOrder()
            print('\n')

        if choose == 7:
            if bst._isEmpty():
                print('\nCây rỗng!')
            else:
                print('\nCây ko rỗng!')
            print('\n')

        if choose == 8:
            nodeLeaf = int(input('\nNhập node muốn kiểm tra lá : '))
            leafCheck = bst._search(nodeLeaf)
            if bst._isLeaf(leafCheck):
                print('\nĐây là node lá')
            else:
                print('\nĐây ko phải node lá')
            print('\n')

        if choose == 9:
            parent = int(input('\nNhập node cha : '))
            child = int(input('\nNhập node con : '))
            prNode = bst._search(parent)
            chNode = bst._search(child)
            print('\n')
            if bst._isParentOf(prNode, chNode):
                print(f'{parent} là cha của {child}')
            else:
                print(f'{parent} là ko phải cha của {child}')
            print('\n')

        if choose == 10:
            bst._preOrder()
            print('\n')
            bst._inOrder()
            print('\n')
            bst._postOrder()
            print('\n')

        if choose == 11:
            print(f'\nSố nút trung gian của cây là : {
                  bst._countIntermediate()}')
            print('\n')

        if choose == 12:
            print(f'\nNút lớn nhất của cây là : {bst._maxScore()}')
            print(f'\nNút bé nhất của cây là : {bst._minScore()}')
            print(f'\nTổng các node của cây là : {bst._sumScore()}')
            print(f'\nTrung bình các node của cây là : {bst._avgScore()}')
            print('\n')

        if choose == 13:
            print(f'\nSố node trên cây là : {bst._countNode()}')
            print('\n')

        if choose == 14:
            bst._writeToFile(
                'D:/CTDL&GT/Nội dung ôn CK DSAPy/Binary Search Tree/OOP.txt')
            bst._readFromFile(
                'D:/CTDL&GT/Nội dung ôn CK DSAPy/Binary Search Tree/OOP.txt')
            print('\n')


if __name__ == '__main__':
    main()
