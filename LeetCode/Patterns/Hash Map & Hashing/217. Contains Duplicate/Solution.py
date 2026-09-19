class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nSet=set(nums)
        if len(nSet)!=len(nums):
            return True
        else:
            return False