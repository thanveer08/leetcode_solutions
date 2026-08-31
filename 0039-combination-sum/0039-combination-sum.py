class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack (index,current,target):
            if target<0:
                return
            if index == len(candidates):
                if target == 0:
                    res.append(list(current))
                return    

            current.append(candidates[index])
            backtrack(index,current,target-candidates[index])  
            current.pop()
            backtrack(index+1,current,target)      

        backtrack(0,[],target)
        return res    
