from collections import namedtuple
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        Point=namedtuple("Point",["x","y"])
        root:Point=None
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    root=Point(i,j)
                    break
            if root:
                break        
        
        
        count:int=0

        def water(p:Point):
            ## impl code to return children not visited before

            result=[]

            if p.x>0:
                result.append(Point(p.x-1,p.y))

            if p.x<rows-1:   
                result.append(Point(p.x+1,p.y))

            if p.y>0:
                result.append(Point(p.x,p.y-1))

            if p.y<cols-1:   
                result.append(Point(p.x,p.y+1))

            return [i for i in result if grid[i.x][i.y] ==0]


        def count_stripes(p:Point):
            c=0
            if p.x==0:
                c +=1
            if p.y==0:
                c +=1
            if p.x+1==rows:
                c +=1    
            if p.y+1==cols:
                c +=1    
            c += len(water(p))
            return c


        def land(p:Point):
            ## impl code to return children not visited before

            result=[]

            if p.x>0:
                result.append(Point(p.x-1,p.y))

            if p.x<rows-1:   
                result.append(Point(p.x+1,p.y))

            if p.y>0:
                result.append(Point(p.x,p.y-1))

            if p.y<cols-1:   
                result.append(Point(p.x,p.y+1))

            print(f"children for {p} is {result}")
            return [i for i in result if grid[i.x][i.y] ==1]

        stack=[root]

        while stack:
            p=stack.pop()
            if grid[p.x][p.y]==1:
                grid[p.x][p.y]=-1
                count +=count_stripes(p)
                stack += land(p)

        return count