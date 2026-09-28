class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        aliceSum=sum(aliceSizes)
        bobSum=sum(bobSizes)
        avgSum=(aliceSum+bobSum)//2
        bobSet=set(bobSizes)
        for i in range(len(aliceSizes)):
            diff = avgSum-aliceSum
            b=diff+aliceSizes[i]
            if b in bobSet:
                return aliceSizes[i], b