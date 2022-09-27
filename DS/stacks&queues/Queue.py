class Queue:
    def __init__(self, size):
        self.q = [None] * size
        self.capacity = size
        self.front = -1
        self.rear = -1
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity

    def append(self, value):
        if self.isFull():
            print("Queue overflow!")
            exit(1)
        print("Inserting element ", value)
        if self.count == 0:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    def pop(self):
        if self.isEmpty():
            print("Queue underflow!")
            exit(1)
        print("Removing element ", self.q[self.front])
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1

    def peek(self):
        if self.isEmpty():
            print("Queue underflow!")
            exit(1)
        return self.q[self.front]


q = Queue(5)
q.append(6)
q.append(7)
q.append(12)
print("The queue size is ", q.size())
print("The front element is ", q.peek())
q.pop()
print("The front element is ", q.peek())
q.pop()
print("The front element is ", q.peek())
if q.isEmpty():
    print("Queue is empty")
else:
    print("Queue is not empty")
