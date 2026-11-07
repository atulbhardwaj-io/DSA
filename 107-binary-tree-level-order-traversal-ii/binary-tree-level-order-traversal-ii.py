# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):

        if root is None:
            return []

        result = deque()
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()

            if level == len(result):
                result.appendleft([])

            result[-(level + 1)].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        return list(result)