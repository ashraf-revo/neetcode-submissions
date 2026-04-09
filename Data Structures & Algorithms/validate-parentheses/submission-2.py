class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        def is_open(c:str):
            return True if c=='(' or c=='[' or c =='{' else False

        def is_close(o:str,e:str):
            p=o+e
            return True if p=="{}" or p=="[]" or p=="()" else False


        for i in s:
            if is_open(i):
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                v=stack.pop()
                if not is_close(v,i):
                    return False
        return len(stack)==0                            