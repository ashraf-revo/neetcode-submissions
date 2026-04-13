import queue
from dataclasses import dataclass
from typing import List

@dataclass()
class Node:
    val: int

    def __lt__(self, other):
        return other.val < self.val


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def smash(x, y):
            if x == y:
                return 0
            if x < y:
                return y - x
            else:
                return x - y

        q = queue.PriorityQueue()

        for i in stones:
            q.put(Node(i))

        while q.qsize()>1:
            x = q.get()
            y = q.get()
            r = Node(smash(x.val, y.val))
            if r.val != 0:
                q.put(r)

        return 0 if q.qsize()==0 else q.get().val
