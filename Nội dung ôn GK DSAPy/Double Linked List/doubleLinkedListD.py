class Nut:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DDSLK:
    def __init__(self):
        self.head = None
    def append(self, data):
        nut = Nut(data)
        if self.head == None:
            self.head = nut
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = nut
            nut.prev = cur
    def prepend(self, data):
        nut = Nut(data)
        if self.head == None:
            self.head = nut
        else:
            nut.next = self.head
            self.head.prev = nut
            self.head = nut
    def duyetDau(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next
    
    def duyetCuoi(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        while cur:
            print(cur.data)
            cur = cur.prev
            
def main():
    ds = DDSLK()
    ds.prepend(20)
    ds.append(30)
    ds.prepend(10)
    ds.append(50)
    print("In từ đầu đến cuối: ")
    ds.duyetDau()
    print("In từ cuối đến đầu: ")
    ds.duyetCuoi()
if __name__ == "__main__":
    main()
        
            
            
        