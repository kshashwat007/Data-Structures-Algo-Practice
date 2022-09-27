class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

# Inorder Tree traversal


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)


def inOrderUsingStacks(root):
    current = root
    stack = []
    done = 0
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.data)
            current = current.right
        else:
            break
    print()

# PreOrder Tree traversal


def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)

# PostOrder Tree traversal


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)


def printLevelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while(len(queue) > 0):
        print(queue[0].data)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def reverseLevelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    s = []
    while queue:
        node = queue.pop(0)
        print(node.data)
        if node is None:
            continue
        s.append(node.data)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return s[::-1]


def isComplete(root):
    if root is None:
        return True
    queue = []
    # Create a flag variable which will be set True
    # when a non-full node is seen
    flag = False
    queue.append(root)
    while(len(queue) > 0):
        nodetemp = queue.pop(0)
        if nodetemp.left is not None:
            if flag is True:
                return False
            queue.append(nodetemp.left)
        else:
            flag = True
        if nodetemp.right is not None:
            if flag is True:
                return False
            queue.append(nodetemp.right)
        else:
            flag = True
    return True


def height(root):
    if root is None:
        return 0
    queue = []
    queue.append(root)
    height = 0
    while(len(queue) > 0):
        size = len(queue)
        while (size > 0):
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            size -= 1
        height += 1
    return height


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal is")
printLevelOrder(root)
# print("Reverse Level order traversal is")
# print(reverseLevelOrder(root))
print("The tree is a complete tree:-", isComplete(root))
print("The height of the tree is:-", height(root))
# print("Inorder Traversal is")
# inOrderUsingStacks(root)
# print("Preorder Traversal is")
# preOrder(root)
# print("Postorder Traversal is")
# postOrder(root)
