# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if root is None:
            return []

        que = deque([root])
        result = []

        while que:
            length = len(que)

            for _ in range(length):
                node = que.popleft()
                if _ == length-1:
                    result.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return result


        