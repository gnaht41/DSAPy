# IdValue class
class IdValue:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def __str__(self):
        return f"id: {self.id}, value: {self.value}"


# IdValueNode class
class IdValueNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"data: {self.data}, next: {self.next}"


# IdValueSLL class
class IdValueSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def isDuplicated(self, id):
        current_node = self.head
        while current_node is not None:
            if current_node.data.id == id:
                return True
            current_node = current_node.next
        return False

    def addTail(self, newdata):
        new_node = IdValueNode(newdata)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def checkResult(self):
        result = ""
        current_node = self.head
        while current_node is not None:
            result += str(current_node.data) + " "
            current_node = current_node.next
        return result


# Testing
sll = IdValueSLL()
sll.addTail(IdValue("A", 1))
sll.addTail(IdValue("B", 2))
sll.addTail(IdValue("C", 3))

print(sll.checkResult())  # Output: id: A, value: 1 id: B, value: 2 id: C, value: 3

print(sll.isEmpty())  # Output: False

print(sll.isDuplicated("A"))  # Output: True

print(sll.isDuplicated("D"))  # Output: False
