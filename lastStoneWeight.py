class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            if x!=y:
                stones.append(y-x)
        if stones:
            return stones[0]
        return 0
