# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        if root is None:
            return []
        d = deque()
        d.append(root)
        result = []
        while(len(d) > 0):
            level = len(d)
            levelElements = []
            for i in range(0, level):
                el = d.popleft()
                levelElements.append(el.val)
                if el.left is not None:
                    d.append(el.left)
                if el.right is not None:
                    d.append(el.right)
            result.append(levelElements)
        final = []
        for i in range(len(result)-1, -1, -1):
            final.append(result[i])
        return final