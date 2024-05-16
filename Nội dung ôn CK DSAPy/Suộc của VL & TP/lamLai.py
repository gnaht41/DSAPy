class Nut:
    def __init__(self, data):
        if data is not None:
            self.node = data  # Giá trị của nút
            self.trai = None  # Nút con bên trái
            self.phai = None  # Nút con bên phải

    def insert(self, data):
        if (
            self is None
        ):  # Nếu nút hiện tại là None, trả về một nút mới chứa giá trị data
            return Nut(data)
        elif (
            data < self.node
        ):  # Nếu data nhỏ hơn giá trị của nút hiện tại, thêm vào cây con bên trái
            if self.trai == None:
                self.trai = Nut(data)  # Tạo một nút mới nếu không có nút con bên trái
            else:
                self.trai.insert(
                    data
                )  # Nếu có nút con bên trái, thêm data vào cây con bên trái
        elif (
            data > self.node
        ):  # Nếu data lớn hơn giá trị của nút hiện tại, thêm vào cây con bên phải
            if self.phai == None:
                self.phai = Nut(data)  # Tạo một nút mới nếu không có nút con bên phải
            else:
                self.phai.insert(
                    data
                )  # Nếu có nút con bên phải, thêm data vào cây con bên phải
        else:
            raise ValueError(
                "Duplication!"
            )  # Nếu data đã tồn tại trong cây, ném ra một ngoại lệ


class Tree:
    def __init__(self, data):
        if data is not None:
            self.goc = Nut(data)  # Tạo cây với nút gốc chứa giá trị data
        else:
            self.goc = None

    def _insert(self, data):
        if self.goc is None:
            self.goc = Nut(data)  # Tạo một nút mới nếu cây đang rỗng
        else:
            self.goc.insert(data)  # Thêm giá trị vào cây

    def NLR(self):
        self._NLR(self.goc)  # Duyệt cây theo thứ tự trước (NLR)

    def _NLR(self, nut):
        if nut:
            print(nut.node, end=" ")  # In giá trị của nút
            self._NLR(nut.trai)  # Duyệt cây con bên trái
            self._NLR(nut.phai)  # Duyệt cây con bên phải

    def find(self, data):
        return self._find(self.goc, data)  # Tìm giá trị trong cây

    def _find(self, nut, data):
        if (
            nut is None or nut.node == data
        ):  # Nếu nút là None hoặc giá trị của nút bằng data, trả về nút
            return nut
        if (
            data < nut.node
        ):  # Nếu data nhỏ hơn giá trị của nút, tìm trong cây con bên trái
            return self._find(nut.trai, data)
        return self._find(nut.phai, data)  # Ngược lại, tìm trong cây con bên phải

    def delete(self, data):
        self.goc = self._delete(self.goc, data)  # Xóa giá trị từ cây

    def _delete(self, nut, data):
        if nut is None:
            return nut

        if data < nut.node:
            nut.trai = self._delete(nut.trai, data)  # Xóa giá trị từ cây con bên trái
        elif data > nut.node:
            nut.phai = self._delete(nut.phai, data)  # Xóa giá trị từ cây con bên phải
        else:
            if nut.trai is None:
                return nut.phai
            elif nut.phai is None:
                return nut.trai

            temp = self._minValueNode(
                nut.phai
            )  # Tìm nút có giá trị nhỏ nhất trong cây con bên phải
            nut.node = temp.node  # Gán giá trị của nút nhỏ nhất vào nút hiện tại
            nut.phai = self._delete(
                nut.phai, temp.node
            )  # Xóa nút nhỏ nhất từ cây con bên phải
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
        tree._insert(int(i))  # Thêm các giá trị từ file vào cây
    tree.NLR()  # In cây theo thứ tự trước
    if tree.find(8) is None:  # Tìm giá trị 8 trong cây
        print("\nKhong tim thay")
    else:
        print("\nTim thay")
    tree.delete(8)  # Xóa giá trị 8 từ cây
    tree.NLR()  # In cây sau khi xóa giá trị 8


if __name__ == "__main__":
    main()
