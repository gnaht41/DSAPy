class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def _getHeight(self):
        return self.getHeight(self.root)

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left)-self.getHeight(node.right)

    def _getBalance(self):
        return self.getBalance(self.root)

    def rightRotate(self, y):
        print('Xoay phải trong cây : ', y.data)
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1+max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1+max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def leftRotate(self, x):
        print('Xoay trái trong cây : ', x.data)
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1+max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1+max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def insert(self, node, data):
        if not node:
            return TreeNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        node.height = 1+max(self.getHeight(node.left),
                            self.getHeight(node.right))
        balance = self.getBalance(node)

        if balance > 1 and data < node.left.data:
            return self.rightRotate(node)

        if balance < -1 and data > node.right.data:
            return self.leftRotate(node)

        if balance > 1 and data > node.left.data:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        if balance < -1 and data < node.right.data:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def _insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        return self.insert(self.root, data)

    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data, end=', ')
        self.inOrder(node.right)

    def _inOrder(self):
        return self.inOrder(self.root)

    def minVal(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _minVal(self):
        return self.minVal(self.root)

    def delete(self, node, data):
        if not node:
            return node

        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.minVal(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)

        if node is None:
            return node

        # Update the balance factor and balance the tree
        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))
        balance = self.getBalance(node)

        # Balancing the tree
        # Left Left
        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rightRotate(node)

        # Left Right
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Right Right
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.leftRotate(node)

        # Right Left
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def _delete(self, data):
        self.root = self.delete(self.root, data)


def main():
    avl = AVLTree()

    letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']

    for letter in letters:
        avl._insert(letter)

    print('\nCây duyệt kiểu inorder : ')
    avl._inOrder()

    print(f'\n\nGiá trị nhỏ nhất là : {avl._minVal().data}')

    nodeDel = input('\nNhập node muốn xóa : ')
    print('\n')
    avl._delete(nodeDel)

    print('\nKQ sau khi xóa : ')
    avl._inOrder()


if __name__ == '__main__':
    main()
