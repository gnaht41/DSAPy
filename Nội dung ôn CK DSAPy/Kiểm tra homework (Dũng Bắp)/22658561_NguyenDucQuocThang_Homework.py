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
        return self.insert(self.root, data)

    # Duyệt cây theo LNR
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data, end=', ')
        self.inOrder(node.right)

    def _inOrder(self):
        return self.inOrder(self.root)

    # Đếm số lượng node là số nguyên tố của cây?
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

    # Tính tổng giá trị các node chẵn của cây?
    def sumEven(self, node):
        if node is None:
            return 0
        sum = 0
        if node.data % 2 == 0:
            sum += node.data
        return sum+self.sumEven(node.left)+self.sumEven(node.right)

    def _sumEven(self):
        return self.sumEven(self.root)

    # Tìm node nhỏ nhất của cây?
    def minVal(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _minVal(self):
        return self.minVal(self.root).data

    # Đếm số node lẻ của cây?
    def countOdd(self, node):
        if node is None:
            return 0
        count = 0
        if node.data % 2 != 0:
            count = 1
        return count+self.countOdd(node.left)+self.countOdd(node.right)

    def _countOdd(self):
        return self.countOdd(self.root)

    # Tìm node có giá trị do người dùng nhập
    def search(self, node, target):
        if node is None:
            return None
        elif node.data == target:
            return node
        elif target < node.data:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)

    def _search(self, target):
        return self.search(self.root, target)

    # Xoá một node có giá trị do người dùng nhập
    def delete(self, node, data):
        if not node:
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


def main():
    bst = BSTree()

    ds = [20, 15, 30, 13, 17, 25, 51]

    for node in ds:
        bst.root = bst._insert(node)
    print('\n-----------------Menu-----------------')
    print('\n1.Duyệt cây theo LNR')
    print('\n2.Đếm số lượng node là số nguyên tố của cây?')
    print('\n3.Tính tổng giá trị các node chẵn của cây?')
    print('\n4.Tìm node nhỏ nhất của cây?')
    print('\n5.Đếm số node lẻ của cây?')
    print('\n6.Tìm node có giá trị do người dùng nhập')
    print('\n7.Xoá một node có giá trị do người dùng nhập')
    print('\n--------------------------------------')
    print('\n')

    while True:
        choose = int(input('\nNhập lựa chọn của bạn : '))

        if choose == 1:
            bst._inOrder()
            print('\n')

        elif choose == 2:
            print(f'\nCó {bst._countPrime()} số nguyên tố!')
            print('\n')

        elif choose == 3:
            print(f'\nTổng giá trị các node chẵn của cây : {
                  bst._sumEven()}')
            print('\n')

        elif choose == 4:
            print(f'\nNode nhỏ nhất của cây : {bst._minVal()}')
            print('\n')

        elif choose == 5:
            print(f'\nCó {bst._countOdd()} node lẻ!')
            print('\n')

        elif choose == 6:
            target = int(input('\nNhập node muốn tìm trên cây : '))
            if bst._search(target):
                print('\nTìm thấy!')
            else:
                print('\nKo tìm thấy!')
            print('\n')

        elif choose == 7:
            print('\nCác node hiện tại có trên cây : ')
            bst._inOrder()
            print('\n')
            delNode = int(input('\nNhập node muốn xóa : '))
            bst._delete(delNode)
            print(f'\nCây sau khi xóa {delNode} là : ')
            bst._inOrder()
            print('\n')

        else:
            break


if __name__ == '__main__':
    main()
