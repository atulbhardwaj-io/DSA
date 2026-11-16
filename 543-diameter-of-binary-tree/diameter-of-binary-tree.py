# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.diameter = 0

    def height(self, root):

        if root is None:
            return 0

        lh = self.height(root.left)
        rh = self.height(root.right)

        self.diameter = max(self.diameter, lh + rh)

        return 1 + max(lh, rh)

    def diameterOfBinaryTree(self, root):

        self.diameter = 0
        self.height(root)

        return self.diameter
        