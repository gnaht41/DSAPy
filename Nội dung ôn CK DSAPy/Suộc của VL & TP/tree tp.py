class Student:
    def __init__(self, studentID, fullName, classID, avgMark):
        self.studentID = studentID
        self.fullName = fullName
        self.classID = classID
        self.avgMark = avgMark
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_a(self, node, studentID, fullName, classID, avgMark):
        if node.studentID < studentID:
            if node.right == None:
                node.right = Student(studentID, fullName, classID, avgMark)
            else:
                self.insert_a(node.right,  studentID,
                              fullName, classID, avgMark)
        elif studentID < node.studentID:
            if node.left == None:
                node.left = Student(studentID, fullName, classID, avgMark)
            else:
                self.insert_a(node.left, studentID, fullName, classID, avgMark)

    def insert(self,  studentID, fullName, classID, avgMark):
        if self.root == None:
            self.root = Student(studentID, fullName, classID, avgMark)
        else:
            self.insert_a(self.root,  studentID, fullName, classID, avgMark)
    # Add student

    def addStudent(self):
        studentID = int(input('Enter studentID: '))
        fullName = input('Enter fullName: ')
        classID = input('Enter classID: ')
        avgMark = float(input('Enter avgMark: '))
        self.insert(studentID, fullName, classID, avgMark)
    # Display

    def LNR(self, node):
        if node:
            self.LNR(node.left)
            print('StudentID: ', node.studentID, ' ---- FullName: ', node.fullName,
                  ' ----ClassID: ', node.classID, ' ---- AvgMark: ', node.avgMark)
            self.LNR(node.right)

    def inOrderPrinT(self):
        self.LNR(self.root)
    # Count node

    def count_nodes_a(self, node):
        if node == None:
            return 0
        return 1 + self.count_nodes_a(node.left) + self.count_nodes_a(node.right)

    def count_nodes(self):
        return self.count_nodes_a(self.root)
    # Find

    def find_a(self, node, studentID):
        if node is None:
            return None
        elif node.studentID == studentID:
            return node
        elif node.studentID < studentID:
            return self.find_a(node.right, studentID)
        elif node.studentID > studentID:
            return self.find_a(node.left, studentID)

    def find(self, studentID):
        node = self.find_a(self.root, studentID)
        return node
    # Delete

    def min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete_a(self, node, studentID):
        if node == None:
            return node
        elif node.studentID < studentID:
            node.right = self.delete_a(node.right, studentID)
        elif node.studentID > studentID:
            node.left = self.delete_a(node.left, studentID)
        else:
            if node.right == None:
                return node.left
            elif node.left == None:
                return node.right
            else:
                temp = min(node.right)
                node.studentID = temp.studentID
                node.right = self.delete_a(node.right, temp.studentID)
        return node

    def delete(self, studentID):
        self.root = self.delete_a(self.root, studentID)
    # Is empty

    def isEmpty(self):
        return self.root is not None
    # Nodes is leaf

    def isLeaf(self, node):
        return node.left is None and node.right is None
    # Node_n is father of Node_m

    def is_parent(self, node_n, node_m):
        if node_n is None and node_m is None:
            return False
        elif node_n.left == node_m or node_n.right == node_m:
            return True
        return self.is_parent(node_n.right, node_m) or self.is_parent(node_n.left, node_m)
    # Count leaf

    def count_leaf_a(self, node):
        if node == None:
            return 0
        if self.isLeaf(node):
            return 1
        return self.count_leaf_a(node.right) + self.count_leaf_a(node.left)

    def count_leaf(self):
        return self.count_leaf_a(self.root)
    # Sum Mark

    def sum_Mark_a(self, node):
        if node == None:
            return 0
        return node.avgMark + self.sum_Mark_a(node.left) + self.sum_Mark_a(node.right)

    def sum_Mark(self):
        return self.sum_Mark_a(self.root)
    # Sum Avg Mark

    def sumAvgMark(self):
        total_mark = self.sum_Mark()
        total_student = self.count_nodes()
        if total_student == None:
            return 0
        return total_mark / total_student
    # Print Mark > 7

    def print_7_a(self, node):
        if node:
            self.print_7_a(node.left)
            if node.avgMark > 7:
                print('StudentID: ', node.studentID, ' ---- FullName: ', node.fullName,
                      ' ----ClassID: ', node.classID, ' ---- AvgMark: ', node.avgMark)
            self.print_7_a(node.right)

    def print_7(self):
        self.print_7_a(self.root)


def main():
    root = BinarySearchTree()
    lc = 0
    while True:
        print('''
        ----------------------Menu------------------          
        0. Exit
        1. Add
        2. Display
        3. Count node
        4. Find
        5. Delete
        6. Is empty
        7. Is leaf
        8. Check parent
        9. Count leaf
        10. Sum Mark
        11. Sum avgMark
        12. Mark > 7''')
        lc = int(input('Enter choose: '))
        print('')
        if lc == 0:
            break
        elif lc == 1:
            n = int(input('Enter quantity Student: '))
            for i in range(n):
                print(f'------Student {i+1}')
                root.addStudent()
                print()
        elif lc == 2:
            root.inOrderPrinT()
        elif lc == 3:
            print('Count nodes: ', root.count_nodes())
        elif lc == 4:
            studentID = int(input('Nhập mã sinh viên cần tìm: '))
            found_node = root.find(studentID)
            if found_node is not None:
                print('StudentID: ', found_node.studentID, ' ---- FullName: ', found_node.fullName,
                      ' ----ClassID: ', found_node.classID, ' ---- AvgMark: ', found_node.avgMark)
            else:
                print('Không tìm thấy sinh viên có mã', studentID)
        elif lc == 5:
            n = int(input('Enter studentID delete: '))
            root.delete(n)
            print('-------List After Delete ------')
            root.inOrderPrinT()
        elif lc == 6:
            a = root.isEmpty()
            if a:
                print('Yes data')
            else:
                print('No data')
        elif lc == 7:
            studentID = int(input('Enter studentID: '))
            found_node = root.find(studentID)
            if found_node is not None:
                if root.isLeaf(found_node):
                    print(f'StudentID {studentID} is a leaf node')
                else:
                    print(f'StudentID {studentID} is not a leaf node')
            else:
                print('No see data', studentID)
        elif lc == 8:
            a = int(input('Enter studentID nodes_n: '))
            nodes_n = root.find(a)
            b = int(input('Enter studentID nodes_m: '))
            nodes_m = root.find(b)
            kq = root.is_parent(nodes_n, nodes_m)
            if kq == True:
                print(f'{nodes_n.studentID} is a parent of {
                      nodes_m.studentID}')
            else:
                print('No parent')
        elif lc == 9:
            print(f'Quantity leaf in tree: ', root.count_leaf())
        elif lc == 10:
            print('Sum mark: ', root.sum_Mark_a())
        elif lc == 11:
            print('Sum avg mark: ', root.sumAvgMark())
        elif lc == 12:
            root.print_7()


main()
