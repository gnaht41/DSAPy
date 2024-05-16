class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    # Thêm
    def insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert(node.right, data)
    
    def _insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert(self.root, data)
    # Duyệt
    def LNR(self, node):
        if node:
            self.LNR(node.left)
            print(f'{node.data}', end = ' ')
            self.LNR(node.right)
    
    def _LND(self):
        self.LNR(self.root)

    # Đếm số lượng số nguyên tố
    def is_prime(self, node):
        if node < 2:
            return False
        for i in range(2, int(node**0.5) + 1):
            if node % i == 0:
                return False
        return True
                
    def SNT(self, node):
        if node is None:
            return 0
        dem = 0
        if self.is_prime(node.data):
            dem = 1
        return dem + self.SNT(node.left) + self.SNT(node.right)

    def _SNT(self):
        return self.SNT(self.root)
    
    # Tính tổng giá trị các node chẵn của cây
    def sumNutChan(self, node):
        if node is None:
            return 0
        sum = 0
        if node.data % 2 == 0:
            sum += node.data
        return sum + self.sumNutChan(node.left) + self.sumNutChan(node.right)
    
    def _sumNutChan(self):
        return self.sumNutChan(self.root)
    
    # Tìm node nhỏ nhất của cây
    def minNode(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current
    
    # Đếm số node lẻ của cây
    def demNutLe(self, node):
        if node is None:
            return 0
        dem = 0
        if node.data % 2 != 0:
            dem = 1
        return dem + self.demNutLe(node.left) + self.demNutLe(node.right)
    
    def _demNutLe(self):
        return self.demNutLe(self.root)
    
    # Tìm node 
    def tim(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.tim(node.left, data)
        elif data > node.data:
            return self.tim(node.right, data)
                
    def _tim(self, data):
        return self.tim(self.root, data)
    
   # Xóa node
    def xoa(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self.xoa(node.left, data)
        elif data > node.data:
            node.right = self.xoa(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                tam = self.minNodeXoa(node.right)
                node.data = tam.data
                node.right = self.xoa(node.right, tam.data)
        return node
    
   
    def _xoa(self, data):
        self.root = self.xoa(self.root, data)

    def minNodeXoa(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
        
def main():
    root = Tree()
    ds = [20, 15, 30, 13, 17, 25, 51]
    while True:
        print('\n----------MENU----------\n')
        print('1. Thêm phần tử vào cây')
        print('2. Duyệt cây theo LNR')
        print('3. Đếm số lượng node là số nguyên tố của cây?')
        print('4. Tính tổng giá trị các node chẵn của cây?')
        print('5. Tìm node nhỏ nhất của cây?')
        print('6. Đếm số node lẻ của cây?')
        print('7. Tìm node có giá trị do người dùng nhập')
        print('8. Xoá một node có giá trị do người dùng nhập\n')
        lc = int(input('Nhập lựa chọn của bạn: '))
        if lc == 1:
            for i in ds:
                root._insert(int(i))
        elif lc == 2:
            root._LND()
        elif lc == 3:
            print('Số lượng số nguyên tố của cây là:', root._SNT())
        elif lc == 4:
            print('Tổng giá trị các node là: ', root._sumNutChan())
        elif lc == 5:
            a = root.minNode()
            print('Tìm node nhỏ nhất của cây: ', a.data)
        elif lc == 6:
            print('Đếm số node lẻ trong cây: ', root._demNutLe())
        elif lc == 7:
            print('Tìm node')
            n = int(input('\nNhập node cần tìm: '))
            if root._tim(n) is not None:
                print(f'Đã tìm thấy node: {n}')
            else:
                print(f'Không tìm thấy node: {n}')
        elif lc == 8:
            print('Xóa node')
            n1 = int(input('\nNhập node cần xóa: '))
            root._xoa(n1)
            
if __name__ == '__main__':
    main()
