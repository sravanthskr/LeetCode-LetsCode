class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size=len(nums)
        seen=set(nums)
        for i in range(size+1):
            if i not in seen:
                return i