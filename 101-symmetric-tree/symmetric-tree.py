# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):

        def check(left, right):

            # Both nodes are None
            if left is None and right is None:
                return True

            # Only one node is None
            if left is None or right is None:
                return False

            # Values must be equal
            if left.val != right.val:
                return False

            # Check mirror positions
            return (check(left.left, right.right) and
                    check(left.right, right.left))

        if root is None:
            return True

        return check(root.left, root.right)