class IdValue:
    def __init__(self, id, value):
        self.id = id
        self.value = value

class IdValueNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class IdValueSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def isDuplicated(self, id):
        current = self.head
        while current:
            if current.data.id == id:
                return True
            current = current.next
        return False

    def addTail(self, newdata):
        newNode = IdValueNode(newdata)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

# Example usage:
if __name__ == "__main__":
    sll = IdValueSLL()
    
    print("Danh sách liên kết đơn có trống không?", sll.isEmpty())  # Nên in True
    
    sll.addTail(IdValue("1", 10))
    sll.addTail(IdValue("2", 20))
    sll.addTail(IdValue("3", 30))
    
    print("Danh sách liên kết đơn có trống không?", sll.isEmpty())  # Nên in False
    print("Id '2' có bị trùng không?", sll.isDuplicated("2"))  # Nên in False
    print("Id '3' có bị trùng không?", sll.isDuplicated("3"))  # Nên in True