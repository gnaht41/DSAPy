# Họ tên : Nguyễn Đức Quốc Thắng , MSSV : 22658561 , Số máy : 41 , Đề 2
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

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

    def RLN(self, node):
        if node:
            self.RLN(node.right)
            self.RLN(node.left)
            print(node.data, end=', ')

    def _RLN(self):
        return self.RLN(self.root)

    def NRL(self, node):
        if node:
            print(node.data, end=', ')
            self.NRL(node.right)
            self.NRL(node.left)

    def _NRL(self):
        return self.NRL(self.root)

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

    def minVal(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _minVal(self):
        return self.minVal(self.root).data

    def countOdd(self, node):
        if node is None:
            return 0
        count = 0
        if node.data % 2 != 0:
            count = 1
        return count+self.countOdd(node.left)+self.countOdd(node.right)

    def _countOdd(self):
        return self.countOdd(self.root)

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

    def delete(self, node, data):
        if node is None:
            return node
        elif data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self.minVal(node.right)
                node.data = temp.data
                node.right = self.delete(node.right, temp.data)
        return node

    def _delete(self, data):
        self.root = self.delete(self.root, data)


def main():
    bst = BSTree()

    ds = [18, 15, 20, 18, 40, 30, 50, 61]

    for node in ds:
        bst._insert(node)

    print('MENU:')
    print('\t1.Duyệt RLN')
    print('\t2.Duyệt NRL')
    print('\t3.Đếm số lượng số nguyên tố trên cây ?')
    print('\t4.Tìm node nhỏ nhất của cây?')
    print('\t5.Đếm số node lẻ của cây?')
    print('\t6.Tìm node có giá trị do người dùng nhập')
    print('\t7.Xóa một node có giá trị người dùng nhập, xóa thành công hiển thị cây sau khi xóa')

    while True:
        choose = int(input('\nNhập lựa chọn của bạn : '))
        if choose == 1:
            bst._RLN()
            print('\n')
        elif choose == 2:
            bst._NRL()
            print('\n')
        elif choose == 3:
            print(f'Số lượng số nguyên tố trên cây là : {bst._countPrime()}')
            print('\n')
        elif choose == 4:
            print(f'Node nhỏ nhất trên cây là : {bst._minVal()}')
            print('\n')
        elif choose == 5:
            print(f'Số node lẻ là : {bst._countOdd()}')
            print('\n')
        elif choose == 6:
            n = int(input('\nNhập node muốn kiếm : '))
            if bst._search(n):
                print(f'\nNode {n} có trong cây')
            else:
                print(f'\nKhông tìm thấy node {n} trong cây')
            print('\n')
        elif choose == 7:
            nodeDel = int(input('\nNhập node muốn xóa : '))
            if bst._search(nodeDel):
                print(f'\nCó giá trị {nodeDel}')
                bst._delete(nodeDel)
                print('\nKết quả sau khi xóa: ')
                bst._RLN()
                print('\n')
            else:
                print(f'\nKhông tìm thấy node {n} trong cây')
            print('\n')
        else:
            break


if __name__ == "__main__":
    main()
