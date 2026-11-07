"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        result = []

        def traverse(node):
            if node is None:
                return

            result.append(node.val)  # Root

            for child in node.children:
                traverse(child)      # Children

        traverse(root)
        return result