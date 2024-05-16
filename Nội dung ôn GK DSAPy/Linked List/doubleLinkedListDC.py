class Nut:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DDSLK:
    def __init__(self):
        self.head = None
        self.tail = None
    # thêm vào đầu danh sách
    def prepend(self, data):
        nut = Nut(data)
        if self.head == None:
            self.head = nut
            self.tail = nut
        else:
            self.head.prev = nut
            nut.next = self.head
            self.head = nut
    # thêm vào cuối danh sách
    def append(self, data):
        nut = Nut(data)
        if self.head == None:
           self.head = nut
           self.tail = nut
        else:
            self.tail.next = nut
            nut.prev = self.tail
            self.tail = nut   
    def duyetDau(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
    def duyetCuoi(self):
        current = self.tail
        while current != None:
            print(current.data)
            current = current.prev
def main():
    ds = DDSLK()
    ds.append(50)
    ds.prepend(30)
    ds.append(60)
    ds.prepend(20)
    ds.prepend(40)
    print("In từ đầu đến cuối: ")
    ds.duyetDau()
    print("In từ cuối đến đầu: ")
    ds.duyetCuoi()
if __name__ == "__main__":
    main()