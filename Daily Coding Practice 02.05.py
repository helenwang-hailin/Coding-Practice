"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    # Encodes a tree to a single string.
    def helper(node):
        if node is None:
            return "#"
        return f"{node.val},{helper(node.left)},{helper(node.right)}"
    
    return helper(root)

def deserialize(s):
    #Decodes your encoded data to tree.
    def helper(values):
        val = next(values)
        if val == "#":
            return None
        node = Node(val)
        node.left = helper(values)
        node.right = helper(values)
        return node
    
    return helper(iter(s.split(',')))

# Test case
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
