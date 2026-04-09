class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # using stack
        # every number append to stack
        # if + append poll 2 and add them and its sum
        # if D add 2*prev
        # if C poll and continue

        # at end sum(stack)
        def isdigit(s:str):
            try:
                return int(s)
            except:
                return None    
        stack=[]
        for i in operations:
            if isdigit(i):
                stack.append(int(i))
            else:
                if i=='+':
                    v1=0 if len(stack)==0 else stack.pop()    
                    v2=0 if len(stack)==0 else stack.pop()    
                    stack.append(v2)
                    stack.append(v1)
                    stack.append(v1+v2)
                elif i=='D':
                    if len(stack)>0:
                        v1=stack.pop()
                        stack.append(v1)
                        stack.append(v1*2)
                elif i=='C':
                    if len(stack)>0:
                        v1=stack.pop()
                else:
                    print("unknown")        
            print(f"after {i} is {stack}")
        return sum(stack)
        