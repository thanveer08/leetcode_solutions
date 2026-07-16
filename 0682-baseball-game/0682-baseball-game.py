class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []
        for i in range (len(operations)):
            if operations[i] == "C":
                record.pop()
            elif operations[i] == "D":
                x = record[-1]
                record.append(2*x)    
            elif operations[i] == "+":
                x = record[-1]
                
                y = record[-2]
                record.append(x+y)
            else: 
                record.append(int(operations[i]))    
        return sum(record)        
                

            


            
        