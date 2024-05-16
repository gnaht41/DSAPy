class Nut:
    def __init__(self, data):
        self.data = data
        self.nutKeTiep = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def enqueue(self, newdata):
        nut = Nut(newdata)
        if self.isEmpty():
            self.front = nut
            self.rear = nut
        else:
            self.rear.nutKeTiep = nut
            self.rear = nut
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            remove = self.front.data
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front = self.front.nutKeTiep
            return remove
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.front.data
    def display(self):
        cur = self.front
        while cur != None:
            print(cur.data, end = ' ')
            cur = cur.nutKeTiep
        print()

def main():
    q = Queue()
    q.enqueue(7)
    q.enqueue(2)
    q.enqueue(10)
    print("Queue sau khi enqueue:")
    q.display()
    print("Phần tử được dequeue:", q.dequeue())
    print("Queue sau khi dequeue:")
    q.display() 
    print("Phần tử đầu tiên trong queue:", q.peek()) 
if __name__ == "__main__":
    main()
            