class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>=target:
                right=mid
        if nums[right]<target:
            right+=1
        return right