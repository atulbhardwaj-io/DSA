# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if root is None:
            return []
        
        result = []
        que = deque([root])
        
        while que:
            maxi = float('-inf')
            length = len(que)

            for _ in range(length):
                node = que.popleft()
                maxi = max(maxi,node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            result.append(maxi)

        return result