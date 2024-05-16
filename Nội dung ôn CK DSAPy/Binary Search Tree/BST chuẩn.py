class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None
    # 1.Chèn vào cây

    def insert(self, node, data):
        if node is None:
            return TreeNode(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            elif data > node.data:
                node.right = self.insert(node.right, data)
        return node

    def _insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        self.root = self.insert(self.root, data)

    # 2.Kiểm tra cây rỗng
    def isEmpty(self, node):
        return node is None

    def _isEmpty(self):
        return self.isEmpty(self.root)

    # 3.Kiểm tra nút n có phải là nút lá không.
    def isLeaf(self, node):
        return node.left is None and node.right is None

    def _isLeaf(self, node):
        return self.isLeaf(node)

    # 4.Kiểm tra nút n có phải là nút cha của nút m không.
    def isParentOf(self, parent, child):
        if parent.left == child or parent.right == child:
            return True
        return False

    def _isParentOf(self, parent, child):
        return self.isParentOf(parent, child)

    # 5. Tính chiều cao của cây.
    def height(self, node):
        if node is None:
            return 0
        else:
            leftHeight = self.height(node.left)
            rightHeight = self.height(node.right)
        return max(leftHeight, rightHeight)+1

    def _height(self):
        return self.height(self.root)

    # 6.Tính số nút của cây
    def countNode(self, node):
        if node is None:
            return 0
        return 1+self.countNode(node.left)+self.countNode(node.right)

    def _countNode(self):
        return self.countNode(self.root)

    # 7.Duyệt tiền tự, trung tự, hậu tự.
    def preOrder(self, node):
        if node:
            print(node.data, end=', ')
            self.preOrder(node.left)
            self.preOrder(node.right)

    def _preOrder(self):
        return self.preOrder(self.root)

    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            print(node.data, end=', ')
            self.inOrder(node.right)

    def _inOrder(self):
        return self.inOrder(self.root)

    def postOrder(self, node):
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data, end=', ')

    def _postOrder(self):
        return self.postOrder(self.root)

    # 8.Đếm số nút lá của cây.
    def countLeaf(self, node):
        if node is None:
            return 0
        count = 0
        if node.left is None and node.right is None:
            count = 1
        return count+self.countLeaf(node.left)+self.countLeaf(node.right)

    def _countLeaf(self):
        return self.countLeaf(self.root)

    # 9.Đếm số nút trung gian của cây.
    def countIntermediate(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 0
        count = 0
        if node != self.root and (node.left is not None or node.right is not None):
            count = 1
        return count+self.countIntermediate(node.left)+self.countIntermediate(node.right)

    def _countIntermediate(self):
        return self.countIntermediate(self.root)

    # 10.Nút có giá trị lớn nhất, nhỏ nhất, tổng giá trị các nút, trung bình giá trị các nút
    def maxVal(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def _maxVal(self):
        return self.maxVal(self.root).data

    def minVal(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _minVal(self):
        return self.minVal(self.root).data

    def sumNode(self, node):
        if node is None:
            return 0
        return node.data+self.sumNode(node.left)+self.sumNode(node.right)

    def _sumNode(self):
        return self.sumNode(self.root)

    def avgNode(self, node):
        if node is None:
            return 0
        return self.sumNode(node)/self.countNode(node)

    def _avgNode(self):
        return self.sumNode(self.root)/self.countNode(self.root)

    # 11.Đếm số nút có đúng 1 con
    def countNodeOneChild(self, node):
        if node is None:
            return 0
        count = 0
        if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
            count = 1
        return count+self.countNodeOneChild(node.left)+self.countNodeOneChild(node.right)

    def _countNodeOneChild(self):
        return self.countNodeOneChild(self.root)

    # 12.Đếm số nút có đúng 2 con
    def countNodeTwoChild(self, node):
        if node is None:
            return 0
        count = 0
        if node.left is not None and node.right is not None:
            count = 1
        return count+self.countNodeTwoChild(node.left)+self.countNodeTwoChild(node.right)

    def _countNodeTwoChild(self):
        return self.countNodeTwoChild(self.root)

    # 13.Đếm số nguyên tố trên cây
    def isPrime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    def countPrime(self, node):
        if node is None:
            return 0
        count = 0
        if self.isPrime(node.data):
            count = 1
        return count+self.countPrime(node.left)+self.countPrime(node.right)

    def _countPrime(self):
        return self.countPrime(self.root)

    # 14.Tính tổng các nút có đúng 1 con
    def sumNodeOneChild(self, node):
        if node is None:
            return 0
        sum = 0
        if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
            sum += node.data
        return sum+self.sumNodeOneChild(node.left)+self.sumNodeOneChild(node.right)

    def _sumNodeOneChild(self):
        return self.sumNodeOneChild(self.root)

    # 15.Tính tổng các nút có đúng 2 con
    def sumNodeTwoChild(self, node):
        if node is None:
            return 0
        sum = 0
        if node.left is not None and node.right is not None:
            sum += node.data
        return sum+self.sumNodeTwoChild(node.left)+self.sumNodeTwoChild(node.right)

    def _sumNodeTwoChild(self):
        return self.sumNodeTwoChild(self.root)

    # 16.Tính tổng các số chẵn
    def sumEven(self, node):
        if node is None:
            return 0
        sum = 0
        if node.data % 2 == 0:
            sum += node.data
        return sum+self.sumEven(node.left)+self.sumEven(node.right)

    def _sumEven(self):
        return self.sumEven(self.root)

    # 17.Nhập x, tìm giá trị nhỏ nhất trên cây mà lớn hơn x
    def minGreaterThan(self, node, x):
        if node is None:
            return None
        minVal = None
        while node is not None:
            if node.data > x:
                minVal = node.data
                node = node.left
            else:
                node = node.right
        return minVal

    def _minGreaterThan(self, x):
        return self.minGreaterThan(self.root, x)

    # 18.Xuất số nguyên tố nhỏ nhất trên cây
    def minPrime(self, node):
        if node is None:
            return None
        stack = []
        current = node
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                if self.isPrime(current.data):
                    return current
                current = current.right
            else:
                break
        return None

    def _minPrime(self):
        return self.minPrime(self.root)

    # 19.Nhập x, tìm x trên cây, nếu tìm thấy x thì cho biết x có bao nhiêu con
    def search(self, node, target):
        if node is None:
            return None
        elif node.data == target:
            return node
        elif target < node.data:
            return self.search(node.left, target)
        elif target > node.data:
            return self.search(node.right, target)

    def _search(self, target):
        return self.search(self.root, target)

    def countNodeChild(self, node, x):
        if node is None:
            return 0
        count = 0
        if node.data == x:
            if node.left is not None:
                count += 1
            if node.right is not None:
                count += 1
        return count+self.countNodeChild(node.left, x)+self.countNodeChild(node.left, x)

    def _countNodeChild(self, x):
        return self.countNodeChild(self.root, x)

    # 20.Xóa 1 nút
    def delete(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            if not node.right:
                temp = node.left
                node = None
                return temp
            node.data = self.minVal(node.right).data
            node.right = self.delete(node.right, node.data)
        return node

    def _delete(self, data):
        return self.delete(self.root, data)

    # 21.Ghi kết quả vào file và đọc file
    def inOrderToFile(self, node, file):
        if node:
            self.inOrderToFile(node.left, file)
            print(node.data, end=', ', file=file)
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
    print('\nMENU')
    print('\n1.Chèn vào cây')
    print('\n2.Kiểm tra cây rỗng')
    print('\n3.Kiểm tra nút n có phải là nút lá không.')
    print('\n4.Kiểm tra nút n có phải là nút cha của nút m không.')
    print('\n5.Tính chiều cao của cây.')
    print('\n6.Tính số nút của cây')
    print('\n7.Duyệt tiền tự, trung tự, hậu tự. ')
    print('\n8.Đếm số nút lá của cây.')
    print('\n9.Đếm số nút trung gian của cây.')
    print('\n10.Nút có giá trị lớn nhất, nhỏ nhất, tổng giá trị các nút, trung bình giá trị các nút')
    print('\n11.Đếm số nút có đúng 1 con')
    print('\n12.Đếm số nút có đúng 2 con')
    print('\n13.Đếm số nguyên tố trên cây')
    print('\n14.Tính tổng các nút có đúng 1 con')
    print('\n15.Tính tổng các nút có đúng 2 con')
    print('\n16.Tính tổng các số chẵn')
    print('\n17.Nhập x, tìm giá trị nhỏ nhất trên cây mà lớn hơn x')
    print('\n18.Xuất số nguyên tố nhỏ nhất trên cây')
    print('\n19.Nhập x, tìm x trên cây, nếu tìm thấy x thì cho biết x có bao nhiêu con')
    print('\n20.Xóa 1 nút')
    print('\n21.Ghi kết quả vào file và đọc file')
    print('\n0.Thoát')
    print('\n\n')

    bst = BSTree()
    while True:
        choose = int(input('\nNhập lựa chọn của bạn : '))
        if choose == 1:
            nodes = [20, 15, 30, 13, 17, 25, 51]
            for node in nodes:
                bst._insert(node)
            print('\nNhập thành công!')
            bst._inOrder()
            print('\n')

        elif choose == 2:
            if bst._isEmpty():
                print('\nCây đang rỗng!')
            else:
                print('\nCây ko rỗng!')
            print('\n')

        elif choose == 3:
            nodeLeaf = int(input('\nNhập node muốn check có phải node lá : '))
            checkLeaf = bst._search(nodeLeaf)

            if bst._isLeaf(checkLeaf):
                print('\nĐây là node lá !')
            else:
                print('\nĐây ko phải node lá!')
            print('\n')

        elif choose == 4:
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

        elif choose == 5:
            print(f'\nChiều cao của cây là : {bst._height()}')
            print('\n')

        elif choose == 6:
            print(f'\nSố nút của cây là : {bst._countNode()}')
            print('\n')

        elif choose == 7:
            bst._preOrder()
            print('\n')
            bst._inOrder()
            print('\n')
            bst._postOrder()
            print('\n')

        elif choose == 8:
            print(f'\nSố nút lá của cây là : {
                  bst._countLeaf()}')
            print('\n')

        elif choose == 9:
            print(f'\nSố nút trung gian của cây là : {
                  bst._countIntermediate()}')
            print('\n')

        elif choose == 10:
            print(f'\nNút lớn nhất của cây là : {bst._maxVal()}')
            print(f'\nNút bé nhất của cây là : {bst._minVal()}')
            print(f'\nTổng các node của cây là : {bst._sumNode()}')
            print(f'\nTrung bình các node của cây là : {bst._avgNode()}')
            print('\n')

        elif choose == 11:
            print(f'\nSố nút có đúng 1 node con là : {
                  bst._countNodeOneChild()}')
            print('\n')

        elif choose == 12:
            print(f'\nSố nút có đúng 2 node con là : {
                  bst._countNodeTwoChild()}')
            print('\n')

        elif choose == 13:
            print(f'\nSố nút nguyên tố là : {
                  bst._countPrime()}')
            print('\n')

        elif choose == 14:
            print(f'\nTổng nút có 1 node con là : {
                  bst._sumNodeOneChild()}')
            print('\n')

        elif choose == 15:
            print(f'\nTổng nút có 2 node con là : {
                  bst._sumNodeTwoChild()}')
            print('\n')

        elif choose == 16:
            x = int(input('\nNhập x : '))
            print(f'\nNode bé nhất nhưng lớn hơn {
                  x} là : {bst._minGreaterThan(x)}')
            print('\n')

        elif choose == 17:
            print(f'\nSố nguyên tố bé nhất trên cây là : {
                  bst._minPrime().data}')
            print('\n')

        elif choose == 18:
            x = int(input('\nNhập x : '))
            if bst._search(x):
                print('\nTìm thấy x')
                print(f'{x} có {bst._countNodeChild(x)} node con')
            else:
                print('\nKo tìm thấy x')
            print('\n')

        elif choose == 19:
            nodeDel = int(input('\nNhập node muốn xóa: '))
            bst._delete(nodeDel)
            print('\nKQ sau khi xóa : ')
            bst._inOrder()
            print('\n')

        elif choose == 20:
            bst._writeToFile(
                'D:/CTDL&GT/Nội dung ôn CK DSAPy/Binary Search Tree/KQ.txt')
            bst._readFromFile(
                'D:/CTDL&GT/Nội dung ôn CK DSAPy/Binary Search Tree/KQ.txt')
            print('\n')

        elif choose == 0:
            break


if __name__ == '__main__':
    main()
