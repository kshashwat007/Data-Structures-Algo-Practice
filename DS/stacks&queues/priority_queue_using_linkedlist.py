class PriorityQueueNode:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def isEmpty(self):
        return True if self.front is None else False

    def push(self, value, priority):
        if self.isEmpty():
            self.front = PriorityQueueNode(value, priority)
            return 1
        else:
            # Special condition check to see that
            # first node priority value
            if self.front.priority < priority:
                newNode = PriorityQueueNode(value, priority)
                newNode.next = self.front
                self.front = newNode
                return 1
            else:
                # Traversing through Queue until it
                # finds the next bigger priority node
                temp = self.front
                while temp.next:
                    # If same priority node found then current
                    # node will come after previous node
                    if priority >= self.front.priority:
                        break
                    temp = temp.next
                newNode = PriorityQueueNode(value, priority)
                newNode.next = temp.next
                temp.next = newNode
                return 1

    def pop(self):
        if self.isEmpty():
            return
        else:
            print("Popping element..")
            self.front = self.front.next
            return 1

    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.front.data

    def traverse(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            temp = self.front
            while temp:
                print(temp.data)
                temp = temp.next


pq = PriorityQueue()
pq.push(5, 3)
pq.push(7, 2)
pq.push(10, 4)
pq.push(8, 7)
pq.push(9, 5)
pq.traverse()
pq.pop()
pq.traverse()
