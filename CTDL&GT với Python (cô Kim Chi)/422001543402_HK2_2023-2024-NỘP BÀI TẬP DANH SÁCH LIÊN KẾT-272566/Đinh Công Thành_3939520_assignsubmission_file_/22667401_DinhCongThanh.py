class IdValue:
    def __init__(self, id, value):
        self.id = id
        self.value = value

class IdValueNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class IdValueSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def isDuplicated(self, id):
        hientai = self.head
        while hientai:
            if hientai.data.id == id:
                return True
            hientai = hientai.next
        return False

    def addTail(self, newdata):
        newnode = IdValueNode(newdata, None)
        if self.isEmpty():
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
