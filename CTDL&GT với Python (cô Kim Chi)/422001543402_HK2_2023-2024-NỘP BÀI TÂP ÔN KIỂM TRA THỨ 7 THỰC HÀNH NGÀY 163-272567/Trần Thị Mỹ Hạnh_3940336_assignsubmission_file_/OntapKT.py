class IdValue:
    def __innit__(self,id, value):
        self.id = id
        self.value = value
    
class IdValueNode:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node
        
class IdValueSLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head is None
    
    def isDuplicate(self, id):
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
            
# Su dung
sll = IdValueSLL()
print('Kiem tra xem DSLK co rong khong: ')
print(sll.isEmpty())  # True

sll.addTail(IdValue("1", 10))
sll.addTail(IdValue("2", 20))
sll.addTail(IdValue("3", 30))
print('Kiem tra xem DSLK co rong khong: ')
print(sll.isEmpty())  # False
print('Kiem tra trung lap: ')
print(sll.isDuplicate("2"))  # False
print(sll.isDuplicate("3"))  # True
