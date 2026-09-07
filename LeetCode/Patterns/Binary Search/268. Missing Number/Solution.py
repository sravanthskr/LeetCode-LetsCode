class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expectSum=n*(n+1)//2
        actualSum=sum(nums)
        return expectSum-actualSum
        
        # size=len(nums)
        # seen=set(nums)
        # for i in range(size+1):
        #     if i not in seen:
        #         return i