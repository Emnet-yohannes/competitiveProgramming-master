class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)/3
        initial = len(piles)-2
        total = 0
        piles.sort()
        for i in range(int(n)):
            total+=piles[initial]
            initial -=2
        return total