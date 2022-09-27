import sys


class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already present in the tree")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_tree = self._height(cur_node.left_child, cur_height + 1)
        right_tree = self._height(cur_node.right_child, cur_height + 1)
        return max(left_tree, right_tree)

    # returns node with the value
    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        # returns the node with the min value in the tree
        def min_value_node(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        # returns number of children for a node
        def num_children(n):
            num_children = 0
            if n.left_child is not None:
                num_children += 1
            if n.right_child is not None:
                num_children += 1
            return num_children

        node_parent = node.parent

        node_children = num_children(node)

        # CASE 1 (node has no children)
        if node_children == 0:

            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        # CASE 2 (node has 1 child)
        if node_children == 1:
            # getting the child of the node to be deleted
            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            # replacing the node to be deleted with the child node
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child

            child.parent = node_parent

        # CASE 3 (node has 2 children)
        if node_children == 2:
            # get the inorder successor
            successor = min_value_node(node.right_child)

            node.value = successor.value

            # delete the inorder successor's value now that its value is copied on the other node
            self.delete_node(successor)

    # Validate if the tree is bst or not
    def validate_bst(self):
        return self._validate_bst(self.root)

    def _validate_bst(self, root, min=-sys.maxsize, max=sys.maxsize):
        if root is None:
            return True
        if root.value < min or root.value >= max:
            return False
        lefttree = self._validate_bst(root.left_child, min, root.value)
        righttree = self._validate_bst(root.right_child, root.value, max)
        return lefttree and righttree

    def is_perfect(self):
        def calculateDepth(node):
            d = 0
            while node.left_child is not None:
                d += 1
                node = node.left_child
            return d
        if self.root is not None:
            return self._is_perfect(self.root, calculateDepth(self.root))
        else:
            return False

    def _is_perfect(self, root, d, level=0):
        if root is None:
            return True
        if root.left_child is None and root.right_child is None:
            return d == level
        if root.left_child is None or root.right_child is None:
            return False
        return self._is_perfect(root.left_child, d, level + 1) and self._is_perfect(root.right_child, d, level + 1)


tree = binary_search_tree()
tree.insert(5)
tree.insert(10)
tree.insert(1)
tree.print_tree()
print("Height of the tree is", tree.height())

if tree.is_perfect():
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")
print("valid bst", tree.validate_bst())
# tree.delete_value(25)
# tree.print_tree()
