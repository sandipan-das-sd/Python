class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add the data in the left subtree
            if self.left:
                # you are not a leaf node
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        # visit left subtree
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        # visit base node
        elements.append(self.data)
        # visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [5,8,1,6,10,2,3,58,9,7,12]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())


#Method 2
'''
# Python program for preorder traversals

# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

# Function to print preorder traversal
def printPreorder(node):
    if node is None:
        return

    # Deal with the node
    print(node.data, end=' ')

    # Recur on left subtree
    printPreorder(node.left)

    # Recur on right subtree
    printPreorder(node.right)


# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Function call
    print("Preorder traversal of binary tree is:")
    printPreorder(root)



'''