class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        # counter to indicate how many times a word is inserted
        self.counter = 0
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        node.counter += 1

    def dfs(self, node, prefix):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            return self.output.append((prefix + node.char, node.counter))
        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of 
        times they have been inserted
        """
        self.output = []
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        # Traversing the trie to get all the outcomes
        self.dfs(node, x[:-1])
        print(sorted(self.output, key=lambda x: x[1], reverse=True))


t = Trie()
t.insert("was")
t.insert("where")
t.insert("war")
t.insert("wax")
t.insert("what")
t.query("wh")
