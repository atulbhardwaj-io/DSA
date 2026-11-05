# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        if root is None:
            return None

        result = []

        que = deque([root])

        while(que):
            node = que.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                que.append(node.left)

            if node.right:
                que.append(node.right)

        return root