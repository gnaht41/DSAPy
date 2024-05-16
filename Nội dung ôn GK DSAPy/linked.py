class IdValue:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def info(self):
        return f"Id: {self.id}, value: {self.value}"


class IdValueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def info(self):
        return self.data.info()


class IdValueSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addTail(self, newdata):
        currently = IdValueNode(newdata)
        if self.head == None:
            self.head = currently
            self.tail = currently
        else:
            self.tail.next = currently
            self.tail = currently

    def checkResult(self):
        currently = self.head
        while currently != None:
            kt = str(currently.data.info()) + "\n"
            print(kt)
            currently = currently.next

    def isEmpty(self):
        if self.head == None:
            return False
        return True

    def isDuplicated(self, id):
        currently = self.head
        while currently != None and currently.data.id != id:
            currently = currently.next
        if currently != None:
            return True
        return False

    def sapXep(self):
        current = self.head

        while current != None:
            if current.data.id > current.data.next.id:
                current, current.next, current
            current = current.next


def main():
    ds = IdValueSLL()
    ds.addTail(IdValue("a", 1))
    ds.addTail(IdValue("b", 2))
    ds.addTail(IdValue("c", 2))
    ds.checkResult()
    print(ds.isEmpty())
    print(ds.isDuplicated("b"))
    ds.checkResult()
    ds.sapXep()
    ds.checkResult()


if __name__ == "__main__":
    main()
