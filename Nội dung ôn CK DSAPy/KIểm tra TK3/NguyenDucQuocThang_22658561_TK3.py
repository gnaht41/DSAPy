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

    # 1.	Duyệt LRN in kết quả ra màn hình(1đ)
    def LRNTraversal(self, node):
        if node is None:
            return
        self.LRNTraversal(node.left)
        self.LRNTraversal(node.right)
        print(node.data, end=',')

    # 2.	Duyệt RLN in kết quả ra màn hình(1đ)
    def RLNTraversal(self, node):
        if node is None:
            return
        self.RLNTraversal(node.right)
        self.RLNTraversal(node.left)
        print(node.data, end=',')

    # 3.	Tìm node có giá trị bất kỳ trong cây(2đ)
    # •	Vd: giá trị cần tìm là 18
    # •	Trong trường hợp tìm thấy xuất thông báo “Tìm thấy node 18 trong cây”. Ngược lại “không tìm thấy node 18 trong cây”
    def search(self, node, target):
        if node is None:
            return None
        elif node.data == target:
            return node
        elif target < node.data:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)

    # 4.	Đếm số lượng node chẵn trong cây(2đ)
    def countEvenNodes(self, node):
        if node is None:
            return 0
        count = 0
        if node.data % 2 == 0:
            count = 1
        return count + self.countEvenNodes(node.left) + self.countEvenNodes(node.right)

    # Xóa node 15 ra khỏi cây. Hiển thị ra kết quả sau khi xóa(2đ)
    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    def delete(self, node, data):
        if not node:
            return None
        elif data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp

            node.data = self.minValueNode(node.right).data
            node.right = self.delete(node.right, node.data)
        return node

    # 5. Ghi kết quả vào file KQ.txt (1đ)

    def writeToFile(self, node, filename):
        with open(filename, 'w') as f:
            self.LRNTraversalToFile(node, f)

    def LRNTraversalToFile(self, node, file):
        if node is None:
            return
        self.LRNTraversalToFile(node.left, file)
        self.LRNTraversalToFile(node.right, file)
        print(node.data, end=',', file=file)


def main():
    bst = BSTree()
    nodes = [15, 18, 3, 6, 7, 20]
    for node in nodes:
        bst.root = bst.insert(bst.root, node)

    bst.LRNTraversal(bst.root)

    if bst.search(bst.root, 18) == None:
        print('\nKhông tìm thấy node 18 trong cây')
    else:
        print('\nTìm thấy node 18 trong cây')

    num_even_nodes = bst.countEvenNodes(bst.root)
    print(f"Số lượng node chẵn trong cây là: {num_even_nodes}")

    print("\nGhi kết quả vào file KQ.txt")
    bst.writeToFile(
        bst.root, "D:/CTDL&GT/Nội dung ôn CK DSAPy/KIểm tra TK3/KQ.txt")


if __name__ == '__main__':
    main()
