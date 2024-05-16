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
        new_node = IdValueNode(newdata)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
