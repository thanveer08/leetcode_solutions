class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open,close,ds):
            if open == close == n:
                res.append(list(ds))
                return
            
            if open < n:
                ds.append("(")
                backtrack(open+1,close,ds)
                ds.pop()
            
            if open > close:
                
                ds.append(")")
                
                backtrack(open,close+1,ds)
                ds.pop()
        backtrack(0,0,[])
        return ["".join(x) for x in res]