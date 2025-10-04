# [10, 5, 15, 3, 7, None, 18]
# [[10], [5, 15], [3, 7, 18]]
from collections import deque

def bfs_queue(self, root):
    d = deque()
    d.append(root)
    result = []

    while(len(d) > 0):
        levelSize = len(d)
        levelElements = []
        for i in range(0, levelSize):
            el = d.popleft()
            levelElements.append(el)
            if el.left is not None:
                d.append(el.left)
            if el.right is not None:
                d.append(el.right)
        result.append(levelElements)
    return result