"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if root is None:
            return None

        root.next = None
        que = deque([root])

        while que:
            length = len(que)
            

            for _ in range(length):
                node = que.popleft()
                if _ == length-1:
                    node.next = None
                else:
                    node.next = que[0]

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return root


                