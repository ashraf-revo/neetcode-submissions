class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def execute(x,y, c:chr):
            if c=='+':
                return x+y
            if c=='-':
                return y-x
            if c=='*':
                return x*y
            if c=='/':
                return int(y/x)
            return 0    


        stack=[]

        for token in tokens:
            if token not in ['+','-','*','/']:
                stack.append(int(token))
            else:
                x=stack.pop()    
                y=stack.pop()    
                executed=execute(x,y,token)
                print(x,y,token,executed)
                stack.append(executed)

        return stack[0]

