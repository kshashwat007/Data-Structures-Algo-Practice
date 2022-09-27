class MinHeap:
    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            for i in range(len(self.heap)):
                self._siftdown(i)

    def _siftup(self, i):
        parent = (i-1)//2
        while i != 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i-1)//2

    def _siftdown(self, i):
        left = 2*i + 1
        right = 2*i + 2
        while (left < len(self.heap) and self.heap[i] > self.heap[left]) or (right < len(self.heap) and self.heap[i] > self.heap[right]):
            smallest = left if (right >= len(self.heap) or self.heap[i] < self.heap[right]) else right
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            left = 2*i + 1
            right = 2*i + 2

    def insert(self, value):
        self.heap.append(value)
        self._siftup(len(self.heap)-1)

    def get_min(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return min_val

    def update_by_index(self, i, new):
        old_val = self.heap[i]
        self.heap[i] = new
        if old_val < new:
            self._siftdown(i)
        else:
            self._siftup(i)

    def update(self, old, new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)


class MaxHeap:
    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            for i in range(len(self.heap)):
                self._siftdown(i)

    def _siftup(self, i):
        parent = (i-1)//2
        while i != 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            parent = (i-1)//2

    def _siftdown(self, i):
        left = 2*i + 1
        right = 2*i + 2
        while (left < len(self.heap) and self.heap[i] < self.heap[left]) or (right < len(self.heap) and self.heap[i] < self.heap[right]):
            bigger = left if (right >= len(self.heap) or self.heap[i] > self.heap[right]) else right
            self.heap[i], self.heap[bigger] = self.heap[bigger], self.heap[i]
            i = bigger
            left = 2*i + 1
            right = 2*i + 2

    def insert(self, value):
        self.heap.append(value)
        self._siftup(len(self.heap)-1)

    def get_max(self):
        return self.heap[0] if len(self.heap) > 0 else None

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        max_val = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return max_val

    def update_by_index(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if old < new:
            self._siftup(i)
        else:
            self._siftdown(i)

    def update(self, new, old):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)


def heapsort(arr):
    heap = MinHeap(arr)
    return [heap.extract_min() for i in range(len(heap.heap))]
