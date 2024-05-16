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

# Create some IdValue objects
id_value1 = IdValue("id1", 10)
id_value2 = IdValue("id2", 20)

# Create a single linked list object
sll = IdValueSLL()

# Add nodes to the list
sll.addTail(id_value1)
sll.addTail(id_value2)

# Check if the list is empty
print("Is list empty?", sll.isEmpty())

# Check if a specific id is duplicated
print("Is 'id1' duplicated?", sll.isDuplicated("id1"))
print("Is 'id3' duplicated?", sll.isDuplicated("id3"))


