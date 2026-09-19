class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        avgSum=(sum(aliceSizes)+sum(bobSizes))//2
        bobSet=set(bobSizes)
        for i in range(len(aliceSizes)):
            diff = avgSum-sum(aliceSizes)
            b=diff+aliceSizes[i]
            if b in bobSet:
                return aliceSizes[i], b