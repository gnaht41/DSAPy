class Idvalue:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def info(self):
        return f"Id: {self.id}, Value: {self.value}"


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

    # Them
    def addtail(self, new_date):
        current = IdValueNode(new_date)
        if self.head == None:
            self.head = current
            self.tail = current
        else:
            self.tail.next = current
            self.tail = current

    def checkResulf(self):
        current = self.head
        kq = "----- Display DS ------" + "\n"
        while current != None:
            kq += current.data.info() + "\n"
            current = current.next
        print(kq)

    def isEmpty(self):
        return self.head is not None

    def isDuplicate(self, id):
        current = self.head
        while current != None and current.data.id != id:
            current = current.next
        if current != None and current.data.id == id:
            return True
        return False


def main():
    ds = IdValueSLL()
    ds.addtail(Idvalue("aa", 1))
    ds.addtail(Idvalue("bb", 2))
    ds.addtail(Idvalue("cc", 3))
    ds.checkResulf()
    print("Have the date? (true/ false): ", ds.isEmpty())
    print()
    a = "aaa"
    kq = ds.isDuplicate(a)
    print(f"{a} have in data/ (true/ false): ", kq)


if __name__ == "__main__":
    main()
