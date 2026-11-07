# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):

        if root is None:
            return []

        result = []
        que = deque([root])

        while que:
            level_sum = 0.0
            level_count = len(que)

            for _ in range(level_count):
                node = que.popleft()
                level_sum += node.val

                # Add children inside the for loop
                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

            result.append(level_sum / level_count)

        return result