class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        """
        Kiểm tra xem cây có rỗng không.

        Returns:
            bool: True nếu cây rỗng, False nếu không.
        """
        return self.root is None

    def is_leaf(self, node):
        """
        Kiểm tra xem một nút có phải là nút lá không.

        Parameters:
            node (TreeNode): Nút cần kiểm tra.

        Returns:
            bool: True nếu là nút lá, False nếu không.
        """
        return node and not node.left and not node.right

    def is_parent_of(self, parent, child):
        """
        Kiểm tra xem một nút có phải là cha của một nút khác không.

        Parameters:
            parent (TreeNode): Nút cha.
            child (TreeNode): Nút con.

        Returns:
            bool: True nếu nút là cha, False nếu không.
        """
        return parent and (parent.left == child or parent.right == child)

    def height(self, node):
        """
        Tính chiều cao của cây bắt đầu từ một nút.

        Parameters:
            node (TreeNode): Nút bắt đầu tính chiều cao.

        Returns:
            int: Chiều cao của cây.
        """
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def count_nodes(self, node):
        """
        Tính số nút của cây bắt đầu từ một nút.

        Parameters:
            node (TreeNode): Nút bắt đầu tính số nút.

        Returns:
            int: Số nút của cây.
        """
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def pre_order_traversal(self, node):
        """
        Duyệt cây theo thứ tự tiền tự.

        Parameters:
            node (TreeNode): Nút bắt đầu duyệt.
        """
        if node:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        """
        Duyệt cây theo thứ tự trung tự.

        Parameters:
            node (TreeNode): Nút bắt đầu duyệt.
        """
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        """
        Duyệt cây theo thứ tự hậu tự.

        Parameters:
            node (TreeNode): Nút bắt đầu duyệt.
        """
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")

    def count_leaves(self, node):
        """
        Đếm số nút lá của cây bắt đầu từ một nút.

        Parameters:
            node (TreeNode): Nút bắt đầu đếm.

        Returns:
            int: Số nút lá của cây.
        """
        if node is None:
            return 0
        if self.is_leaf(node):
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def count_intermediates(self, node):
        """
        Đếm số nút trung gian của cây bắt đầu từ một nút.

        Parameters:
            node (TreeNode): Nút bắt đầu đếm.

        Returns:
            int: Số nút trung gian của cây.
        """
        if node is None or self.is_leaf(node):
            return 0
        return (
            1
            + self.count_intermediates(node.left)
            + self.count_intermediates(node.right)
        )

    def max_value(self, node):
        """
        Tìm giá trị lớn nhất trong cây bắt đầu từ một nút.

        Parameters:
            node (TreeNode): Nút bắt đầu tìm giá trị lớn nhất.

        Returns:
            int: Giá trị lớn nhất trong cây.
        """
        if node is None:
            return float("-inf")
        max_left = self.max_value(node.left)
        max_right = self.max_value(node.right)
        return max(node.data, max_left, max_right)

    def min_value(self, node):
        """
        Tìm giá trị nhỏ nhất trong cây bắt đầu từ một nút.

        Parameters:
            node (TreeNode): Nút bắt đầu tìm giá trị nhỏ nhất.

        Returns:
            int: Giá trị nhỏ nhất trong cây.
        """
        if node is None:
            return float("inf")
        min_left = self.min_value(node.left)
        min_right = self.min_value(node.right)
        return min(node.data, min_left, min_right)

    def sum_values(self, node):
        """
        Tính tổng giá trị của các nút trong cây bắt đầu từ một nút.

        Parameters:
            node (TreeNode): Nút bắt đầu tính tổng.

        Returns:
            int: Tổng giá trị của các nút trong cây.
        """
        if node is None:
            return 0
        return node.data + self.sum_values(node.left) + self.sum_values(node.right)

    def average_value(self, node):
        """
        Tính giá trị trung bình của các nút trong cây bắt đầu từ một nút.

        Parameters:
            node (TreeNode): Nút bắt đầu tính giá trị trung bình.

        Returns:
            float: Giá trị trung bình của các nút trong cây.
        """
        count = self.count_nodes(node)
        if count == 0:
            return 0
        return self.sum_values(node) / count

    # Hàm chèn một giá trị vào cây
    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    # Hàm chèn đệ quy
    def _insert_recursive(self, node, data):
        if node.left is None:
            node.left = TreeNode(data)
        elif node.right is None:
            node.right = TreeNode(data)
        else:
            # Lặp lại quá trình chèn từ nút trái đến nút phải
            self._insert_recursive(node.left, data)


# Hàm main
def main():
    tree = BinaryTree()
    nodes = [10, 5, 15, 3, 7, 20]
    # Chèn các giá trị vào cây
    for node in nodes:
        tree.insert(node)

    # In ra cây sau khi chèn
    print("Cây nhị phân sau khi chèn:")
    tree.in_order_traversal(tree.root)

    # Kiểm tra cây rỗng
    print("\n1. Kiểm tra cây rỗng:", tree.is_empty())

    # Kiểm tra nút có phải là nút lá không
    print("2. Kiểm tra nút 3 là nút lá:", tree.is_leaf(tree.root.left.left))

    # Kiểm tra nút có phải là nút cha của nút khác không
    print(
        "3. Kiểm tra nút 5 có phải là cha của nút 3:",
        tree.is_parent_of(tree.root.left, tree.root.left.left),
    )

    # Tính chiều cao của cây
    print("4. Chiều cao của cây:", tree.height(tree.root))

    # Tính số nút của cây
    print("5. Số nút của cây:", tree.count_nodes(tree.root))

    # Duyệt tiền tự, trung tự, hậu tự
    print("6. Duyệt tiền tự:")
    tree.pre_order_traversal(tree.root)
    print("\nDuyệt trung tự:")
    tree.in_order_traversal(tree.root)
    print("\nDuyệt hậu tự:")
    tree.post_order_traversal(tree.root)

    # Đếm số nút lá của cây
    print("\n7. Số nút lá của cây:", tree.count_leaves(tree.root))

    # Đếm số nút trung gian của cây
    print("8. Số nút trung gian của cây:", tree.count_intermediates(tree.root))

    # Nút có giá trị lớn nhất, nhỏ nhất, tổng giá trị các nút, trung bình giá trị các nút
    print("9. Giá trị lớn nhất trong cây:", tree.max_value(tree.root))
    print("   Giá trị nhỏ nhất trong cây:", tree.min_value(tree.root))
    print("   Tổng giá trị các nút trong cây:", tree.sum_values(tree.root))
    print("   Giá trị trung bình của các nút trong cây:",
          tree.average_value(tree.root))


if __name__ == "__main__":
    main()
