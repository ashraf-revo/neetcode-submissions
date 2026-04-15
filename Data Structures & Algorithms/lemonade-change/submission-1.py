class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mem={5:0,10:0,20:0}
        
        for b in bills:
            if b==5:
                mem[b] +=1
            elif b==10:
                if mem.get(5)>=1:
                    mem[5] -=1
                else:
                    return False
                mem[10] +=1
            else:
                ## 20 sub 5+5+5  or sub 10+5 
                if mem.get(5)>=3:
                    mem[5] -=3
                elif mem.get(5)>=1 and  mem.get(10)>=1:
                    mem[5] -=1
                    mem[10] -=1
                else:
                    return False
                mem[20] +=1
        return True
