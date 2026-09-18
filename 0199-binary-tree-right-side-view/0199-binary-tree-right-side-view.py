# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        res = []
        if not root:
            return []
        q = deque([(root,0)])
        min_row,max_row = 0,0
        rows = {}
        while q:
            node,row = q.popleft()
            min_row,max_row = min(min_row,row), max(max_row,row)
            if not row in rows:
                rows[row] = node.val 
            if node.right:
                q.append((node.right,row+1))
            if node.left:
                q.append((node.left,row+1))

        for r in range(min_row,max_row+1):
            res.append(rows[r])
        return res        
