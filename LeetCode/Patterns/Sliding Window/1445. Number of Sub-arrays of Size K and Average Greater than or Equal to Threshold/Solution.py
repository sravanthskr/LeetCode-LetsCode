class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        currSum=0
        for i in range(k):
            currSum+=arr[i]
        avg=currSum//k
        if avg>=threshold:
            count+=1
        for j in range(k, len(arr)):
            currSum=currSum+arr[j]-arr[j-k]
            avg=currSum//k
            if avg>=threshold:
                count+=1
        return count