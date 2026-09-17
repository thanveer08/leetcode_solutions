# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        cols = defaultdict(list)
        min_col = 0
        max_col = 0
        res = []
        q = deque([(root,0,0)])
        while q:
            node,col,row = q.popleft()
            min_col,max_col = min(min_col,col),max(max_col,col)
            cols[col].append((row,node.val))
            if node.left:
                q.append((node.left,col-1,row+1))
            if node.right:
                q.append((node.right,col+1,row+1)) 
        for c in range(min_col,max_col+1):

            cols[c].sort()
            col_val= []
            for row, node in cols[c]:
                col_val.append(node)
            res.append(col_val)    
        return res        