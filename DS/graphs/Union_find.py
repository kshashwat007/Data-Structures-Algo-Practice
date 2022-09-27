class UnionFind(object):

    def __init__(self, elements=None):
        self.num_elements = 0  # number of elements
        self.num_components = 0  # number of components
        self.id = []   # id of parent
        self.size = []  # size of component
        self.next = 0  # next available id
        self.elem = []  # elements
        self.indx = {}  # dict mapping element -> id in elem[]

        if elements is None:
            elements = []
        for ele in elements:
            self.add(ele)

    def add(self, x):
        if x in self:
            return
        self.elem.append(x)
        self.next += 1
        self.num_elements += 1
        self.num_components += 1
        self.size.append(1)
        self.id.append(self.next)
        self.indx[x] = self.next

    def find(self, x):
        root = x
        while x != self.id[x]:
            root = self.id[root]
        # Path compression
        while x != root:
            q = self.id[x]
            self.id[x] = root
            x = q
        return root

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        if self.connected(x, y):
            return

        root1 = self.find(x)
        root2 = self.find(y)

        if self.size[root1] < self.size[root2]:
            self.id[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.id[root2] = root1
            self.size[root1] += self.size[root2]
        self.num_components -= 1
