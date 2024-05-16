class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Chương trình 1: Kiểm tra cây rỗng
    def is_empty(self):
        return self.root is None

    # Chương trình 2: Kiểm tra nút n có phải là nút lá không
    def is_leaf(self, node):
        return node.left is None and node.right is None

    # Chương trình 3: Kiểm tra nút n có phải là nút cha của nút m không
    def is_parent_of(self, node_n, node_m):
        return (node_n.left == node_m) or (node_n.right == node_m)

    # Chương trình 4: Tính chiều cao của cây
    def tree_height(self):
        def _tree_height(node):
            if node is None:
                return 0
            else:
                return 1 + max(_tree_height(node.left), _tree_height(node.right))
        return _tree_height(self.root)

    # Chương trình 5: Tính số nút của cây
    def count_nodes(self):
        def _count_nodes(node):
            if node is None:
                return 0
            else:
                return 1 + _count_nodes(node.left) + _count_nodes(node.right)
        return _count_nodes(self.root)

    # Chương trình 6: Duyệt tiền tự, trung tự, hậu tự (tiếp tục)

    def preorder_traversal(self):
        def _preorder_traversal(node):
            if node:
                print(node.value, end=" ")
                _preorder_traversal(node.left)
                _preorder_traversal(node.right)
        _preorder_traversal(self.root)

    def inorder_traversal(self):
        def _inorder_traversal(node):
            if node:
                _inorder_traversal(node.left)
                print(node.value, end=" ")
                _inorder_traversal(node.right)
        _inorder_traversal(self.root)

    def postorder_traversal(self):
        def _postorder_traversal(node):
            if node:
                _postorder_traversal(node.left)
                _postorder_traversal(node.right)
                print(node.value, end=" ")
        _postorder_traversal(self.root)

    # Chương trình 7: Đếm số nút lá của cây (tiếp tục)
    def count_leaves(self):
        def _count_leaves(node):
            if node is None:
                return 0
            elif node.left is None and node.right is None:
                return 1
            else:
                return _count_leaves(node.left) + _count_leaves(node.right)
        return _count_leaves(self.root)

    # Chương trình 8: Đếm số nút trung gian của cây (tiếp tục)
    def count_internal_nodes(self):
        def _count_internal_nodes(node):
            if node is None or (node.left is None and node.right is None):
                return 0
            else:
                return 1 + _count_internal_nodes(node.left) + _count_internal_nodes(node.right)
        return _count_internal_nodes(self.root)

    # Chương trình 9: Nút có giá trị lớn nhất, nhỏ nhất, tổng giá trị các nút, trung bình giá trị các nút (tiếp tục)
    def find_max_value(self):
        def _find_max_value(node):
            if node is None:
                return float('-inf')
            else:
                return max(node.value, _find_max_value(node.left), _find_max_value(node.right))
        return _find_max_value(self.root)

    def find_min_value(self):
        def _find_min_value(node):
            if node is None:
                return float('inf')
            else:
                return min(node.value, _find_min_value(node.left), _find_min_value(node.right))
        return _find_min_value(self.root)

    def sum_of_values(self):
        def _sum_of_values(node):
            if node is None:
                return 0
            else:
                return node.value + _sum_of_values(node.left) + _sum_of_values(node.right)
        return _sum_of_values(self.root)

    def average_value(self):
        node_count = self.count_nodes()
        if node_count == 0:
            return 0
        else:
            return self.sum_of_values() / node_count


def main():
    # Tạo một cây nhị phân
    tree = BinaryTree()
    tree.root = TreeNode(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    tree.root.right.left = TreeNode(6)

    # Kiểm tra các chương trình con
    print("Cây rỗng:", tree.is_empty())
    print("Chiều cao của cây:", tree.tree_height())
    print("Số nút của cây:", tree.count_nodes())
    print("Duyệt tiền tự:", end=" ")
    tree.preorder_traversal()
    print("\nDuyệt trung tự:", end=" ")
    tree.inorder_traversal()
    print("\nDuyệt hậu tự:", end=" ")
    tree.postorder_traversal()
    print("\nSố nút lá của cây:", tree.count_leaves())
    print("Số nút trung gian của cây:", tree.count_internal_nodes())
    print("Giá trị lớn nhất của nút:", tree.find_max_value())
    print("Giá trị nhỏ nhất của nút:", tree.find_min_value())
    print("Tổng giá trị các nút:", tree.sum_of_values())
    print("Trung bình giá trị các nút:", tree.average_value())


if __name__ == "__main__":
    main()
