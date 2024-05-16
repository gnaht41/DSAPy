class Nut:
    def __init__(self, data):
        if data is not None:
            self.node = data
            self.trai = None
            self.phai = None

    def insert(self, data):
        if self is None:
            return Nut(data)
        elif data < self.node:
            if self.trai == None:
                self.trai = Nut(data)
            else:
                self.trai.insert(data)
        elif data > self.node:
            if self.phai == None:
                self.phai = Nut(data)
            else:
                self.phai.insert(data)
        else:
            raise ValueError("Duplication!")


class Tree:
    def __init__(self, data):
        if data is not None:
            self.goc = Nut(data)
        else:
            self.goc = None

    def _insert(self, data):
        if self.goc is None:
            self.goc = Nut(data)
        else:
            self.goc.insert(data)

    def NLR(self):
        self._NLR(self.goc)

    def _NLR(self, nut):
        if nut:
            print(nut.node, end=" ")
            self._NLR(nut.trai)
            self._NLR(nut.phai)

    def find(self, data):
        return self._find(self.goc, data)

    def _find(self, nut, data):
        if nut is None or nut.node == data:
            return nut
        if data < nut.node:
            return self._find(nut.trai, data)
        return self._find(nut.phai, data)

    def delete(self, data):
        self.goc = self._delete(self.goc, data)

    def _delete(self, nut, data):
        if nut is None:
            return nut

        if data < nut.node:
            nut.trai = self._delete(nut.trai, data)
        elif data > nut.node:
            nut.phai = self._delete(nut.phai, data)
        else:
            if nut.trai is None:
                return nut.phai
            elif nut.phai is None:
                return nut.trai

            temp = self._minValueNode(nut.phai)
            nut.node = temp.node
            nut.phai = self._delete(nut.phai, temp.node)
        return nut

    def _minValueNode(self, nut):
        current = nut
        while current.trai is not None:
            current = current.trai
        return current


def main():
    tree = Tree(10)
    f = open("data.txt", "r")
    for i in f.read().strip().split():
        tree._insert(int(i))
    tree.NLR()
    if tree.find(8) == None:
        print("\nKhong tim thay")
    else:
        print("\nTim thay")
    tree.delete(8)
    tree.NLR()


if __name__ == "__main__":
    main()
