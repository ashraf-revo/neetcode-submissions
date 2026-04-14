class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge=set()
        for i in trust:
            judge.add(i[1])

        return list(judge)[0] if len(judge)==1 else -1  