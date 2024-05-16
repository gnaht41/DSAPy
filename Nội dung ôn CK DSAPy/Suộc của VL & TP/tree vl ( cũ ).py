class Nut:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Nut(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.value:
            if node.left == None:
                node.left = Nut(data)
            else:
                self._insert(data, node.left)
        elif data > node.value:
            if node.right == None:
                node.right = Nut(data)
            else:
                self._insert(data, node.right)

    def PrintTree(self):
        self._print(self.root)

    def _print(self, node):
        if node:
            self._print(node.left)
            print(node.value)
            self._print(node.right)


def main():
    root = BinaryTree()
    root.insert(14)
    root.insert(17)
    root.insert(3)
    root.insert(8)
    root.PrintTree()


if __name__ == "__main__":
    main()
