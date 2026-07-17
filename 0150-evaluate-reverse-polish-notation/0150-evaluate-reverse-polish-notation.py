class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(len(tokens)):
            if tokens[i] not in {"+", "-", "*", "/"}:
                stk.append(int(tokens[i]))
            else:
                if tokens[i] =="+":
                    b = stk.pop()
                    a = stk.pop()
                    stk.append(a+b)  
                elif  tokens[i] =="-":
                    b = stk.pop()
                    a = stk.pop()
                    stk.append(a-b)  
                elif tokens[i] == "*":
                    b = stk.pop()
                    a = stk.pop()
                    stk.append(a*b)    
                else:
                    b = stk.pop()
                    a = stk.pop()
                    stk.append(int(a/b)) 
        return stk[-1]            
