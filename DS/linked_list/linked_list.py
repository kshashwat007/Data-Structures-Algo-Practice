class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.data != prev_node:
            cur_node = cur_node.next
            if cur_node is Node:
                print('Previous node not present')
                return
        new_node.next = cur_node.next
        cur_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            cur_node.next = self.head
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_node_position(self, pos):
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        print(count)

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap(self, key_1, key_2):
        if key_1 == key_2:
            return
        cur_node1 = self.head
        prev1 = None
        while cur_node1 and cur_node1.data != key_1:
            prev1 = cur_node1
            cur_node1 = cur_node1.next
        prev2 = None
        cur_node2 = self.head
        while cur_node2 and cur_node2.data != key_2:
            prev2 = cur_node2
            cur_node2 = cur_node2.next
        if not cur_node1 and cur_node2:
            return
        if prev1:
            prev1.next = cur_node2
        else:
            self.head = cur_node2
        if prev2:
            prev2.next = cur_node1
        else:
            self.head = cur_node1
        cur_node1.next, cur_node2.next = cur_node2.next, cur_node1.next

    # 1 -> 2 -> 3 -> 4
    # 1 <- 2 <- 3 <- 4

    def reverse(self):
        prev, cur = None, self.head
        print("Reversing")
        while cur is not None:
            nextnode = cur.next
            cur.next = prev
            prev = cur
            cur = nextnode
        self.head = prev
        return self.head.data

    def middleNode(self):
        currentNode = self.head
        index = 0
        while currentNode is not None:
            currentNode = currentNode.next
            index += 1
        currentNode = self.head

        if index % 2 != 0:
            position = (index // 2) + 1
            currentPos = 1
            while currentPos < position:
                currentNode = currentNode.next
                currentPos += 1
            return currentNode.data
        else:
            position = (index / 2)
            currentPos = 1
            while currentPos <= position:
                currentNode = currentNode.next
                currentPos += 1
            return currentNode.data

    def middleNode2Pointer(self):
        slow, fast = self.head, self.head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
llist.print_list()
print("Middle node of linked list", llist.middleNode2Pointer())
llist.reverse()
llist.print_list()
