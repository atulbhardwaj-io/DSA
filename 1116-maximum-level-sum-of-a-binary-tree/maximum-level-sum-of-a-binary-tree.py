# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxLevelSum(self, root):
        if root is None:
            return 0

        smallest_level = 0
        que = deque([root])
        count = 0
        maxi = float('-inf')

        while que:
            count += 1
            sumi = 0
            leng = len(que)

            for _ in range(leng):
                node = que.popleft()
                sumi = sumi + node.val

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

            if sumi > maxi:
                maxi = sumi
                smallest_level = count

        return smallest_level

    


            
