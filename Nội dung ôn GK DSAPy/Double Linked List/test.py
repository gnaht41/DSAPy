class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def traverse_forward(self):
        cur = self.head
        while cur:
            print(cur.data, end=" <-> ")
            cur = cur.next
        print("None")

    def traverse_backward(self):
        cur = self.head
        if cur is None:
            return
        while cur.next:
            cur = cur.next
        while cur:
            print(cur.data, end=" <-> ")
            cur = cur.prev
        print("None")

def main():
    dll = DoubleLinkedList()
    dll.append(50)
    dll.prepend(20)
    dll.prepend(30)
    dll.prepend(40)
    print("In từ đầu đến cuối: ")
    dll.traverse_forward()
    print("In từ cuối đến đầu: ")
    dll.traverse_backward()

if __name__ == "__main__":
    main()
