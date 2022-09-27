class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        ptr = Node(data)
        temp = self.head
        ptr.next = temp

        if self.head is not None:
            while temp.next is not self.head:
                temp = temp.next
            temp.next = ptr
        else:
            ptr.next = ptr
        self.head = ptr

    def printlist(self):
        temp = self.head
        if self.head is not None:
            while temp.next:
                print(temp.data)
                temp = temp.next
                if temp is self.head:
                    break

    def deleteNode(self, key):
        if self.head is None:
            return
        if self.head is key and self.head.next is None:
            self.head = None

        last = self.head
        d = key
        if self.head is key:
            while last.next:
                last = last.next
            last.next = self.head.next
            self.head = last.next
        while last.next is not self.head and last.next.data is not key:
            last = last.next
        if last.next.data is key:
            d = last.next
            last.next = d.next
        else:
            print("Value not found")
        return self.head

    def exchangeNodes(self):
        if self.head is None and self.head.next is self.head:
            return self.head
        elif self.head.next.next is self.head:
            self.head = self.head.next
            return self.head
        else:
            prev = None
            cur = self.head
            temp = self.head
            while cur.next is not self.head:
                prev = cur
                cur = cur.next
            cur.next = temp.next
            prev.next = temp
            temp.next = cur
            self.head = cur
            return self.head


cclist = CircularLinkedList()
cclist.push(5)
cclist.push(7)
cclist.push(9)
cclist.printlist()
cclist.exchangeNodes()
cclist.printlist()
